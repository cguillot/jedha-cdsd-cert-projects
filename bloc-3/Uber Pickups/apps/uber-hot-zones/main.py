from enum import Enum

import os
import requests
from pathlib import Path

import pandas as pd
import numpy as np

from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler

import plotly.graph_objects as go

import plotly.express as px

import streamlit as st

# Few definitions
class ClusteringMethod(Enum):
    DBSCAN = "dbscan"
    KMEANS = "kmeans"

EARTH_RADIUS_KM = 6371.0

DAYS_OF_WEEK = {
    0: "Lundi",
    1: "Mardi",
    2: "Mercredi",
    3: "Jeudi",
    4: "Vendredi",
    5: "Samedi",
    6: "Dimanche"
}

DAY_LABEL_TO_KEY = {v: k for k, v in DAYS_OF_WEEK.items()}

# Page start
st.set_page_config(layout="wide", page_title="Uber Hot Zones in New York © C. GUILLOT", page_icon=":taxi:")

# Hack to reduce top padding!
# in combination with: --client.toolbarMode=minimal --ui.hideTopBar=True
st.markdown("""
<style>
header.stAppHeader {
    background-color: transparent;
}
section.stMain .block-container {
    padding-top: 0rem;
    z-index: 1;
}
</style>""", unsafe_allow_html=True)

# Session init
if "sample_ratio" not in st.session_state:
    st.session_state.sample_ratio = 0.5

if "zones_weekday_name" not in st.session_state:
    st.session_state.zones_weekday_name = "Lundi"

if "zones_hour" not in st.session_state:
    st.session_state.zones_hour = 12

if "zones_clustering_method" not in st.session_state:
    st.session_state.zones_clustering_method = ClusteringMethod.DBSCAN

# Default parameters for clusters
if "zones_method_kmeans_n_clusters" not in st.session_state:
    st.session_state.zones_method_kmeans_n_clusters = 5

if "zones_method_dbscan_epsilon_km" not in st.session_state:
    st.session_state.zones_method_dbscan_epsilon_km = 1.3

if "zones_method_dbscan_min_samples" not in st.session_state:
    st.session_state.zones_method_dbscan_min_samples = 5

if "zones_map_density" not in st.session_state:
    st.session_state.zones_map_density = False

@st.cache_data
def load_data(sample_ratio):
    path = Path(__file__).parent / "data/uber-raw-data-sep14.zip"

    rides_df = pd.read_csv(
        path,
        names=[
            "date_time",
            "lat",
            "lon",
        ],
        skiprows=1,
        usecols=[0, 1, 2],  # ignore base column
        parse_dates=[
            "date_time"
        ],  # set as datetime instead of converting after the fact
    )

    # centering data
    for col in ["lat", "lon"] :
        col_mean = rides_df[col].mean()
        col_std = rides_df[col].std()
        # with 4 keep all airports
        range_min = col_mean - 4 * col_std
        range_max = col_mean + 4 * col_std

        rides_df = rides_df[(rides_df[col] > range_min) & (rides_df[col] <= range_max)]

    rides_df["dt_weekday"] = rides_df["date_time"].dt.dayofweek
    rides_df["dt_hour"] = rides_df["date_time"].dt.hour

    # Let reduce overall size by sampling dataset to a 50% per weekday/hour peer
    sampled_rides_df = rides_df.groupby(['dt_weekday', 'dt_hour'], group_keys=False).sample(frac=sample_ratio, random_state=42)

    # compute radians for DBSCAN haversine/balltree computations
    sampled_rides_df[["lat_rad", "lon_rad"]] = np.radians(sampled_rides_df[["lat", "lon"]])

    return sampled_rides_df

# Filter data (day, hour)
@st.cache_data
def weekday_rides_count_per_hour(df, weekday):
    hourly_counts = df[(df["dt_weekday"] == weekday)]['dt_hour'].value_counts().sort_index()

    hourly_df = hourly_counts.reset_index()
    hourly_df.columns = ['hour', 'count']

    return hourly_df

@st.cache_data
def weekday_hourly_rides(df, weekday, hour):
    return df[(df["dt_weekday"] == weekday) & (df["dt_hour"] == hour)]

@st.cache_data
def compute_zones_dbscan_method(data, epsilon_km, min_samples):
    print(f"compute_zones_dbscan_method for eps={epsilon_km} and min_samples={min_samples}")
    epsilon = epsilon_km / EARTH_RADIUS_KM

    dbscan = DBSCAN(eps=epsilon, min_samples=min_samples, metric="haversine", algorithm="ball_tree")

    # copy original data as we will extend it
    zones_data_df = data.copy()
    zones_data_df["cluster"] = "-1"

    data_to_clusterize_df = zones_data_df[["lat_rad", "lon_rad"]]

    dbscan.fit(data_to_clusterize_df)

    zones_data_df["cluster"] = dbscan.labels_

    # ensure use of discrete colors
    zones_data_df["cluster"] = zones_data_df["cluster"].astype(str)

    # compute centroids
    day_clusters_centroids_df = zones_data_df[zones_data_df["cluster"] != "-1"].groupby(["cluster"])[["lat", "lon"]].mean().reset_index()

    return zones_data_df, day_clusters_centroids_df

@st.cache_data
def compute_zones_kmeans_method(data, n_clusters, scale=True):

    # copy original data as we will extend it
    zones_data_df = data.copy()
    zones_data_df["cluster"] = "-1"

    data_to_clusterize_df = zones_data_df[["lat", "lon"]]

    # standardize data
    if scale is True:
        scaler = StandardScaler()
        data_to_clusterize_df = scaler.fit_transform(data_to_clusterize_df)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init = 'auto')

    zones_data_df["cluster"] = kmeans.fit_predict(data_to_clusterize_df)

    # Store cluster centroids (need to inverse scale of centroids)
    centroids_scaled = kmeans.cluster_centers_
    centroids_original = scaler.inverse_transform(centroids_scaled)

    zones_data_df["cluster"] = zones_data_df["cluster"].astype(str)

    day_clusters_centroids_df = pd.DataFrame(centroids_original, columns=['lat', 'lon'])

    return zones_data_df, day_clusters_centroids_df

def build_daily_rides_per_hour_chart(rides_df, zones_weekday, hour):
     # Nombre de courses par heure
    rides_count_per_hour_df = weekday_rides_count_per_hour(rides_df, zones_weekday)

    line_fig = px.line(rides_count_per_hour_df, x="hour", y="count", markers=True)
    line_fig.update_traces(mode="markers+lines", hovertemplate=None)
    line_fig.update_layout(hovermode="x unified", height=100)

    # Add vertical line at selected hour
    line_fig.add_vline(
        x=hour,
        line_dash="dash",
        line_color="red",
    )

    line_fig.update_layout(margin={"r":0,"t":10,"l":0,"b":0})

    return line_fig

st.header("Uber Hot Zones in New York © C. GUILLOT")

# STREAMLIT APP LAYOUT
with st.spinner("Chargement des données...", show_time=True):
    rides_df = load_data(st.session_state.sample_ratio)

col1, col2 = st.columns([1, 3])

with col1:
    zones_weekday_name = st.selectbox(
        "Hot Zones du :",
        list(DAYS_OF_WEEK.values()),
        key="zones_weekday_name"
    )

    zones_weekday = DAY_LABEL_TO_KEY[zones_weekday_name]

    # Streamlit selectbox
    zones_clustering_options = list(ClusteringMethod)

    zones_clustering_method = st.selectbox(
        "Méthode :",
        options=zones_clustering_options,
        key="zones_clustering_method",
        format_func=lambda method: method.value
    )

    # Display ride density or cluster groups
    st.toggle(
        "Density view",
        key="zones_map_density"
    )

with col2:
    zones_hour_slider_placeholder = st.empty()

    dily_rides_per_hour_chart_placeholder = st.empty()

    line_fig = build_daily_rides_per_hour_chart(rides_df, zones_weekday, st.session_state.zones_hour)

    line_chart_events = dily_rides_per_hour_chart_placeholder.plotly_chart(line_fig, theme=None, use_container_width=True, on_select="rerun", selection_mode="points")

    if line_chart_events:
        selected_points = line_chart_events["selection"]["points"]
        if len(selected_points) > 0:
            st.session_state.zones_hour = int(selected_points[0]["x"])

            # refresh chart
            line_fig = build_daily_rides_per_hour_chart(rides_df, zones_weekday, st.session_state.zones_hour)
            line_chart_events = dily_rides_per_hour_chart_placeholder.plotly_chart(line_fig, theme=None, use_container_width=True, on_select="rerun", selection_mode="points")


    zones_hour_slider_placeholder.slider(
        "Select hour for hot zones", 0, 23, key="zones_hour", format="%02d:00"
    )

@st.cache_resource
def build_hot_zones_map(hourly_df, clusters_df, density):
    if density is True:
        map_fig = px.density_map(
            hourly_df,
            lat="lat",
            lon="lon",
            z=None,
            radius=5,
            center={"lat": 40.742, "lon": -73.94},
            zoom=11,
            map_style="open-street-map",
            color_continuous_scale='inferno',
            height=800
        )
    else:
        map_fig = px.scatter_map(
            hourly_df[hourly_df["cluster"] != "-1"],
            lat="lat",
            lon="lon",
            color="cluster",
            center={"lat": 40.742, "lon": -73.94},
            zoom=11,
            map_style="open-street-map",
            height=800
        )


    centroids_fig = go.Scattermap(
        lat=clusters_df["lat"],
        lon=clusters_df["lon"],
        mode="markers+text",
        marker=dict(
            size=18,
            color="black",
            symbol="car"
        ),
        # name="",
        showlegend=False,
        text=[f"Zone {i}" for i in clusters_df.index],
        textposition="top right",
        subplot="map",
        customdata=np.stack(range(1, len(clusters_df) + 1), axis=-1),
        hovertemplate="<b>Zone %{customdata}</b><br>" +
                    "Lat: %{lat:.3f}<br>" +
                    "Lon: %{lon:.3f}<br><extra></extra>"
    )

    map_fig.add_trace(centroids_fig)

    map_fig.update_layout(margin={"r":0,"t":15,"l":0,"b":0})

    return map_fig

with st.spinner("Préparation de la carte...", show_time=True):
    hourly_df = weekday_hourly_rides(rides_df, zones_weekday, st.session_state.zones_hour)
    print("Shape of hourly data: ", hourly_df.shape)

    epsilon_km = st.session_state.zones_method_dbscan_epsilon_km
    min_samples = st.session_state.zones_method_dbscan_min_samples

    n_clusters = st.session_state.zones_method_kmeans_n_clusters

    print("Clustering method: ", st.session_state.zones_clustering_method)
    print("Clustering method: ", type(st.session_state.zones_clustering_method))

    if st.session_state.zones_clustering_method.value == ClusteringMethod.DBSCAN.value:
        zoned_rides_df, zone_centroids_df = compute_zones_dbscan_method(hourly_df, epsilon_km, min_samples)
    elif st.session_state.zones_clustering_method.value ==  ClusteringMethod.KMEANS.value:
        zoned_rides_df, zone_centroids_df = compute_zones_kmeans_method(hourly_df, n_clusters)
    else:
        print("Unrecognized clustering method!")

    hot_zones_fig = build_hot_zones_map(zoned_rides_df, zone_centroids_df, st.session_state.zones_map_density)
    st.plotly_chart(hot_zones_fig)
