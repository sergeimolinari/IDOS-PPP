"""Tasks running the core analyses."""

import pandas as pd

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

from idos_ppp.analysis.idos_dataanalysis import (
    calculate_yearly_prot_prov_continent_correlations,
    calculate_yearly_prot_prov_correlations,
    calculate_yearly_prov_part_continent_correlations,
    calculate_yearly_prov_part_correlations
)
from idos_ppp.analysis.idos_trends import (
    calculate_statistics,
    calculate_mean,
    calculate_growth
)
from idos_ppp.config import BLD
from idos_ppp.parameters import country_lists


# Correlation Analysis -> Function: Create a function to calculate and visualize the correlation between protection and provision.


def task_prot_prov_correlation_year(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "prot_prov_correlations" / "yearly_prot_prov_correlations.arrow",
):
    """Task to calculate yearly correlations between protection and provision."""
    data = pd.read_pickle(merged_data)
    yearly_correlations_df = calculate_yearly_prot_prov_correlations(data)

    yearly_correlations_df.to_feather(produces)


def task_prot_prov_correlation_year_by_continent(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "prot_prov_correlations" / "yearly_prot_prov_continent_correlations.arrow",
):
    """Task to calculate yearly correlations between protection and provision by continent."""
    data = pd.read_pickle(merged_data)
    yearly_continent_df = calculate_yearly_prot_prov_continent_correlations(data)

    yearly_continent_df.to_feather(produces)

def task_prov_part_correlation_year(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "prov_part_correlations" / "yearly_prov_part_correlations.arrow",
):
    """Task to calculate yearly correlations between provision and participation."""
    data = pd.read_pickle(merged_data)
    yearly_correlations_df = calculate_yearly_prov_part_correlations(data)

    yearly_correlations_df.to_feather(produces)


def task_prov_part_correlation_year_by_continent(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "prov_part_correlations" / "yearly_prov_part_continent_correlations.arrow",
):
    """Task to calculate yearly correlations between provision and participation by continent."""
    data = pd.read_pickle(merged_data)
    yearly_continent_df = calculate_yearly_prov_part_continent_correlations(data)

    yearly_continent_df.to_feather(produces)


# Trends and Regional Disparities -> Function: Create a function to calculate average values of key indicators across continents.


def task_statistics_by_continent(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "statistical analysis" / "statistics.arrow",
):
    """Task to calculate statistics."""
    data = pd.read_pickle(merged_data)
    statistics = calculate_statistics(data)

    statistics.to_feather(produces)


def task_mean_by_continent(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "statistical analysis" / "mean.pkl",
):
    """Task to calculate mean values."""
    data = pd.read_pickle(merged_data)
    mean_values = calculate_mean(data)

    mean_values.to_pickle(produces)

# Growth -> Function: Create a function to calculate the growth ration for each year.


inputs_growth = {list_name: BLD / "data" / "subsets" / f"{list_name}_data.pkl" for list_name in country_lists.keys()}
products_growth = {list_name: BLD / "analysis" / "subsets_growth" / f"{list_name}_growth_data.pkl" for list_name in country_lists.keys()}

def task_growth(
    merged_data=inputs_growth,
    produces=products_growth,
):
    """Task to calculate growth ratios."""
    for list_name, data in merged_data.items():
        data = pd.read_pickle(data)
        growth_data = calculate_growth(data)
        output_pkl_file_path = BLD / "analysis" / "subsets_growth" / f"{list_name}_growth_data.pkl"
        growth_data.to_pickle(output_pkl_file_path) # Save the filtered DataFrames as PKL files

# Recall: PKL for intermediate files (want to use them later for data visualization), FEATHER for final files (independent stat analysis)
