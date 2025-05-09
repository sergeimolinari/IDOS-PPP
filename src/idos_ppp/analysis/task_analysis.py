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
)
from idos_ppp.config import BLD


# Correlation Analysis -> Function: Create a function to calculate and visualize the correlation between protection and provision.


def task_prot_prov_correlation_year(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "yearly_prot_prov_correlations.arrow",
):
    """Task to calculate yearly correlations between protection and provision."""
    data = pd.read_pickle(merged_data)
    yearly_correlations_df = calculate_yearly_prot_prov_correlations(data)

    yearly_correlations_df.to_feather(produces)


def task_prot_prov_correlation_year_by_continent(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "yearly_prot_prov_continent_correlations.arrow",
):
    """Task to calculate yearly correlations between protection and provision by continent."""
    data = pd.read_pickle(merged_data)
    yearly_continent_df = calculate_yearly_prot_prov_continent_correlations(data)

    yearly_continent_df.to_feather(produces)

def task_prov_part_correlation_year(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "yearly_prov_part_correlations.arrow",
):
    """Task to calculate yearly correlations between provision and participation."""
    data = pd.read_pickle(merged_data)
    yearly_correlations_df = calculate_yearly_prov_part_correlations(data)

    yearly_correlations_df.to_feather(produces)


def task_prov_part_correlation_year_by_continent(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "yearly_prov_part_continent_correlations.arrow",
):
    """Task to calculate yearly correlations between provision and participation by continent."""
    data = pd.read_pickle(merged_data)
    yearly_continent_df = calculate_yearly_prov_part_continent_correlations(data)

    yearly_continent_df.to_feather(produces)


# Trends and Regional Disparities -> Function: Create a function to calculate average values of key indicators across continents.


def task_statistics_by_continent(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "statistics.csv",
):
    """Task to calculate statistics."""
    data = pd.read_pickle(merged_data)
    statistics = calculate_statistics(data)

    statistics.to_csv(produces)


def task_mean_by_continent(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "mean.pkl",
):
    """Task to calculate mean values."""
    data = pd.read_pickle(merged_data)
    mean_values = calculate_mean(data)

    mean_values.to_pickle(produces)  # Intermediate file
