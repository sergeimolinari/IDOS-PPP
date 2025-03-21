"""Task running the results formatting (plots of trend by 3p index)."""

import pandas as pd

from idos_ppp.config import BLD
from idos_ppp.final.idos_plot import plot_mean_trends

products = [
    BLD / "final" / "trend_plots" / "protection_mean_trend.png",
    BLD / "final" / "trend_plots" / "provision_mean_trend.png",
    BLD / "final" / "trend_plots" / "participation_mean_trend.png",
]


def task_plot_trends(
    mean_values=BLD / "analysis" / "continent_mean.pkl", produces=products
):
    """Task to plot the trend of mean values for key indicators over the years."""
    mean_data = pd.read_pickle(mean_values)
    plot_mean_trends(mean_data, produces[0].parent)
