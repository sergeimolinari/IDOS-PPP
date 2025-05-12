import pandas as pd
import pytest

from src.idos_ppp.analysis.idos_trends import (
    calculate_statistics,
    calculate_statistics_continent,
    calculate_growth
)


@pytest.fixture
def sample_data():
    data = {
        "year": [2020, 2020, 2021, 2021],
        "continent": ["Africa", "Asia", "Africa", "Asia"],
        "country_alpha3": ['ITA', 'CHN', 'DEU', 'IND'],
        "country_name": ['Italy', 'China', 'Germany', 'India'],
        "protection": [1.5, 2.5, 3.5, 4.5],
        "provision": [2.0, 3.0, 4.0, 5.0],
        "participation": [1.0, 2.0, 3.0, 4.0],
    }
    return pd.DataFrame(data)

@pytest.fixture
def sample_data_growth():
    data = {
        "year": [2020, 2020, 2021, 2021],
        "continent": ["Africa", "Asia", "Africa", "Asia"],
        "country_alpha3": ['ITA', 'CHN', 'DEU', 'IND'],
        "country_name": ['Italy', 'China', 'Germany', 'India'],
        "protection": [1.5, 2.5, 3.5, 4.5],
        "provision": [2.0, 3.0, 4.0, 5.0],
        "participation": [1.0, 2.0, 3.0, 4.0],
    }
    sample_data_growth = pd.DataFrame(data).set_index(["country_alpha3", "year"])
    return sample_data_growth


def test_calculate_statistics(sample_data):
    result = calculate_statistics(sample_data)
    assert ("protection", "mean") in result.columns
    assert ("provision", "mean") in result.columns
    assert ("participation", "mean") in result.columns
    assert ("protection", "median") in result.columns
    assert ("protection", "std") in result.columns
    assert ("protection", "min") in result.columns
    assert ("protection", "max") in result.columns
    assert ("protection", "range") in result.columns
    assert ("provision", "median") in result.columns
    assert ("provision", "std") in result.columns
    assert ("provision", "min") in result.columns
    assert ("provision", "max") in result.columns
    assert ("provision", "range") in result.columns
    assert ("participation", "median") in result.columns
    assert ("participation", "std") in result.columns
    assert ("participation", "min") in result.columns
    assert ("participation", "max") in result.columns
    assert ("participation", "range") in result.columns
    assert not result.empty


def test_calculate_statistics_continent(sample_data):
    result = calculate_statistics_continent(sample_data)
    assert "year" in result.columns
    assert ("protection", "mean") in result.columns
    assert ("provision", "mean") in result.columns
    assert ("participation", "mean") in result.columns
    assert ("protection", "median") in result.columns
    assert ("protection", "std") in result.columns
    assert ("protection", "min") in result.columns
    assert ("protection", "max") in result.columns
    assert ("protection", "range") in result.columns
    assert ("provision", "median") in result.columns
    assert ("provision", "std") in result.columns
    assert ("provision", "min") in result.columns
    assert ("provision", "max") in result.columns
    assert ("provision", "range") in result.columns
    assert ("participation", "median") in result.columns
    assert ("participation", "std") in result.columns
    assert ("participation", "min") in result.columns
    assert ("participation", "max") in result.columns
    assert ("participation", "range") in result.columns
    assert not result.empty


def test_calculate_growth(sample_data_growth):
    result = calculate_growth(sample_data_growth)
    assert "year" in result.columns
    assert "country_alpha3" in result.columns
    assert "continent" in result.columns
    assert "protection_growth" in result.columns
    assert "provision_growth" in result.columns
    assert "participation_growth" in result.columns
    assert not result.empty


def test_calculate_statistics_error_handling(sample_data):
    data_missing_year = sample_data.drop(columns=["year"])
    with pytest.raises(KeyError):
        calculate_statistics(data_missing_year)


def test_calculate_mean_error_handling(sample_data):
    data_missing_year = sample_data.drop(columns=["year"])
    with pytest.raises(KeyError):
        calculate_statistics(data_missing_year)
