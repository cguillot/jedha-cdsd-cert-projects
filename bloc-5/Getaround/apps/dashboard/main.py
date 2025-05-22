import os
import requests

import pandas as pd
import numpy as np

import plotly.graph_objects as go

import streamlit as st

st.set_page_config(page_title="Getaround: dashboard des locations", page_icon="🚗", layout="wide")
st.header("Getaround: dashboard des locations")
st.markdown("""
Retrouvez sur ce dashboard l'ensemble des informations vous permettant de comprendre le panel des locations chez Getaround ainsi que les impacts du futur delais entre réservation.

Vous disposez également d'un outils d'aide à l'estimation du juste prix.
""")

#########################################################################################################
# Loading & pre-processing base data
#########################################################################################################
@st.cache_data
def load_data():
    delay_analysis_raw_df = pd.read_excel("./data/get_around_delay_analysis.xlsx", sheet_name="rentals_data")

    # Enforce types
    delay_analysis_raw_df['rental_id'] = delay_analysis_raw_df['rental_id'].astype(pd.Int64Dtype())
    delay_analysis_raw_df['previous_ended_rental_id'] = delay_analysis_raw_df['previous_ended_rental_id'].astype(pd.Int64Dtype())

    # Outliers removal
    def get_outliers_mask(df_in, col_name, keep_na=True):
        q1 = df_in[col_name].quantile(0.25)
        q3 = df_in[col_name].quantile(0.75)
        iqr = q3-q1 #Interquartile range
        fence_low  = q1-1.5*iqr
        fence_high = q3+1.5*iqr
        if keep_na:
            mask_out = df_in[col_name].isna() | ((df_in[col_name] > fence_low) & (df_in[col_name] < fence_high))
        else:
            mask_out = (df_in[col_name] > fence_low) & (df_in[col_name] < fence_high)

        return mask_out

    outliers_mask = get_outliers_mask(delay_analysis_raw_df, "delay_at_checkout_in_minutes")
    delay_analysis_df = delay_analysis_raw_df[outliers_mask]

    # Extra features engineering
    delay_analysis_df = delay_analysis_df.merge(
        delay_analysis_df[["rental_id", "delay_at_checkout_in_minutes"]].rename(columns={
            "rental_id": "previous_ended_rental_id",
            "delay_at_checkout_in_minutes": "previous_delay_at_checkout_in_minutes"
        }),
        on="previous_ended_rental_id",
        how="left"
    )

    delay_analysis_df["time_delta_with_previous_checkout_in_minutes"] = delay_analysis_df["time_delta_with_previous_rental_in_minutes"] - delay_analysis_df["previous_delay_at_checkout_in_minutes"]

    # Categorizing checkout delay
    def map_delay_to_status(delay):
        if pd.isna(delay):
            return "free"
        elif delay < 0:
            return "in-advance"
        elif delay == 0:
            return "on-time"
        else:
            return "delayed"

    # Categorizing time_delta for checkin
    def map_time_delta_to_status(time_delta):
        if time_delta < 0:
            return "checkin-delayed"
        else: # NA or >= 0
            return "checkin-ok"

    # delay_at_checkout
    delay_analysis_df["delay_at_checkout_status"] = delay_analysis_df["delay_at_checkout_in_minutes"].map(map_delay_to_status)
    delay_analysis_df["previous_delay_at_checkout_status"] = delay_analysis_df["previous_delay_at_checkout_in_minutes"].map(map_delay_to_status)

    # time_delta
    delay_analysis_df["time_delta_with_previous_checkout_status"] = delay_analysis_df["time_delta_with_previous_checkout_in_minutes"].map(map_time_delta_to_status)

    # st.dataframe(delay_analysis_df, use_container_width=True)

    #########################################################################################################
    # Building data report for rental delta impact
    #########################################################################################################
    # On utilise un step de 30 minutes afin de calculer l'impact sur l'ensemble des locations
    min_time_delta_thresholds = [td for td in range(0, 720, 30)]

    # impacted_planned_rentals_count
    # impacted_real_on_time_rentals_count
    # impacted_real_checkin_delayed_rentals_count
    # impacted_planned_checkout_delayed_rentals_count
    # unimpacted_rentals_count
    def compute_rental_delta_impact(checkin_type, rental_delta_in_minutes, df):
        # planned: time_delta_with_previous_rental_in_minutes
        # real: time_delta_with_previous_checkout_in_minutes

        impacted_df = df[df["checkin_type"] == checkin_type]


        planned_rentals_df = impacted_df[impacted_df["time_delta_with_previous_rental_in_minutes"] < rental_delta_in_minutes]

        real_rentals_df = impacted_df[(impacted_df["time_delta_with_previous_checkout_in_minutes"] >= 0) & (impacted_df["time_delta_with_previous_checkout_in_minutes"] < rental_delta_in_minutes)]

        impacted_planned_rentals_count = len(planned_rentals_df)

        # checkin-ok
        impacted_real_on_time_rentals_count = len(real_rentals_df[real_rentals_df["time_delta_with_previous_checkout_status"] == "checkin-ok"])
        # checkin-delayed (location rendue trop en retard par rapport au checkin planifié)
        impacted_real_checkin_delayed_rentals_count = len(planned_rentals_df[planned_rentals_df["time_delta_with_previous_checkout_status"] == "checkin-delayed"])

        # Location précédente rendue en retard dans l'intervale du rental_delta
        impacted_planned_checkout_delayed_rentals_count = len(planned_rentals_df[(planned_rentals_df["delay_at_checkout_in_minutes"] > 0) & (planned_rentals_df["delay_at_checkout_in_minutes"] < rental_delta_in_minutes)])
        impacted_planned_previous_checkout_delayed_rentals_count = len(planned_rentals_df[(planned_rentals_df["previous_delay_at_checkout_in_minutes"] > 0) & (planned_rentals_df["previous_delay_at_checkout_in_minutes"] < rental_delta_in_minutes)])

        return {
            "checkin_type": checkin_type,
            "impacted_planned_rentals_count": impacted_planned_rentals_count,
            "impacted_real_on_time_rentals_count": impacted_real_on_time_rentals_count,
            "impacted_real_checkin_delayed_rentals_count": impacted_real_checkin_delayed_rentals_count,
            "impacted_planned_checkout_delayed_rentals_count": impacted_planned_checkout_delayed_rentals_count,
            "impacted_planned_previous_checkout_delayed_rentals_count": impacted_planned_previous_checkout_delayed_rentals_count,
        }

    chained_rentals_df = delay_analysis_df[delay_analysis_df["previous_ended_rental_id"].notna()]

    rental_delta_impact = []

    for min_rental_delta_t in min_time_delta_thresholds:
        row = compute_rental_delta_impact("mobile", min_rental_delta_t, chained_rentals_df)
        row["rental_delta"] = min_rental_delta_t
        rental_delta_impact.append(row)

        row = compute_rental_delta_impact("connect", min_rental_delta_t, chained_rentals_df)
        row["rental_delta"] = min_rental_delta_t
        rental_delta_impact.append(row)

    rental_delta_impact_df = pd.DataFrame(rental_delta_impact)

    return delay_analysis_df, chained_rentals_df, rental_delta_impact_df

with st.spinner("Chargement des données...", show_time=True):
    delay_analysis_df, chained_rentals_df, rental_delta_impact_df = load_data()

#########################################################################################################
# Global metrics
#########################################################################################################
st.subheader("Informations générales")

# Rentals
rentals_count = len(delay_analysis_df)
ended_rentals_count = len(delay_analysis_df[delay_analysis_df["state"] == "ended"])
canceled_rentals_count = len(delay_analysis_df[delay_analysis_df["state"] == "canceled"])

connect_rentals_count = len(delay_analysis_df[delay_analysis_df["checkin_type"] == "connect"])
canceled_connect_rentals_count = len(delay_analysis_df[(delay_analysis_df["checkin_type"] == "connect") & (delay_analysis_df["state"] == "canceled")])

mobile_rentals_count = len(delay_analysis_df[delay_analysis_df["checkin_type"] == "mobile"])
canceled_mobile_rentals_count = len(delay_analysis_df[(delay_analysis_df["checkin_type"] == "mobile") & (delay_analysis_df["state"] == "canceled")])

# Delays
delays_count = len(delay_analysis_df[delay_analysis_df["delay_at_checkout_status"] == "delayed"])
mean_delays_in_minutes = delay_analysis_df[delay_analysis_df["delay_at_checkout_status"] == "delayed"]["delay_at_checkout_in_minutes"].mean()

checkin_delayed_count = len(delay_analysis_df[(delay_analysis_df["delay_at_checkout_status"] == "delayed") & (delay_analysis_df["time_delta_with_previous_checkout_status"] == "checkin-delayed")])
mean_checkin_delay_impact_in_minutes = delay_analysis_df[(delay_analysis_df["delay_at_checkout_status"] == "delayed") & (delay_analysis_df["time_delta_with_previous_checkout_status"] == "checkin-delayed")]["time_delta_with_previous_checkout_in_minutes"].mean()
mean_checkin_delay_impact_in_minutes = np.abs(mean_checkin_delay_impact_in_minutes)

# Successive rentals
# Locations en chaine
chained_rentals_count = len(chained_rentals_df)

# chained_rentals_delta_time_max = chained_rentals_df["time_delta_with_previous_rental_in_minutes"].max()
# chained_rentals_delta_time_max_str = "{:02.0f}h:{:02.0f}".format(*divmod(chained_rentals_delta_time_max, 60))

def percent_str(part_value, total_value):
    return f"{part_value * 100 / total_value:.1f}%"

rentals_col_1, delay_col_2 = st.columns(2)

with rentals_col_1:
    st.subheader("Locations")

    st.metric("Total", f"{rentals_count}")
    st.markdown(f":red[{canceled_rentals_count} ({percent_str(canceled_rentals_count, rentals_count)}) canceled]")

    st.metric("Connect", f"{connect_rentals_count} ({percent_str(connect_rentals_count, rentals_count)})")
    st.markdown(f":red[{canceled_connect_rentals_count} ({percent_str(canceled_connect_rentals_count, connect_rentals_count)}) canceled]")

    st.metric("Mobile", f"{mobile_rentals_count} ({percent_str(mobile_rentals_count, rentals_count)})")
    st.markdown(f":red[{canceled_mobile_rentals_count} ({percent_str(canceled_mobile_rentals_count, mobile_rentals_count)}) canceled]")

with delay_col_2:
    st.subheader("Retards")
    st.metric("Total", f"{delays_count} ({percent_str(delays_count, rentals_count)} des locations)")
    st.metric("Moyen", f"{mean_delays_in_minutes:.0f} minutes")
    st.metric("Check-ins impactés", f"{checkin_delayed_count} ({percent_str(checkin_delayed_count, delays_count)} des retards)")
    st.metric("Retard moyen des check-ins", f"{mean_checkin_delay_impact_in_minutes} minutes")

#########################################################################################################
# Helpers tabs
#########################################################################################################

st.divider()

tab_delay_impact, tab_price_tool = st.tabs(["📊 Impact des délais", "📝 Outils: prix de location"])

#########################################################################################################
# Formulaire d'évaluation de l'impact d'un delais entre locations
#########################################################################################################
with tab_delay_impact:
    st.subheader(f"Impact d'un délai tampon sur les {chained_rentals_count} locations successives")

    # Rental delay selection
    rental_deltas = rental_delta_impact_df[rental_delta_impact_df["rental_delta"] > 0]["rental_delta"].unique()

    threshold = st.select_slider(
        "Selectionnez le délai minimum à respecter entre 2 locations (minutes)",
        options=rental_deltas,
        value=30,
    )

    st.markdown(f"### Détails de l'impact d'un delai de {threshold} minutes")

    #########################################################################################################
    # General impacted metrics
    #########################################################################################################
    impacted_rows = rental_delta_impact_df[rental_delta_impact_df["rental_delta"] == threshold]

    delta_impact_col_1, delta_impact_col_2, delta_impact_col_3 = st.columns(3)
    if len(impacted_rows) > 0:
        # Total rentals
        impacted_rentals_count = int(impacted_rows["impacted_planned_rentals_count"].sum())

        # Conflicts avoided due to rental delta impact
        conflicts_count = int(chained_rentals_df[chained_rentals_df["time_delta_with_previous_checkout_status"] == "checkin-delayed"]["rental_id"].count())
        impacted_conflicts_count = int(impacted_rows["impacted_real_checkin_delayed_rentals_count"].sum())

        with delta_impact_col_1:
            st.metric("Location affectées", f"{impacted_rentals_count} sur {ended_rentals_count} ({percent_str(impacted_rentals_count, ended_rentals_count)})")
            st.metric("Conflit évités", f"{impacted_conflicts_count} sur {conflicts_count} ({percent_str(impacted_conflicts_count, conflicts_count)})")

        with delta_impact_col_2:
            impacted_connect_rentals_count = int(impacted_rows[impacted_rows["checkin_type"] == "connect"]["impacted_planned_rentals_count"].sum())
            st.metric("Location connect affectées", f"{impacted_connect_rentals_count} ({percent_str(impacted_connect_rentals_count, impacted_rentals_count)})")

            impacted_connect_conflicts_count = int(impacted_rows[impacted_rows["checkin_type"] == "connect"]["impacted_real_checkin_delayed_rentals_count"].sum())
            st.metric("Conflit connect évités", f"{impacted_connect_conflicts_count} ({percent_str(impacted_connect_conflicts_count, impacted_conflicts_count)})")


        with delta_impact_col_3:
            impacted_mobile_rentals_count = int(impacted_rows[impacted_rows["checkin_type"] == "mobile"]["impacted_planned_rentals_count"].sum())
            st.metric("Location mobile affectées", f"{impacted_mobile_rentals_count} ({percent_str(impacted_mobile_rentals_count, impacted_rentals_count)})")

            impacted_mobile_conflicts_count = int(impacted_rows[impacted_rows["checkin_type"] == "mobile"]["impacted_real_checkin_delayed_rentals_count"].sum())
            st.metric("Conflit mobile évités", f"{impacted_mobile_conflicts_count} ({percent_str(impacted_mobile_conflicts_count, impacted_conflicts_count)})")

    #########################################################################################################
    # Overall impact chart
    #########################################################################################################
    y_columns = [
        "impacted_planned_rentals_count",
        "impacted_real_on_time_rentals_count",
        "impacted_real_checkin_delayed_rentals_count",
        "impacted_planned_previous_checkout_delayed_rentals_count"
    ]

    # Dictionnaire de noms lisibles
    human_names = {
        "impacted_planned_rentals_count": "🔢 Locations planifiées impactées",
        "impacted_real_on_time_rentals_count": "⏱️ Locations réellement impactées",
        "impacted_real_checkin_delayed_rentals_count": "🐢 Retards réel entrainé au départ",
        "impacted_planned_previous_checkout_delayed_rentals_count": "⏮️ Tous les retards au checkout"
    }

    def plot_checkin_type(df, checkin_type):
        plot_df = df[df["checkin_type"] == checkin_type]

        fig = go.Figure()

        for col in y_columns:
            grouped = plot_df.groupby("rental_delta")[col].sum().reset_index()
            fig.add_trace(go.Scatter(
                x=grouped["rental_delta"],
                y=grouped[col],
                mode="lines+markers",
                name=human_names[col]
            ))

        fig.update_layout(
            title="Checkin Type: Connect",
            xaxis_title="rental_delta",
            yaxis_title="Valeurs",
            legend_title="Métriques",
            hovermode="x unified",
        )

        # fig.show()
        return fig

    mobile_fig = plot_checkin_type(rental_delta_impact_df, "mobile")
    connect_fig = plot_checkin_type(rental_delta_impact_df, "connect")

    mobile_fig.add_vline(x=threshold,line=dict(color="red", dash="dash"))
    connect_fig.add_vline(x=threshold,line=dict(color="red", dash="dash"))

    # Ajout du marqueur pour le rental delta sélectionné
    st.plotly_chart(mobile_fig, use_container_width=True)
    st.plotly_chart(connect_fig, use_container_width=True)

#########################################################################################################
# Formulaire d'estimation de prix
#########################################################################################################
with tab_price_tool:
    st.subheader("Formulaire de saisie du véhicule")

    st.markdown("Veuillez remplir les informations du véhicule afin d'obtenir une estimation du prix de location.")

    # Formulaire utilisateur
    with st.form("predict_form"):
        model_key = st.selectbox("Marque", [
            "Citroën", "Peugeot", "PGO", "Renault", "Audi", "BMW", "Ford", "Mercedes", "Opel",
            "Porsche", "Volkswagen", "KIA Motors", "Alfa Romeo", "Ferrari", "Fiat", "Lamborghini",
            "Maserati", "Lexus", "Honda", "Mazda", "Mini", "Mitsubishi", "Nissan", "SEAT",
            "Subaru", "Suzuki", "Toyota", "Yamaha"
        ])

        mileage = st.number_input("Kilométrage", min_value=0)
        engine_power = st.number_input("Puissance moteur (ch)", min_value=0)

        fuel = st.selectbox("Type de carburant", ["diesel", "petrol", "hybrid_petrol", "electro"])
        paint_color = st.selectbox("Couleur", ["black", "grey", "white", "red", "silver", "blue", "orange", "beige", "brown", "green"])
        car_type = st.selectbox("Type de voiture", ["convertible", "coupe", "estate", "hatchback", "sedan", "subcompact", "suv", "van"])

        private_parking_available = st.checkbox("Parking privé disponible", value=False)
        has_gps = st.checkbox("GPS intégré", value=False)
        has_air_conditioning = st.checkbox("Climatisation", value=False)
        automatic_car = st.checkbox("Boîte automatique", value=False)
        has_getaround_connect = st.checkbox("Getaround Connect", value=False)
        has_speed_regulator = st.checkbox("Régulateur de vitesse", value=False)
        winter_tires = st.checkbox("Pneus hiver", value=False)

        submitted = st.form_submit_button("🔍 Estimer le prix")

    # Envoi de la requête à l'API
    if submitted:
        api_url = os.getenv("CDSD_B5_GETAROUND_PREDICT_API_ENDPOINT_URL", "https://pikaboum-cdsd-bloc-5-getaround-api.hf.space/predict")
        payload = {
            "data": [{
                "model_key": model_key,
                "mileage": mileage,
                "engine_power": engine_power,
                "fuel": fuel,
                "paint_color": paint_color,
                "car_type": car_type,
                "private_parking_available": private_parking_available,
                "has_gps": has_gps,
                "has_air_conditioning": has_air_conditioning,
                "automatic_car": automatic_car,
                "has_getaround_connect": has_getaround_connect,
                "has_speed_regulator": has_speed_regulator,
                "winter_tires": winter_tires
            }]
        }

        try:
            response = requests.post(api_url, json=payload)
            response.raise_for_status()
            result = response.json()

            st.success(f"💰 Prix recommandé : {result['recommended_rental_prices'][0]:.2f} $ par jour")
        except requests.exceptions.RequestException as e:
            st.error(f"Erreur lors de l'appel API : {e}")
        except KeyError:
            st.error("La réponse de l'API n'est pas conforme.")
