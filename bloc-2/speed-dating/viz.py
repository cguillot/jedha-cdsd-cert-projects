import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

from speed_dating_document_context import LabelDecoder
from config import COLORS

def show_correlation_matrix(data: pd.DataFrame, figsize=(15, 15), corr_label_size=6.5, include_booleans=True):
    included_types = [np.number]
    if include_booleans:
        included_types.append(np.bool)

    colnames_numerical = data.select_dtypes(
        include=included_types).columns.tolist()

    corr = data[colnames_numerical].corr()

    # corr = df.corr()
    # corr_notna = ~corr.isna().all()
    # corr = corr.loc[corr_notna, corr_notna]

    # or as a one-liner
    # corr = df.corr().dropna(how='all', axis=1).dropna(how='all')

    # Unpivot the dataframe, so we can get pair of arrays for x and y
    corr = pd.melt(corr.reset_index(), id_vars='index')
    corr.columns = ['x', 'y', 'value']

    correlation_matrix_np(x=corr['x'],
                          y=corr['y'],
                          size=corr['value'].abs(),
                          color=corr['value'],
                          figsize=figsize,
                          corr_label_size=corr_label_size)

# CORRELATION MATRIX - CUSTOMIZED HEATMAP FUNCTION
# Credits: https://github.com/CoteDave/blog/blob/13432a3041e8d999ca91d34408cba0bee932222b/Demonstrating%20the%20power%20of%20feature%20engineering/Demonstrating%20the%20power%20of%20feature%20engineering%20-%20Part%20II.ipynb
def correlation_matrix_np(x, y, size, color, figsize=(15, 15), corr_label_size=6.5):
    _, ax = plt.subplots(figsize=figsize)

    ax.set_xticks([])
    ax.set_yticks([])

    # Mapping from column names to integer coordinates
    x_labels = [v for v in sorted(x.unique())]
    y_labels = [v for v in sorted(y.unique())]
    x_to_num = {p[1]: p[0] for p in enumerate(x_labels)}
    y_to_num = {p[1]: p[0] for p in enumerate(y_labels)}

    size_scale = 500

    n_colors = 256  # Use 256 colors for the diverging color palette
    palette = sns.diverging_palette(20, 220, n=n_colors)  # Create the palette
    # Range of values that will be mapped to the palette, i.e. min and max possible correlation
    color_min, color_max = [-1, 1]

    def value_to_color(val):
        if pd.isna(val):
            return sns.color_palette("Greys", n_colors=1)[0]

        # We first need to normalize the value to the [0, 1] range
        # position of value in the input range, relative to the length of the input range
        val_position = float((val - color_min)) / (color_max - color_min)
        # target index in the color palette
        ind = int(val_position * (n_colors - 1))
        return palette[ind]

    def compute_size(val):
        if pd.isna(val):
            return 0
        return val * size_scale

    plot_grid = plt.GridSpec(
        1, 15, hspace=0.2, wspace=0.1)  # Setup a 1x15 grid
    # Use the leftmost 14 columns of the grid for the main plot
    ax = plt.subplot(plot_grid[:, :-1])

    x_vals = list(x.map(x_to_num))
    y_vals = list(y.map(y_to_num))
    txt = round(color, 2).astype(str).tolist()
    for i, typ in enumerate(txt):
        ax.scatter(
            x=x_vals[i],  # Use mapping for x
            y=y_vals[i],  # Use mapping for y
            # Vector of square sizes, proportional to size parameter
            s=compute_size(size[i]),
            # Vector of square colors, mapped to color palette
            c=color[[i]].apply(value_to_color),
            edgecolors='grey',
            linewidths=0.5,
            marker='s'  # Use square as scatterplot marker
        )
        ax.text(x_vals[i]-0.05, y_vals[i]-0.4, typ,
                fontsize=corr_label_size, color='grey')
    ax.set_title('Correlation matrix')

    # Show column labels on the axes
    ax.set_xticks([x_to_num[v] for v in x_labels])
    ax.set_xticklabels(x_labels, rotation=45, horizontalalignment='right')
    ax.set_yticks([y_to_num[v] for v in y_labels])
    ax.set_yticklabels(y_labels)

    ax.grid(False, 'major')  # Turn off major gridlines
    ax.grid(True, 'minor')  # Turn on minor gridlines
    # Set gridlines to appear between integer coordinates
    ax.set_xticks([t + 0.5 for t in ax.get_xticks()], minor=True)
    ax.set_yticks([t + 0.5 for t in ax.get_yticks()],
                  minor=True)  # Do the same for y axis

    ax.set_xlim([-0.5, max([v for v in x_to_num.values()]) + 0.5])
    ax.set_ylim([-0.5, max([v for v in y_to_num.values()]) + 0.5])

    # Add color legend on the right side of the plot
    ax = plt.subplot(plot_grid[:, -1])  # Use the rightmost column of the plot

    col_x = [0]*len(palette)  # Fixed x coordinate for the bars
    # y coordinates for each of the n_colors bars
    y = np.linspace(color_min, color_max, n_colors)

    bar_height = y[1] - y[0]
    ax.barh(
        y=y,
        width=[5]*len(palette),  # Make bars 5 units wide
        left=col_x,  # Make bars start at 0
        height=bar_height,
        color=palette,
        linewidth=0
    )
    # Bars are going from 0 to 5, so lets crop the plot somewhere in the middle
    ax.set_xlim(1, 2)
    ax.grid(False)  # Hide grid
    ax.set_facecolor('white')  # Make background white
    ax.set_xticks([])  # Remove horizontal ticks
    # Show vertical ticks for min, middle and max
    ax.set_yticks(np.linspace(min(y), max(y), 3))
    ax.yaxis.tick_right()  # Show vertical ticks on the right

"""
    Show representations of attributes ratings (related to a phase/perspective bunch of attributes) per genre:
    - stacked bar plot
    - bar plot per attribute to ease comparison
    - polar plot to quickly view overall tendencies
"""
def plot_attribute_expectations_per_genre(df, attributes, title, palette_gender_label = None):

    expected_attributes_df = df[["gender_label"] + attributes].groupby("gender_label").mean()
    expected_attributes_df["Total"] = expected_attributes_df.sum(axis=1)

    # Remove "Total" from plot
    expected_attributes_plot_df = expected_attributes_df.iloc[:,:-1]

    # Computing labels
    labels_df = pd.DataFrame()

    legend_labels = []

    for c in expected_attributes_df.columns[:-1]:
        legend_labels.append(LabelDecoder.get_attribute_label(c))

        labels_df[c] = round((100 * expected_attributes_df[c] / expected_attributes_df["Total"]), 2)
        labels_df[c] = labels_df[c].map(lambda x: "" if x is None or x < 2.0 else str(x) + "%")

    fig, ax = plt.subplots(figsize = (12, 6))

    bplot = expected_attributes_plot_df.plot.bar(stacked = True,
                    ax = ax,
                    width = 0.3,
                    edgecolor = "black")

    bplot.set_title(title)
    bplot.set_xlabel("Genre")
    bplot.set_ylabel("Score")

    # Add legend with custom labels
    handles, _ = bplot.get_legend_handles_labels()
    bplot.legend(handles, legend_labels, title="Critères") # , loc="lower left", bbox_to_anchor=(1.01, 0.29)

    # Add labels
    for i, c in enumerate(bplot.containers):
        labels = labels_df.iloc[:, i].tolist()
        bplot.bar_label(c,label_type='center',labels=labels)

    ############################
    # barplot, group attributes ratings per genre to ease comparison
    long_format_df = expected_attributes_plot_df.stack().reset_index()
    long_format_df.columns = ['gender_label', 'attribute', 'score']

    long_format_df["attribute"] = long_format_df["attribute"].map(LabelDecoder.get_attribute_label)

    g = sns.catplot(data=long_format_df,
            x="gender_label", y="score",
            col="attribute",
            kind="bar", hue="gender_label", palette=palette_gender_label, height=5, aspect=.4)

    g.fig.subplots_adjust(top=0.85)
    g.fig.suptitle(title)

    g.set_axis_labels("", "Score")
    g.set_titles("{col_name}")

    labels_arr = labels_df.to_numpy()

    for i, ax in enumerate(g.axes.ravel()):
        # i: attribute name
        for j, c in enumerate(ax.containers):
            # j: Man/Woman
            labels = [labels_arr[j][i]]
            ax.bar_label(c, labels=labels, label_type='edge')

        ax.margins(y=0.2)

    ##################
    # Show polar plot
    # Expect wide format
    pp = create_attributes_polar_plot(expected_attributes_plot_df, title)
    pp.show()

"""
    Show polar representation of attributes ratings (related to a phase/perspective bunch of attributes) per genre
"""
def create_attributes_polar_plot(df, title: str = None, ) -> go.Figure:
    # Extract list of columns and rename labels
    cols = list(df.columns)
    labels = [LabelDecoder.get_attribute_label(c) for c in cols]

    # Create a Polar Chart
    fig = go.Figure()

    # Women Polar Chart
    fig.add_trace(go.Scatterpolar(
        r=df.loc['Woman'].values.tolist(),
        theta=labels,
        fill='toself',
        line_color=COLORS["woman"],
        name='Woman'
    ))
    # Men Polar Chart
    fig.add_trace(go.Scatterpolar(
        r=df.loc['Man'].values.tolist(),
        theta=labels,
        fill='toself',
        line_color=COLORS["man"],
        name='Man'
    ))
    # Set Title and Value Range of Polar Chart
    fig.update_layout(
        title=title.replace("\n", "<br>"),
        title_x=0.5,
        width=700,
        height=500,
        polar=dict(
            radialaxis=dict(
                visible=False
            )),
        showlegend=True
    )

    return fig
