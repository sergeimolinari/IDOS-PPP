import numpy as np
import pandas as pd
from scipy.stats import pearsonr

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

# Correlation Analysis -> Function: Create a function to calculate and visualize the correlation between protection and provision.


def calculate_yearly_prot_prov_correlations(data):
    """Calculate the yearly correlations between protection, which serves the purpose of measuring security, and provision, described as the socioeconomic measure.

    Arguments: - data: pd.DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with the yearly correlations.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    yearly_data = data.groupby("year")[["protection", "provision"]]

    def calculate_correlation_and_p_value(group):
        if len(group["protection"]) < 2 or len(group["provision"]) < 2:
            return pd.Series({"correlation": np.nan, "p_value": np.nan})
        correlation, p_value = pearsonr(group["protection"], group["provision"])
        return pd.Series({"correlation": correlation, "p_value": p_value})

    # This function from the scipy.stats module calculates the Pearson correlation coefficient and the p-value for testing the null hypothesis that the correlation is zero.
    # The p-value represents the probability of observing the data, or something more extreme, assuming that the null hypothesis is true (H0: corr = 0).
    # A p-value less than 0.1 indicates that there is less than a 10% chance of observing the data, or something more extreme, if the null hypothesis is true.
    # In other words, there is a relatively low probability that the observed correlation is due to random chance.

    yearly_correlations = yearly_data.apply(calculate_correlation_and_p_value)

    yearly_correlations_df = yearly_correlations.reset_index()
    yearly_correlations_df.columns = ["year", "correlation", "p_value"]

    return yearly_correlations_df


def calculate_yearly_prot_prov_continent_correlations(data):
    """Calculate the yearly correlation between protection and provision for each continent.

    Arguments: - data: pd.DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with the yearly correlations for each continent.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    grouped_data = data.groupby(["year", "continent"])[["protection", "provision"]]

    def calculate_correlation_and_p_value(group):
        if len(group["protection"]) < 2 or len(group["provision"]) < 2:
            return pd.Series({"correlation": np.nan, "p_value": np.nan})
        correlation, p_value = pearsonr(group["protection"], group["provision"])
        return pd.Series({"correlation": correlation, "p_value": p_value})

    correlations = grouped_data.apply(calculate_correlation_and_p_value)

    correlations_df = correlations.reset_index()
    correlations_df.columns = ["year", "continent", "correlation", "p_value"]

    return correlations_df


# Correlation Analysis -> Function: Create a function to calculate and visualize the correlation between provision and participation.


def calculate_yearly_prov_part_correlations(data):
    """Calculate the yearly correlations between provision, described as the socioeconomic measure, and (political) participation (3-1 is the Electoral Democracy Index and 3-2 is Voice and Accountability ).

    Arguments: - data: pd.DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with the yearly correlations.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    yearly_data = data.groupby("year")[["provision", "participation"]]

    def calculate_correlation_and_p_value(group):
        if len(group["participation"]) < 2 or len(group["provision"]) < 2:
            return pd.Series({"correlation": np.nan, "p_value": np.nan})
        correlation, p_value = pearsonr(group["provision"], group["participation"])
        return pd.Series({"correlation": correlation, "p_value": p_value})

    # This function from the scipy.stats module calculates the Pearson correlation coefficient and the p-value for testing the null hypothesis that the correlation is zero.

    yearly_correlations = yearly_data.apply(calculate_correlation_and_p_value)

    yearly_correlations_df = yearly_correlations.reset_index()
    yearly_correlations_df.columns = ["year", "correlation", "p_value"]

    return yearly_correlations_df


def calculate_yearly_prov_part_continent_correlations(data):
    """Calculate the yearly correlation between provision and participation for each continent.

    Arguments: - data: pd.DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with the yearly correlations for each continent.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    grouped_data = data.groupby(["year", "continent"])[["provision", "participation"]]

    def calculate_correlation_and_p_value(group):
        if len(group["provision"]) < 2 or len(group["participation"]) < 2:
            return pd.Series({"correlation": np.nan, "p_value": np.nan})
        correlation, p_value = pearsonr(group["provision"], group["participation"])
        return pd.Series({"correlation": correlation, "p_value": p_value})

    correlations = grouped_data.apply(calculate_correlation_and_p_value)

    correlations_df = correlations.reset_index()
    correlations_df.columns = ["year", "continent", "correlation", "p_value"]

    return correlations_df


# Correlation Analysis -> Function: Create a function to calculate and visualize the correlation between protection and participation.


def calculate_yearly_prot_part_correlations(data):
    """Calculate the yearly correlations between protection, which serves the purpose of measuring security, and and (political) participation (3-1 is the Electoral Democracy Index and 3-2 is Voice and Accountability ).

    Arguments: - data: pd.DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with the yearly correlations.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    yearly_data = data.groupby("year")[["protection", "participation"]]

    def calculate_correlation_and_p_value(group):
        if len(group["protection"]) < 2 or len(group["participation"]) < 2:
            return pd.Series({"correlation": np.nan, "p_value": np.nan})
        correlation, p_value = pearsonr(group["protection"], group["participation"])
        return pd.Series({"correlation": correlation, "p_value": p_value})

    # This function from the scipy.stats module calculates the Pearson correlation coefficient and the p-value for testing the null hypothesis that the correlation is zero.

    yearly_correlations = yearly_data.apply(calculate_correlation_and_p_value)

    yearly_correlations_df = yearly_correlations.reset_index()
    yearly_correlations_df.columns = ["year", "correlation", "p_value"]

    return yearly_correlations_df


def calculate_yearly_prot_part_continent_correlations(data):
    """Calculate the yearly correlation between protection and provision for each continent.

    Arguments: - data: pd.DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with the yearly correlations for each continent.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    grouped_data = data.groupby(["year", "continent"])[["protection", "participation"]]

    def calculate_correlation_and_p_value(group):
        if len(group["protection"]) < 2 or len(group["participation"]) < 2:
            return pd.Series({"correlation": np.nan, "p_value": np.nan})
        correlation, p_value = pearsonr(group["protection"], group["participation"])
        return pd.Series({"correlation": correlation, "p_value": p_value})

    correlations = grouped_data.apply(calculate_correlation_and_p_value)

    correlations_df = correlations.reset_index()
    correlations_df.columns = ["year", "continent", "correlation", "p_value"]

    return correlations_df


# Error handling functions
def _fail_if_not_dataframe(data):
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Expected a DataFrame")


def _fail_if_empty_dataframe(data):
    if data.empty:
        raise ValueError("DataFrame is empty")
