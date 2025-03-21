import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

from idos_ppp.parameters import three_p_indexes


def plot_mean_trends(data, output_dir):
    """Plot the trend and stores the plots in png format of the mean values for the 3P indexes over the years.

    Arguments:
    - data: pd.DataFrame containing the mean statistics data.
    - output_dir: Path, directory to save the output plots.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    for index in three_p_indexes:
        plt.figure(figsize=(12, 6))

        sns.lineplot(data=data, x="year", y=index, hue="continent", marker="o")

        plt.xlabel("Year")
        plt.ylabel("Mean Value")
        plt.title(f"Trend of {index.capitalize()} Over Years")
        plt.legend(title="Continent")

        output_file = output_dir / f"{index}_mean_trend.png"
        plt.savefig(output_file)
        plt.close()


# Error handling functions
def _fail_if_not_dataframe(data):
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Expected a DataFrame")


def _fail_if_empty_dataframe(data):
    if data.empty:
        raise ValueError("DataFrame is empty")
