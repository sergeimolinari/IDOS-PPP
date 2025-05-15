"""Task running the results formatting (plots of trend by 3p index)."""

import pandas as pd

from idos_ppp.config import BLD
from idos_ppp.final.idos_plot import plot_boxplots
from idos_ppp.parameters import country_lists, three_p_indexes

inputs_plots = {
    list_name: BLD / "data" / "subsets" / f"{list_name}_data.pkl"
    for list_name in country_lists.keys()
}
inputs_plots["merged_dataframe_countries"] = BLD / "data" / "merged_data.pkl"


# Boxplots -> Function: Create a function to create a boxplot for each of the 3P indexes over the years.


products_plots = []
for list_name in inputs_plots:
    for index in three_p_indexes:
        products_plots.append(
            BLD / "final" / "boxplots" / f"{list_name}" / f"{index}_boxplot.png",
        )


def task_plot_boxplots(
    stat_values=inputs_plots,
    produces=products_plots,
):
    """Task to plot boxplots for each of the 3P indexes over the years."""
    for list_name, stat_data_path in stat_values.items():
        stat_data = pd.read_pickle(stat_data_path)
        output_png_file_path = BLD / "final" / "boxplots" / f"{list_name}"
        plot_boxplots(stat_data, output_png_file_path)
