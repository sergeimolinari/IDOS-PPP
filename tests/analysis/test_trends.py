import pandas as pd
import pytest

from src.idos_ppp.analysis.idos_trends import (
    calculate_mean_by_continent,
    calculate_statistics_by_continent,
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


def test_calculate_statistics_by_continent_expected_columns_mean(sample_data):
    result = calculate_statistics_by_continent(sample_data)
    assert ("protection", "mean") in result.columns
    assert ("provision", "mean") in result.columns
    assert ("participation", "mean") in result.columns
    assert not result.empty


def test_calculate_mean_by_continent(sample_data):
    result = calculate_mean_by_continent(sample_data)
    assert "year" in result.columns
    assert "continent" in result.columns
    assert not result.empty


def test_calculate_statistics_by_continent_error_handling(sample_data):
    data_missing_year = sample_data.drop(columns=["year"])
    with pytest.raises(KeyError):
        calculate_statistics_by_continent(data_missing_year)


def test_calculate_mean_by_continent_error_handling(sample_data):
    data_missing_continent = sample_data.drop(columns=["continent"])
    with pytest.raises(KeyError):
        calculate_mean_by_continent(data_missing_continent)
