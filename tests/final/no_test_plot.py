import pandas as pd
import pytest

from src.idos_ppp.final.idos_plot import plot_mean_trends
from src.idos_ppp.parameters import three_p_indexes


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


@pytest.fixture
def output_dir(tmp_path):
    # temporary path
    return tmp_path


def test_plot_mean_trends(sample_data, output_dir):
    plot_mean_trends(sample_data, output_dir)
    for index in three_p_indexes:
        output_file = output_dir / f"{index}_mean_trend.png"
        assert output_file.exists()


def test_plot_mean_trends_error_handling(sample_data, output_dir):
    data_missing_year = sample_data.drop(columns=["year"])
    with pytest.raises(ValueError):
        plot_mean_trends(data_missing_year, output_dir)
