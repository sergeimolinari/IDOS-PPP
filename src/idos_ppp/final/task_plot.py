"""Tasks for plotting the data."""

import matplotlib.pyplot as plt
import pandas as pd

from idos_ppp.config import BLD
from idos_ppp.final.idos_plot import (
    plot_boxplots,
    plot_comparative_bar_chart,
    plot_correlation,
    plot_interactive_plots,
)
from idos_ppp.parameters import country_lists, three_p_indexes, years

inputs_plots = {
    list_name: BLD / "data" / "subsets" / f"{list_name}_data.pkl"
    for list_name in country_lists.keys()
}
inputs_plots["merged_dataframe_countries"] = BLD / "data" / "merged_data.pkl"


inputs_prot_prov_correlations = {
    list_name: BLD
    / "analysis"
    / "prot_prov_correlations"
    / f"{list_name}_yearly_prot_prov_correlations.pkl"
    for list_name in country_lists.keys()
}
inputs_prot_prov_correlations["merged_dataframe_countries"] = (
    BLD
    / "analysis"
    / "prot_prov_correlations"
    / "merged_dataframe_yearly_prot_prov_correlations.pkl"
)

inputs_prov_part_correlations = {
    list_name: BLD
    / "analysis"
    / "prov_part_correlations"
    / f"{list_name}_yearly_prov_part_correlations.pkl"
    for list_name in country_lists.keys()
}
inputs_prov_part_correlations["merged_dataframe_countries"] = (
    BLD
    / "analysis"
    / "prov_part_correlations"
    / "merged_dataframe_yearly_prov_part_correlations.pkl"
)

inputs_prot_part_correlations = {
    list_name: BLD
    / "analysis"
    / "prot_part_correlations"
    / f"{list_name}_yearly_prot_part_correlations.pkl"
    for list_name in country_lists.keys()
}
inputs_prot_part_correlations["merged_dataframe_countries"] = (
    BLD
    / "analysis"
    / "prot_part_correlations"
    / "merged_dataframe_yearly_prot_part_correlations.pkl"
)


# Boxplots -> Function: Create a function to create a boxplot for each of the 3P indexes over the years.


products_boxplots = []
for list_name in inputs_plots:
    for index in three_p_indexes:
        products_boxplots.append(
            BLD
            / "final"
            / "boxplots"
            / f"{list_name}"
            / f"{index.capitalize()}_boxplot.png",
        )


def task_plot_boxplots(
    input_values=inputs_plots,
    produces=products_boxplots,
):
    """Task to plot boxplots for each of the 3P indexes over the years."""
    for list_name, data_path in input_values.items():
        data = pd.read_pickle(data_path)
        output_png_file_path = BLD / "final" / "boxplots" / f"{list_name}"
        plot_boxplots(data, output_png_file_path)


# Scatterplots for correlations -> Function: Create a function to create a heatmap for the correlation of the 3P indexes over the years.


products_prot_prov_correlations = []
for list_name in inputs_prot_prov_correlations:
    products_prot_prov_correlations.append(
        BLD
        / "final"
        / "prot_prov_correlations"
        / f"{list_name}"
        / f"{list_name}_correlation.png",
    )


def task_plot_prot_prov_correlations(
    input_values=inputs_prot_prov_correlations,
    produces=products_prot_prov_correlations,
):
    """Task to plot correlation between protection and provision for each dataset over the years."""
    for list_name, data_path in input_values.items():
        data = pd.read_pickle(data_path)
        output_png_file_path = BLD / "final" / "prot_prov_correlations" / f"{list_name}"
        plot_correlation(data, output_png_file_path)


products_prov_part_correlations = []
for list_name in inputs_prov_part_correlations:
    products_prov_part_correlations.append(
        BLD
        / "final"
        / "prov_part_correlations"
        / f"{list_name}"
        / f"{list_name}_correlation.png",
    )


def task_plot_prov_part_correlations(
    input_values=inputs_prov_part_correlations,
    produces=products_prov_part_correlations,
):
    """Task to plot correlation between provision and participation for each dataset over the years."""
    for list_name, data_path in input_values.items():
        data = pd.read_pickle(data_path)
        output_png_file_path = BLD / "final" / "prov_part_correlations" / f"{list_name}"
        plot_correlation(data, output_png_file_path)


products_prot_part_correlations = []
for list_name in inputs_prot_part_correlations:
    products_prot_part_correlations.append(
        BLD
        / "final"
        / "prot_part_correlations"
        / f"{list_name}"
        / f"{list_name}_correlation.png",
    )


def task_plot_prot_part_correlations(
    input_values=inputs_prot_part_correlations,
    produces=products_prot_part_correlations,
):
    """Task to plot correlation heatmap for each dataset over the years."""
    for list_name, data_path in input_values.items():
        data = pd.read_pickle(data_path)
        output_png_file_path = BLD / "final" / "prot_part_correlations" / f"{list_name}"
        plot_correlation(data, output_png_file_path)


# Bar Charts -> Create a bar chart to compare the values of key indices between countries for a specific year.


products_comparative_bar_charts = []
for year in years:
    products_comparative_bar_charts.append(
        BLD
        / "final"
        / "lebanon_and_yemen"
        / "comparative_bar_charts"
        / f"bar_chart_{year}.png",
    )


def task_plot_comparative_bar_charts(
    input_data=BLD
    / "data"
    / "subsets"
    / "conflict_and_postconflict_countries_data.pkl",
    produces=products_comparative_bar_charts,
):
    """Task to plot comparative bar charts for each dataset over the years."""
    data = pd.read_pickle(input_data)
    data = data.reset_index()
    output_dir = BLD / "final" / "lebanon_and_yemen" / "comparative_bar_charts"
    for year in years:
        plot_comparative_bar_chart(data, year, three_p_indexes)
        plt.savefig(output_dir / f"bar_chart_{year}.png")
        plt.close()


# Create interactive plots using Plotly to allow to explore the data dynamically.


def task_plot_interactive_plots_lebanon_and_yemen(
    input_data=BLD
    / "data"
    / "subsets"
    / "conflict_and_postconflict_countries_data.pkl",
    produces=BLD
    / "final"
    / "lebanon_and_yemen"
    / "interactive_plots"
    / "lebanon_and_yemen_interactive_plot.html",
):
    """Task to plot interactive plots for conflict and post-conflict countries over the years."""
    data = pd.read_pickle(input_data)
    data = data.reset_index()
    output_dir = BLD / "final" / "lebanon_and_yemen" / "interactive_plots"
    plot_interactive_plots(data, three_p_indexes, output_dir, list_name = "lebanon_and_yemen")


products_interactive_plots = []
for list_name in inputs_plots:
    products_interactive_plots.append(
        BLD
        / "final"
        / "interactive_line_plots"
        / f"{list_name}_interactive_plot.html",
    )

def task_plot_interactive_plots(
    input_data=inputs_plots,
    produces=products_interactive_plots,
):
    """Task to plot interactive plots for each dataset over the years."""
    for list_name, data_path in input_data.items():
        data = pd.read_pickle(data_path)
        data = data.reset_index()
        output_html_file_path = BLD / "final" / "interactive_line_plots"
        plot_interactive_plots(data, three_p_indexes, output_html_file_path, list_name)