import pandas as pd
import pytest

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

from src.idos_ppp.data_management.idos_datamanagement import (
    _add_name_columns_countries,
    _clean_missing_values,
    _filter_valid_country_codes,
    _rename_columns_based_on_id,
    _select_relevant_columns,
    _select_relevant_rows,
    _update_country_codes,
    clean_and_concatenate_data,
    clean_year_data,
)


@pytest.fixture
def sample_raw_data():
    data = {
        "Unnamed: 0": ["Country1", "Country2"],
        "Unnamed: 1": ["ABC", "DEF"],
        "Indicator1": [1.5, 2.5],
        "Indicator2": ["XXX", 3.5],
    }
    return pd.DataFrame(data)


@pytest.fixture
def country_codes():
    return ["ABC", "DEF"]


def test_add_name_columns_countries(sample_raw_data):
    result = _add_name_columns_countries(sample_raw_data)
    assert "country_name" in result.columns
    assert "country_alpha3" in result.columns


def test_update_country_codes(sample_raw_data, country_codes):
    result = _update_country_codes(sample_raw_data, country_codes)
    assert result.iloc[0, 1] == "ABC"
    assert result.iloc[1, 1] == "DEF"


def test_filter_valid_country_codes(sample_raw_data, country_codes):
    result = _filter_valid_country_codes(sample_raw_data, country_codes)
    assert result.shape[0] == 2


def test_rename_columns_based_on_id(sample_raw_data):
    result = _rename_columns_based_on_id(sample_raw_data)
    assert "1_1_indicator1" in result.columns
    assert "1_2_ucdp" in result.columns


def test_select_relevant_columns(sample_raw_data):
    sample_raw_data.columns = [
        "country_name",
        "country_alpha3",
        "1_1_indicator1",
        "1_2_ucdp",
    ]
    result = _select_relevant_columns(sample_raw_data)
    assert "country_name" in result.columns
    assert "1_1_indicator1" in result.columns


def test_select_relevant_rows(sample_raw_data, country_codes):
    result = _select_relevant_rows(sample_raw_data, country_codes)
    assert result.shape[0] == 2


def test_clean_missing_values(sample_raw_data):
    result = _clean_missing_values(sample_raw_data)
    assert pd.isna(result["Indicator2"][0])


def test_clean_year_data(sample_raw_data, country_codes):
    result = clean_year_data(sample_raw_data, country_codes)
    assert "country_name" in result.columns
    assert "1_1_indicator1" in result.columns
    assert result["1_1_indicator1"].dtype == pd.Float64Dtype()


def test_clean_and_concatenate_data(sample_raw_data, country_codes):
    raw_data_dict = {2020: sample_raw_data, 2021: sample_raw_data}
    result = clean_and_concatenate_data(raw_data_dict, country_codes)
    assert "year" in result.columns
    assert result.index.name == "country_alpha3"
