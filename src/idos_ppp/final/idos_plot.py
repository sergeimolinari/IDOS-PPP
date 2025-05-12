import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

from idos_ppp.parameters import three_p_indexes, years, country_lists


'''
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
'''

def plot_boxplots(data, output_dir):
    """
    Plot boxplots for each of the 3P indexes over the years and save the plots in png format.

    Arguments:
    - data: pd.DataFrame containing the statistics data.
    - output_dir: Path, directory to save the output plots.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    # Iterate over each year and each index
    for year in years:
        for index in three_p_indexes:
            plt.figure(figsize=(12, 6))

            # Filter data for the current year and index
            year_data = data[data['year'] == year]
            sns.boxplot(data=year_data, x=year_data.index.get_level_values(0), y=(index, 'mean'))

            plt.xlabel("Year")
            plt.ylabel("Mean value")
            plt.title(f"Boxplot of {index.capitalize()} for year {year}")
            plt.xticks(rotation=45)

            output_png_file_path = output_dir / f"{index}_boxplot_{year}.png"
            plt.savefig(output_png_file_path)
            plt.close()

# PROBLEMMMMMMMMM

# Error handling functions
def _fail_if_not_dataframe(data):
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Expected a DataFrame")


def _fail_if_empty_dataframe(data):
    if data.empty:
        raise ValueError("DataFrame is empty")
