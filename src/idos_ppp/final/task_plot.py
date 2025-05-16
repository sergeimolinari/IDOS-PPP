"""Task running the results formatting (plots of trend by 3p index)."""

import pandas as pd

from idos_ppp.config import BLD
from idos_ppp.final.idos_plot import plot_boxplots, plot_correlation_heatmap
from idos_ppp.parameters import country_lists, three_p_indexes, years

inputs_plots = {
    list_name: BLD / "data" / "subsets" / f"{list_name}_data.pkl"
    for list_name in country_lists.keys()
}
inputs_plots["merged_dataframe_countries"] = BLD / "data" / "merged_data.pkl"


inputs_stat_plots = {
    list_name: BLD / "analysis" / "statistical_analysis" / f"{list_name}_yearly_statistics.pkl"
    for list_name in country_lists.keys()
}
inputs_stat_plots["merged_dataframe_yearly_statistics"] = BLD / "analysis" / "statistical_analysis" / "merged_dataframe_yearly_statistics.pkl"


# Boxplots -> Function: Create a function to create a boxplot for each of the 3P indexes over the years.


products_boxplots = []
for list_name in inputs_plots:
    for index in three_p_indexes:
        products_boxplots.append(
            BLD / "final" / "boxplots" / f"{list_name}" / f"{index}_boxplot.png",
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


# Heatmaps -> Function: Create a function to create a heatmap for the correlation of the 3P indexes over the years.

# PROBLEMMMMMMMM

products_correlation_heatmap = []
for list_name in inputs_stat_plots:
    for year in years:
        products_correlation_heatmap.append(
            BLD / "final" / "correlation_heatmaps" / f"{list_name}" / f"{year}_correlation_heatmap.png",
        )


def task_plot_correlation_heatmap(
    input_values=inputs_plots,
    produces=products_correlation_heatmap,
):
    """Task to plot correlation heatmap for each dataset over the years."""
    for list_name, data_path in input_values.items():
        data = pd.read_pickle(data_path)
        output_png_file_path = BLD / "final" / "correlation_heatmaps" / f"{list_name}"
        plot_correlation_heatmap(data, output_png_file_path)
