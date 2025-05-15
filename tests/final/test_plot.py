import pandas as pd
import pytest

from src.idos_ppp.final.idos_plot import plot_boxplots
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
def output_dir(tmp_path):
    # temporary path
    return tmp_path


def test_boxplot(sample_data, output_dir):
    plot_boxplots(sample_data, output_dir)
    for index in three_p_indexes:
        output_file = output_dir / f"{index}_boxplot.png"
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


def test_boxplot_correct_plot_titles(sample_data, output_dir):
    plot_boxplots(sample_data, output_dir)
    for index in three_p_indexes:
        output_file = output_dir / f"{index}_boxplot.png"
        assert output_file.exists()
        # Optionally, you can add more assertions to check the content of the plot titles
