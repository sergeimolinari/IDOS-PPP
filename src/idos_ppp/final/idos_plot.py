import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

from idos_ppp.parameters import three_p_indexes, country_lists


# Boxplots -> Function: Create a function to create a boxplot for each of the 3P indexes over the years.


def plot_boxplots(data, output_dir):
    """Plot boxplots for each of the 3P indexes over the years and save the plots in png format.

    Arguments:
    - data: pd.DataFrame containing the statistics data.
    - output_dir: Path, directory to save the output plots.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    dataset_name = output_dir.name.replace("_", " ")

    for index in three_p_indexes:
        plt.figure(figsize=(12, 6))

        sns.boxplot(data=data, x="year", y=index)
        plt.xlabel("Year")
        plt.ylabel(f"{index.capitalize()} value")
        plt.title(
            f"Boxplot of {dataset_name.title()}' {index.title()} Over The Years",
        )

        output_png_file_path = output_dir / f"{index.capitalize()}_boxplot.png"
        plt.savefig(output_png_file_path)
        plt.close()


# Scatterplots for correlations -> Function: Create a function to create a heatmap for the correlation of the 3P indexes over the years.


def plot_correlation(data, output_dir):
    """
    Plot correlation values over the years and highlight pessimistic and optimistic values.

    Arguments:
    - data: pd.DataFrame containing the raw data.
    - output_dir: Path, directory to save the output plots.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    # Extract the dataset name from the output directory path
    dataset_name = output_dir.name.replace("_", " ")

    # Extract the folder name from the output directory path
    folder_name = output_dir.parent.name.replace("_", " ")

    data = data.reset_index()

    plt.figure(figsize=(10, 6))

    scatter = plt.scatter(data['year'], data['correlation'], c=data['correlation'], cmap='viridis')

    pessimistic_data = data[data['correlation'] < 0.2]
    plt.scatter(pessimistic_data['year'], pessimistic_data['correlation'], color='red', label='Low (< 0.2)', zorder=5)

    optimistic_data = data[data['correlation'] > 0.8]
    plt.scatter(optimistic_data['year'], optimistic_data['correlation'], color='green', label='High (> 0.8)', zorder=5)

    plt.xlabel("Year")
    plt.title(f'{folder_name.title()} of {dataset_name.title()} Over The Years')
    plt.legend()

    output_png_file_path = output_dir / f"{output_dir.name}_correlation.png"
    plt.savefig(output_png_file_path)
    plt.close()


# Error handling functions
def _fail_if_not_dataframe(data):
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Expected a DataFrame")


def _fail_if_empty_dataframe(data):
    if data.empty:
        raise ValueError("DataFrame is empty")
