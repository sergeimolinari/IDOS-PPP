import pandas as pd
import pytest

from src.idos_ppp.final.idos_plot import plot_boxplots, plot_correlation
from src.idos_ppp.parameters import three_p_indexes


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
def sample_correlation_data():
    data = {
        "year": [2007, 2010, 2013, 2016, 2019],
        "correlation": [0.1, 0.3, 0.5, 0.7, 0.9]
    }
    return pd.DataFrame(data)


@pytest.fixture
def output_dir(tmp_path):
    # temporary path
    return tmp_path


def test_boxplot(sample_data, output_dir):
    plot_boxplots(sample_data, output_dir)
    for index in three_p_indexes:
        output_file = output_dir / f"{index.capitalize()}_boxplot.png"
        assert output_file.exists()


def test_boxplot_error_handling(sample_data, output_dir):
    data_missing_year = sample_data.drop(columns=["year"])
    with pytest.raises(ValueError):
        plot_boxplots(data_missing_year, output_dir)


def test_boxplot_empty_dataframe(output_dir):
    empty_data = pd.DataFrame()
    with pytest.raises(ValueError):
        plot_boxplots(empty_data, output_dir)


def test_boxplot_missing_columns(sample_data, output_dir):
    data_missing_columns = sample_data.drop(columns=["protection"])
    with pytest.raises(ValueError):
        plot_boxplots(data_missing_columns, output_dir)


def test_plot_correlation(sample_correlation_data, output_dir):
    plot_correlation(sample_correlation_data, output_dir)
    output_file = output_dir / f"{output_dir.name}_correlation.png"
    assert output_file.exists()


def test_plot_correlation_error_handling(output_dir):
    empty_data = pd.DataFrame()
    with pytest.raises(ValueError):
        plot_correlation(empty_data, output_dir)


def test_plot_correlation_missing_columns(sample_correlation_data, output_dir):
    data_missing_columns = sample_correlation_data.drop(columns=["correlation"])
    with pytest.raises(KeyError):
        plot_correlation(data_missing_columns, output_dir)


def test_plot_correlation_highlighting(sample_correlation_data, output_dir):
    sample_correlation_data.loc[len(sample_correlation_data)] = [2022, 0.1]
    sample_correlation_data.loc[len(sample_correlation_data)] = [2023, 0.9]

    plot_correlation(sample_correlation_data, output_dir)
    output_file = output_dir / f"{output_dir.name}_correlation.png"
    assert output_file.exists()
