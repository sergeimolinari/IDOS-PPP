import pandas as pd

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

from idos_ppp.parameters import three_p_indexes

# Trends and Regional Disparities -> Function: Create a function to calculate average values of key indicators across continents.


def calculate_statistics(data):
    """Calculate the mean, median, standard deviation, range, and interval of key indicators for each year.

    Arguments: - data: pd.DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with the statistical values for each year.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    grouped_data = data.groupby(["year"])[three_p_indexes]

    statistics = grouped_data.agg(["mean", "median", "std", "min", "max"]).reset_index()

    for index in three_p_indexes:
        statistics[(index, 'range')] = statistics[(index, 'max')] - statistics[(index, 'min')]

    return statistics


def calculate_statistics_continent(data):
    """Calculate the mean, median, standard deviation, range, and interval of key indicators for each year for each continent.

    Arguments: - data: pd.DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with the statistical values for each year.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    grouped_continent_data = data.groupby(["year", "continent"])[three_p_indexes]

    statistics_by_continent = grouped_continent_data.agg(["mean", "median", "std", "min", "max"]).reset_index()

    for index in three_p_indexes:
        statistics_by_continent[(index, 'range')] = statistics_by_continent[(index, 'max')] - statistics_by_continent[(index, 'min')]

    return statistics_by_continent


# Growth -> Function: Create a function to calculate the growth ration for each year.


def calculate_growth(data):
    """Calculate the growth/degrowth of each country by dividing the value from the current year by the value from the previous year.

    Arguments: - data: pd.DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with the growth ratios for each year and variable.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    data_3p_subset = data.sort_values(by=['country_alpha3', 'year'])

    # Calculate growth ratios for each of the three columns
    data_3p_subset['protection_growth'] = data_3p_subset.groupby('country_alpha3')['protection'].pct_change() + 1
    data_3p_subset['provision_growth'] = data_3p_subset.groupby('country_alpha3')['provision'].pct_change() + 1
    data_3p_subset['participation_growth'] = data_3p_subset.groupby('country_alpha3')['participation'].pct_change() + 1

    # Create the new DataFrame with the required columns
    growth_3p_data = data_3p_subset[['country_name', 'continent', 'protection_growth', 'provision_growth', 'participation_growth']].copy()

    # Reset index to include country_alpha3 and year in the resulting DataFrame
    growth_3p_data = growth_3p_data.reset_index()

    # Filter out the first year (2007) as there is no previous year to compare with
    growth_3p_data = growth_3p_data[growth_3p_data['year'] != 2007]

    return growth_3p_data


# Error handling functions
def _fail_if_not_dataframe(data):
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Expected a DataFrame")


def _fail_if_empty_dataframe(data):
    if data.empty:
        raise ValueError("DataFrame is empty")
