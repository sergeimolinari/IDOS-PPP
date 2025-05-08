import pandas as pd

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

from idos_ppp.parameters import three_p_indexes

# Trends and Regional Disparities -> Function: Create a function to calculate average values of key indicators across continents.


def calculate_statistics(data):
    """Calculate the mean, median, and standard deviation of key indicators for each year.

    Arguments: - data: pd.DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with the three statistical values for each year and continent.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    grouped_data = data.groupby(["year"])[three_p_indexes]

    statistics = grouped_data.agg(["mean", "median", "std"]).reset_index()

    return statistics


def calculate_mean(data):
    """Calculate and save the mean of key indicators across continents for each year.

    Arguments: - data: pd.DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with the mean for each year and continent.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    grouped_data = data.groupby(["year"])[three_p_indexes]

    mean_values = grouped_data.mean().reset_index()

    return mean_values


# Growth -> Function: Create a function to calculate the growth ration for each year.

'''
def calculate_growth(data):
    """Calculate the growth/degrowth of each country by dividing the value from the current year by the value from the previous year.

    Arguments: - data: pd.DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with the growth ratios for each year and variable.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)
'''

# Error handling functions
def _fail_if_not_dataframe(data):
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Expected a DataFrame")


def _fail_if_empty_dataframe(data):
    if data.empty:
        raise ValueError("DataFrame is empty")
