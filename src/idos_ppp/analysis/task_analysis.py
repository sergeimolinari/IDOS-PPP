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

inputs_analysis = {list_name: BLD / "data" / "subsets" / f"{list_name}_data.pkl" for list_name in country_lists.keys()}
inputs_analysis['merged_dataframe'] = BLD / "data" / "merged_data.pkl"


# Correlation Analysis -> Function: Create a function to calculate and visualize the correlation between protection and provision.


products_prot_prov_corr = {list_name: BLD / "analysis" / "prot_prov_correlations" / f"{list_name}_yearly_prot_prov_correlations.pkl" for list_name in country_lists.keys()}

def task_prot_prov_correlation_year(
    merged_data=inputs_analysis,
    produces=products_prot_prov_corr,
):
    """Task to calculate yearly correlations between protection and provision."""
    for list_name, data in merged_data.items():
        data = pd.read_pickle(data)
        yearly_prot_prov_correlations_data = calculate_yearly_prot_prov_correlations(data)
        output_pkl_file_path = BLD / "analysis" / "prot_prov_correlations" / f"{list_name}_yearly_prot_prov_correlations.pkl"
        yearly_prot_prov_correlations_data.to_pickle(output_pkl_file_path)


def task_prot_prov_correlation_year_by_continent(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "prot_prov_correlations" / "yearly_prot_prov_continent_correlations.pkl",
):
    """Task to calculate yearly correlations between protection and provision by continent."""
    data = pd.read_pickle(merged_data)
    yearly_continent_df = calculate_yearly_prot_prov_continent_correlations(data)

    yearly_continent_df.to_pickle(produces)


products_prov_part_corr = {list_name: BLD / "analysis" / "prov_part_correlations" / f"{list_name}_yearly_prov_part_correlations.pkl" for list_name in country_lists.keys()}

def task_prov_part_correlation_year(
    merged_data=inputs_analysis,
    produces=products_prov_part_corr,
):
    """Task to calculate yearly correlations between provision and participation."""
    for list_name, data in merged_data.items():
        data = pd.read_pickle(data)
        yearly_prov_part_correlations_data = calculate_yearly_prov_part_correlations(data)
        output_pkl_file_path = BLD / "analysis" / "prov_part_correlations" / f"{list_name}_yearly_prov_part_correlations.pkl"
        yearly_prov_part_correlations_data.to_pickle(output_pkl_file_path)


def task_prov_part_correlation_year_by_continent(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=BLD / "analysis" / "prov_part_correlations" / "yearly_prov_part_continent_correlations.pkl",
):
    """Task to calculate yearly correlations between provision and participation by continent."""
    data = pd.read_pickle(merged_data)
    yearly_continent_df = calculate_yearly_prov_part_continent_correlations(data)

    yearly_continent_df.to_pickle(produces)


# Trends and Regional Disparities -> Function: Create functions to calculate statistical measure and average values of key indicators.


products_statistical_analysis = {list_name: BLD / "analysis" / "statistical_analysis" / "stats_to_feather" / f"{list_name}_yearly_statistics.arrow" for list_name in country_lists.keys()}

def task_statistical_analysis(
    merged_data=inputs_analysis,
    produces=products_statistical_analysis,
):
    """Task to calculate statistics."""
    for list_name, data in merged_data.items():
        data = pd.read_pickle(data)
        yearly_statistics = calculate_statistics(data)
        output_pkl_file_path = BLD / "analysis" / "statistical_analysis" / "stats_to_feather" / f"{list_name}_yearly_statistics.arrow"
        yearly_statistics.to_feather(output_pkl_file_path)


products_yearly_means = {list_name: BLD / "analysis" / "statistical_analysis" / "means" / f"{list_name}_yearly_3p_mean.pkl" for list_name in country_lists.keys()}

def task_mean_3p_indexes(
    merged_data=inputs_analysis,
    produces=products_yearly_means,
):
    """Task to calculate mean values for plotting."""
    for list_name, data in merged_data.items():
        data = pd.read_pickle(data)
        mean_values = calculate_mean(data)
        output_pkl_file_path = BLD / "analysis" / "statistical_analysis" / "means" / f"{list_name}_yearly_3p_mean.pkl"
        mean_values.to_pickle(output_pkl_file_path)


# Growth -> Function: Create a function to calculate the growth ration for each year.


products_growth = {list_name: BLD / "analysis" / "growth" / f"{list_name}_growth_data.pkl" for list_name in country_lists.keys()}

def task_growth(
    merged_data=inputs_analysis,
    produces=products_growth,
):
    """Task to calculate growth ratios."""
    for list_name, data in merged_data.items():
        data = pd.read_pickle(data)
        growth_data = calculate_growth(data)
        output_pkl_file_path = BLD / "analysis" / "growth" / f"{list_name}_growth_data.pkl"
        growth_data.to_pickle(output_pkl_file_path)

# Recall: PKL for intermediate files (want to use them later for data visualization), FEATHER for final files (independent stat analysis)
