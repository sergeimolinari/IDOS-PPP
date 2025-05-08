import pandas as pd

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

# Create filtered datasets for lists of countries
def process_and_save_country_list(raw, country_list):
    """
    Filter the DataFrame for a given list of countries.
    Arguments: - raw pd.DataFrame - The raw DataFrame to clean.
               - country_list: list - The list of country names to filter the DataFrame.
    
    Returns:
    pd.DataFrame: the filtered DataFrame.
    """
    _fail_if_not_dataframe(raw)
    _fail_if_empty_dataframe(raw)
    
    reset_index_df = raw.reset_index()

    filtered_df = reset_index_df[reset_index_df['country_name'].isin(country_list)]

    filtered_df = filtered_df.set_index(['country_alpha3', 'year'])

    return filtered_df


# Correlation Analysis -> Function: Create a function to calculate and visualize the correlation between protection and provision.


def calculate_yearly_correlations(data):
    """Calculate the yearly correlations between protection, which serves the purpose of measuring security, and provision, described as the socio-economic measure.

    Arguments: - data: pd.DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with the yearly correlations.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    yearly_data = data.groupby("year")[["protection", "provision"]]

    yearly_correlations = yearly_data.apply(lambda x: x.corr().iloc[0, 1])

    yearly_correlations_df = pd.DataFrame(
        {"year": yearly_correlations.index, "correlation": yearly_correlations.values}
    )

    return yearly_correlations_df


def calculate_yearly_continent_correlations(data):
    """Calculate the yearly correlation between protection and provision for each continent.

    Arguments: - data: pd.DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with the yearly correlations for each continent.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    grouped_data = data.groupby(["year", "continent"])[["protection", "provision"]]

    correlations = grouped_data.apply(lambda x: x.corr().iloc[0, 1])

    correlations_df = correlations.reset_index()
    correlations_df.columns = ["year", "continent", "correlation"]

    return correlations_df


# Error handling functions
def _fail_if_not_dataframe(data):
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Expected a DataFrame")


def _fail_if_empty_dataframe(data):
    if data.empty:
        raise ValueError("DataFrame is empty")
