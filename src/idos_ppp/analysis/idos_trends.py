import pandas as pd

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

from idos_ppp.parameters import three_p_indexes

# Trends and Regional Disparities -> Function: Create a function to calculate average values of key indicators across continents.


def calculate_statistics_by_continent(data):
    """Calculate the mean, median, and standard deviation of key indicators across continents for each year, in order to understand regional disparities.

    Arguments: - data: pd.DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with the three statistical values for each year and continent.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    grouped_data = data.groupby(["year", "continent"])[three_p_indexes]

    statistics = grouped_data.agg(["mean", "median", "std"]).reset_index()

    return statistics


def calculate_mean_by_continent(data):
    """Calculate and save the mean of key indicators across continents for each year.

    Arguments: - data: pd.DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with the mean for each year and continent.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    grouped_data = data.groupby(["year", "continent"])[three_p_indexes]

    mean_values = grouped_data.mean().reset_index()

    return mean_values


# Error handling functions
def _fail_if_not_dataframe(data):
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Expected a DataFrame")


def _fail_if_empty_dataframe(data):
    if data.empty:
        raise ValueError("DataFrame is empty")
