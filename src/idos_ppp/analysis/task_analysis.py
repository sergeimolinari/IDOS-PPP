"""Tasks running the core analyses."""

import pandas as pd

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

from idos_ppp.analysis.idos_dataanalysis import (
    process_and_save_country_list,
    calculate_yearly_continent_correlations,
    calculate_yearly_correlations,
)
from idos_ppp.analysis.idos_trends import (
    calculate_mean_by_continent,
    calculate_statistics_by_continent,
)
from idos_ppp.config import BLD
from idos_ppp.parameters import country_lists

# Create filtered datasets for each list of countries

products = {list_name: BLD / "analysis" / f"{list_name}_data.csv" for list_name in country_lists.keys()}

def task_process_and_save_country_list(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces= products,
):
    """Task to create datasets constrained to countries in specified lists."""
    data = pd.read_pickle(merged_data)
    for list_name, country_list in country_lists.items():
        filtered_data = process_and_save_country_list(data, country_list)
        output_csv_file_path = BLD / "analysis" / f"{list_name}_data.csv"
        filtered_data.to_csv(output_csv_file_path) # Save the filtered DataFrame as a CSV


# Correlation Analysis -> Function: Create a function to calculate and visualize the correlation between protection and provision.


def task_correlation_year(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "yearly_correlations.arrow",
):
    """Task to calculate yearly correlations between protection and provision."""
    data = pd.read_pickle(merged_data)
    yearly_correlations_df = calculate_yearly_correlations(data)

    yearly_correlations_df.to_feather(produces)


def task_correlation_year_by_continent(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "yearly_continent_correlations.arrow",
):
    """Task to calculate yearly correlations between protection and provision by continent."""
    data = pd.read_pickle(merged_data)
    yearly_continent_df = calculate_yearly_continent_correlations(data)

    yearly_continent_df.to_feather(produces)


# Trends and Regional Disparities -> Function: Create a function to calculate average values of key indicators across continents.


def task_statistics_by_continent(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "continent_statistics.csv",
):
    """Task to calculate statistics by continent."""
    data = pd.read_pickle(merged_data)
    statistics = calculate_statistics_by_continent(data)

    statistics.to_csv(produces)


def task_mean_by_continent(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "continent_mean.pkl",
):
    """Task to calculate mean values by continent."""
    data = pd.read_pickle(merged_data)
    mean_values = calculate_mean_by_continent(data)

    mean_values.to_pickle(produces)  # intermediate file
