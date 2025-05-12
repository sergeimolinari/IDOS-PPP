"""Tasks for managing the data."""

import zipfile

import pandas as pd

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

from idos_ppp.config import BLD, DATA
from idos_ppp.data_management.idos_datamanagement import (
    clean_and_concatenate_data,
    process_and_save_country_list,
)
from idos_ppp.parameters import country_lists, missing_countries, sheet_names, years

products_unzip = {
    "continents data": BLD
    / "data"
    / "data_continents"
    / "continents-according-to-our-world-in-data.csv",
    "continents json": BLD
    / "data"
    / "data_continents"
    / "continents-according-to-our-world-in-data.metadata.json",
    "continents data readme": BLD / "data" / "data_continents" / "readme.md",
}


def task_unzip_file(
    zip_file=DATA / "continents-according-to-our-world-in-data.filtered.zip",
    produces=products_unzip,
):
    output_dir = BLD / "data" / "data_continents"

    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(output_dir)


def task_clean_and_concatenate(
    raw_data=DATA / "Data_2007_2010_2013_2016_2019.xlsx",
    produces=BLD / "data" / "clean_data.csv",
):
    raw = {
        year: pd.read_excel(raw_data, sheet_name=sheet, header=1)
        for year, sheet in zip(years, sheet_names, strict=False)
    }
    countries_list = pd.read_excel(raw_data, sheet_name="3-2", header=0)
    clean_data = clean_and_concatenate_data(
        raw_data_dict=raw,
        country_codes=countries_list.iloc[0:, 1].tolist(),
    )
    clean_data.to_csv(produces)


def task_merge_data(
    clean_data=BLD / "data" / "clean_data.csv",
    continent_data=BLD
    / "data"
    / "data_continents"
    / "continents-according-to-our-world-in-data.csv",
    produces=BLD / "data" / "merged_data.pkl",
):
    df1 = pd.read_csv(clean_data)
    continent_df = pd.read_csv(continent_data)

    df2 = continent_df.drop(columns=["Entity", "Year", "time"])
    country_codes = df1.reset_index()["country_alpha3"][:154,].tolist()
    df2 = df2[df2["Code"].isin(country_codes)]
    df2 = df2.rename(
        columns={
            "Code": "country_alpha3",
            "World regions according to OWID": "continent",
        },
    )
    df2 = pd.concat([df2, missing_countries], ignore_index=True)
    df2["country_alpha3"] = df2["country_alpha3"].astype(pd.StringDtype())
    df2["continent"] = df2["continent"].astype(pd.CategoricalDtype())

    # Check that there are no overlaps in column names between the two datasets
    cols_df1 = set(df1.columns)
    cols_df2 = set(df2.columns)
    overlapping_cols = cols_df1.intersection(cols_df2)
    if len(overlapping_cols) == 0:
        print("No overlapping columns.")
    else:
        print(f"Overlapping columns: {overlapping_cols}")

    merged_df = pd.merge(df1, df2, on="country_alpha3", how="left")

    col_to_move = "continent"
    cols = [col for col in merged_df.columns if col != col_to_move]
    cols.insert(2, col_to_move)  # Zero-based index
    merged_df = merged_df[cols]

    merged_data_indexed = merged_df.set_index(["country_alpha3", "year"])

    merged_data_indexed.to_pickle(produces)


products = {
    list_name: BLD / "data" / "subsets" / f"{list_name}_data.pkl"
    for list_name in country_lists.keys()
}


def task_process_and_save_country_list(
    merged_data=BLD / "data" / "merged_data.pkl",
    produces=products,
):
    """Task to create datasets constrained to countries in specified lists."""
    data = pd.read_pickle(merged_data)
    for list_name, country_list in country_lists.items():
        filtered_data = process_and_save_country_list(data, country_list)
        output_pkl_file_path = BLD / "data" / "subsets" / f"{list_name}_data.pkl"
        filtered_data.to_pickle(output_pkl_file_path)
