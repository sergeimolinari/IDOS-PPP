import pandas as pd
import pytest

from src.idos_ppp.analysis.idos_dataanalysis import (
    calculate_yearly_prot_part_continent_correlations,
    calculate_yearly_prot_part_correlations,
    calculate_yearly_prot_prov_continent_correlations,
    calculate_yearly_prot_prov_correlations,
    calculate_yearly_prov_part_continent_correlations,
    calculate_yearly_prov_part_correlations,
)


@pytest.fixture
def sample_data():
    data = {
        "year": [2020, 2020, 2021, 2021],
        "continent": ["Africa", "Asia", "Africa", "Asia"],
        "protection": [1.5, 2.5, 3.5, 4.5],
        "provision": [2.0, 3.0, 4.0, 5.0],
        "participation": [1.0, 2.0, 3.0, 4.0],
    }
    return pd.DataFrame(data)


def test_calculate_prot_prov_yearly_correlations_expected_columns(sample_data):
    result = calculate_yearly_prot_prov_correlations(sample_data)
    assert "year" in result.columns
    assert "correlation" in result.columns
    assert "p_value" in result.columns
    assert not result.empty


def test_calculate_prot_prov_yearly_continent_correlations_expected_columns(
    sample_data,
):
    result = calculate_yearly_prot_prov_continent_correlations(sample_data)
    assert "year" in result.columns
    assert "continent" in result.columns
    assert "correlation" in result.columns
    assert "p_value" in result.columns
    assert not result.empty


def test_calculate_prov_part_yearly_correlations_expected_columns(sample_data):
    result = calculate_yearly_prov_part_correlations(sample_data)
    assert "year" in result.columns
    assert "correlation" in result.columns
    assert "p_value" in result.columns
    assert not result.empty


def test_calculate_prov_part_yearly_continent_correlations_expected_columns(
    sample_data,
):
    result = calculate_yearly_prov_part_continent_correlations(sample_data)
    assert "year" in result.columns
    assert "continent" in result.columns
    assert "correlation" in result.columns
    assert "p_value" in result.columns
    assert not result.empty


def test_calculate_prov_part_yearly_correlations_error_handling(sample_data):
    data_missing_year = sample_data.drop(columns=["year"])
    with pytest.raises(KeyError):
        calculate_yearly_prov_part_correlations(data_missing_year)


def test_calculate_prov_part_yearly_continent_correlations_error_handling(sample_data):
    data_missing_continent = sample_data.drop(columns=["continent"])
    with pytest.raises(KeyError):
        calculate_yearly_prov_part_continent_correlations(data_missing_continent)


def test_calculate_prot_prov_yearly_correlations_error_handling(sample_data):
    data_missing_year = sample_data.drop(columns=["year"])
    with pytest.raises(KeyError):
        calculate_yearly_prot_prov_correlations(data_missing_year)


def test_calculate_prot_prov_yearly_continent_correlations_error_handling(sample_data):
    data_missing_continent = sample_data.drop(columns=["continent"])
    with pytest.raises(KeyError):
        calculate_yearly_prot_prov_continent_correlations(data_missing_continent)


def test_calculate_prot_part_yearly_correlations_expected_columns(sample_data):
    result = calculate_yearly_prot_part_correlations(sample_data)
    assert "year" in result.columns
    assert "correlation" in result.columns
    assert "p_value" in result.columns
    assert not result.empty


def test_calculate_prot_part_yearly_continent_correlations_expected_columns(
    sample_data,
):
    result = calculate_yearly_prot_part_continent_correlations(sample_data)
    assert "year" in result.columns
    assert "continent" in result.columns
    assert "correlation" in result.columns
    assert "p_value" in result.columns
    assert not result.empty


def test_calculate_prot_part_yearly_correlations_error_handling(sample_data):
    data_missing_year = sample_data.drop(columns=["year"])
    with pytest.raises(KeyError):
        calculate_yearly_prot_part_correlations(data_missing_year)


def test_calculate_prot_part_yearly_continent_correlations_error_handling(sample_data):
    data_missing_continent = sample_data.drop(columns=["continent"])
    with pytest.raises(KeyError):
        calculate_yearly_prot_part_continent_correlations(data_missing_continent)
