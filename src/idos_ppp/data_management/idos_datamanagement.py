import pandas as pd

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

from idos_ppp.parameters import (
    identifier_codes,
    identifier_codes_underscore,
    specific_column_mapping,
    three_p_indexes,
    countries_to_leave_out
)


def clean_year_data(raw, country_codes):
    """Clean the entire raw 3P dataset and return a cleaned DataFrame.
    Arguments: - raw pd.DataFrame - The raw DataFrame to clean.
               - country_codes list: A list of country codes to use for filtering.

    Returns:
    pd.DataFrame: A DataFrame with the cleaned data of the requested year.
    """
    _fail_if_not_dataframe(raw)
    _fail_if_empty_dataframe(raw)

    renamed_dta = _add_name_columns_countries(raw)

    updated_dta = _update_country_codes(renamed_dta, country_codes)

    filtered_dta = _filter_valid_country_codes(updated_dta, country_codes)

    # reduced_dta = _remove_countries_to_leave_out(filtered_dta)

    renamed_dta = _rename_columns_based_on_id(filtered_dta)

    selected_columns_dta = _select_relevant_columns(renamed_dta)

    selected_dta = _select_relevant_rows(selected_columns_dta, country_codes)

    cleaned_dta = _clean_missing_values(selected_dta)

    converted_dta = _convert_dtypes(cleaned_dta)

    return converted_dta


def _add_name_columns_countries(raw_dta):
    """Add 'country_name' and 'country_alpha3' as the names for the first two columns of a DataFrame."""
    country_columns_mapping = {
        "Unnamed: 0": "country_name",
        "Unnamed: 1": "country_alpha3",
    }
    renamed_dta = raw_dta.rename(columns=country_columns_mapping)
    return renamed_dta


def _update_country_codes(raw_dta, country_codes):
    """Update the content of the second column with the values from the country_codes list."""
    num_countries = len(country_codes)
    updated_dta = raw_dta
    updated_dta.iloc[:num_countries, 1] = country_codes
    return updated_dta


def _filter_valid_country_codes(raw_dta, country_codes):
    """Filter the DataFrame to include only observations with valid country codes."""
    filtered_dta = raw_dta[raw_dta.iloc[:, 1].isin(country_codes)]
    return filtered_dta


def _remove_countries_to_leave_out(raw_dta):
    """Remove observations for countries in the countries_to_leave_out list."""
    name_to_alpha3 = raw_dta.set_index('country_name')['country_alpha3'].to_dict()
    
    countries_to_leave_out_alpha3 = [name_to_alpha3[country] for country in countries_to_leave_out if country in name_to_alpha3]

    reduced_dta = raw_dta[~raw_dta['country_alpha3'].isin(countries_to_leave_out_alpha3)]

    return reduced_dta

def _rename_columns_based_on_id(raw_dta):
    """Use the identifier codes to give better names to columns, replace hyphens and spaces with underscores, and remove trailing underscores and newline characters from column names."""
    column_mapping = {}
    for col_idx, col_name in enumerate(raw_dta.columns):
        if col_idx in identifier_codes:
            code = identifier_codes[col_idx]
            if code in specific_column_mapping:
                column_mapping[col_name] = specific_column_mapping[code]
            else:
                column_mapping[col_name] = f"{code} {col_name}"
        else:
            column_mapping[col_name] = col_name

    renamed_dta = raw_dta.rename(columns=column_mapping)

    renamed_dta.columns = renamed_dta.columns.str.replace("NEW$", "", regex=True)

    renamed_dta.columns = renamed_dta.columns.str.replace(
        " - SOME NEW DATA", "", regex=False
    )

    renamed_dta.columns = renamed_dta.columns.str.replace(
        "Gov't", "Government", regex=False
    )

    renamed_dta.columns = renamed_dta.columns.str.rstrip()

    renamed_dta.columns = renamed_dta.columns.str.replace("\n", "_")

    renamed_dta.columns = renamed_dta.columns.str.replace("-", "_").str.replace(
        " ", "_"
    )

    renamed_dta.columns = renamed_dta.columns.str.lower()

    return renamed_dta


def _select_relevant_columns(raw_dta):
    """Select columns that start with "country", match any of the identifier codes, or represent the 3P indexes."""
    selected_columns = []

    for col_idx, col_name in enumerate(raw_dta.columns):
        if col_name.startswith("country") or col_name in three_p_indexes:
            selected_columns.append(col_name)
        elif col_idx in identifier_codes_underscore:
            code = identifier_codes_underscore[col_idx]
            if col_name.startswith(code):
                selected_columns.append(col_name)

    selected_dta = raw_dta[selected_columns]
    return selected_dta


def _select_relevant_rows(raw_dta, country_codes):
    """Select observations where the second column matches any of the country codes."""
    selected_dta = raw_dta[raw_dta.iloc[:, 1].isin(country_codes)]
    return selected_dta


def _clean_missing_values(raw_dta):
    """Replace "XXX" with a missing value."""
    cleaned_dta = raw_dta.replace({"XXX": pd.NA, "YYY": pd.NA})
    return cleaned_dta


def _convert_dtypes(raw_dta):
    """Convert the data types if possible, otherwise keep it as object."""
    cleaned_dta = raw_dta
    for col in cleaned_dta.columns:
        if (
            any(col.startswith(code) for code in identifier_codes_underscore.values())
            or col in three_p_indexes
        ):
            cleaned_dta[col] = cleaned_dta[col].astype(pd.Float64Dtype())
        elif col.startswith("country"):
            cleaned_dta[col] = cleaned_dta[col].astype(pd.StringDtype())

    return cleaned_dta


def clean_and_concatenate_data(raw_data_dict, country_codes):
    """Clean the dataset for each year and concatenate the results into a single DataFrame in long format.

    Arguments:
    - raw_data_dict dict: A dictionary with years as keys and raw DataFrames as values.
    - country_codes list: A list of country codes to use for filtering.
    Returns: pd.DataFrame: A concatenated DataFrame with cleaned data for all specified years.
    """
    _fail_if_invalid_country_codes(country_codes)

    cleaned_data_frames = []

    for year, raw_data in raw_data_dict.items():
        cleaned_df = clean_year_data(raw_data, country_codes)

        cleaned_df["year"] = year
        cleaned_df["year"] = cleaned_df["year"].astype(pd.Int16Dtype())

        cleaned_data_frames.append(cleaned_df)

    concatenated_df = pd.concat(cleaned_data_frames, ignore_index=False)

    concatenated_df = concatenated_df.set_index(["country_alpha3"])

    col_to_move = "year"
    cols = [col for col in concatenated_df.columns if col != col_to_move]
    cols.insert(1, col_to_move)  # Zero-based index
    reordered_df = concatenated_df[cols]

    return reordered_df


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


# Error handling functions
def _fail_if_not_dataframe(data):
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Expected a DataFrame")


def _fail_if_empty_dataframe(data):
    if data.empty:
        raise ValueError("DataFrame is empty")


def _fail_if_invalid_country_codes(country_codes):
    if not all(isinstance(code, str) for code in country_codes):
        raise TypeError("All country codes must be strings")
