from pathlib import Path

import idos_datamanagement
import pandas as pd

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

from idos_ppp.parameters import missing_countries

if __name__ == "__main__":
    this_file = Path(__file__)
    bld_file = this_file.parent / "continents-according-to-our-world-in-data.filtered"
    # Load the raw dataset:
    raw_data_path = bld_file.parent / "Data_2007_2010_2013_2016_2019.xlsx"
    raw_data_2007 = pd.read_excel(
        raw_data_path, sheet_name="Transformed 2007", header=1
    )
    raw_data_2010 = pd.read_excel(
        raw_data_path, sheet_name="Transformed 2010", header=1
    )
    raw_data_2013 = pd.read_excel(
        raw_data_path, sheet_name="Transformed 2013", header=1
    )
    raw_data_2016 = pd.read_excel(
        raw_data_path, sheet_name="Transformed 2016", header=1
    )
    raw_data_2019 = pd.read_excel(
        raw_data_path, sheet_name="Transformed 2019 new", header=1
    )

    # Load the country codes
    countries_list = pd.read_excel(raw_data_path, sheet_name="3-2", header=0)
    # country_names = countries_list.iloc[0:, 0].tolist()  # First column, starting from the second row
    country_codes = countries_list.iloc[
        0:, 1
    ].tolist()  # Second column, starting from the second row

    # Load the reference years
    raw_data_dict = {
        2007: raw_data_2007,
        2010: raw_data_2010,
        2013: raw_data_2013,
        2016: raw_data_2016,
        2019: raw_data_2019,
    }

    # Clean the dataset
    cleaned_and_concatenated_df = idos_datamanagement.clean_and_concatenate_data(
        raw_data_dict=raw_data_dict, country_codes=country_codes
    )

    # Read continent data
    continent_file_path = bld_file / "continents-according-to-our-world-in-data.csv"
    continent_data = pd.read_csv(continent_file_path)

    # Drop unnecessary columns
    continent_df = continent_data.drop(columns=["Entity", "Year", "time"])
    # Filter the DataFrame to include only the countries in your list
    continent_df = continent_df[continent_df["Code"].isin(country_codes)]
    # Rename the 'Code' column to 'country_alpha3' to match your main DataFrame
    continent_df = continent_df.rename(
        columns={
            "Code": "country_alpha3",
            "World regions according to OWID": "continent",
        }
    )
    # missing_country_codes = set(country_codes) - set(continent_df['country_alpha3'])

    # Append the missing countries to the filtered DataFrame
    continent_df = pd.concat([continent_df, missing_countries], ignore_index=True)

    # Change dtypes
    continent_df["country_alpha3"] = continent_df["country_alpha3"].astype(
        pd.StringDtype()
    )
    continent_df["continent"] = continent_df["continent"].astype(pd.CategoricalDtype())

    # First we check that there are no overlaps in column names between the two datasets:
    cols_df1 = set(cleaned_and_concatenated_df.columns)
    cols_df2 = set(continent_df.columns)
    overlapping_cols = cols_df1.intersection(cols_df2)
    if len(overlapping_cols) == 0:
        print("No overlapping columns.")
    else:
        print(f"Overlapping columns: {overlapping_cols}")

    # Assuming clean_and_concatenate_df is your main DataFrame
    merged_df = pd.merge(
        cleaned_and_concatenated_df, continent_df, on="country_alpha3", how="left"
    )

    # Move "continent" to the third position
    col_to_move = "continent"
    cols = [col for col in merged_df.columns if col != col_to_move]
    cols.insert(2, col_to_move)  # Zero-based index
    merged_df = merged_df[cols]

    # Set the index to 'country_alpha3' and 'year'
    merged_indexed_df = merged_df.set_index(["country_alpha3", "year"])

    # Final testing
    # print(merged_df)
    # print(merged_indexed_df)
    # print(merged_df[["country_name", "continent", "protection", "provision", "participation"]])

    # We save and check if it created merged df
    merged_df_pickle_path = bld_file.parent / "merged_idos3p_data.pkl"
    merged_df.to_pickle(merged_df_pickle_path)
    # merged_df_csv_path = bld_file.parent / "merged_idos3p_data.csv"
    # merged_df.to_csv(merged_df_csv_path)
    merged_indexed_df_pickle_path = bld_file.parent / "merged_indexed_idos3p_data.pkl"
    merged_indexed_df.to_pickle(merged_indexed_df_pickle_path)
    # merged_indexed_df_csv_path = bld_file.parent / "merged_indexed_idos3p_data.csv"
    # merged_indexed_df.to_csv(merged_indexed_df_csv_path)
    # print(merged_df.describe())
    # print(merged_indexed_df.index.unique())
