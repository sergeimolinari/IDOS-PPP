import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"

from idos_ppp.parameters import three_p_indexes


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
            f"Boxplot of {dataset_name.capitalize()}' {index.capitalize()} over the years",
        )

        output_png_file_path = output_dir / f"{index.capitalize()}_boxplot.png"
        plt.savefig(output_png_file_path)
        plt.close()


# Heatmaps -> Function: Create a function to create a heatmap for the correlation of the 3P indexes over the years.

# PROBLEMMMMMMMM

def plot_correlation_heatmap(data, output_dir):
    """
    Plot correlation heatmaps for the 3P indexes and highlight pessimistic and optimistic values.

    Arguments:
    - data: pd.DataFrame containing the raw data.
    - output_dir: Path, directory to save the output plots.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    # Extract the dataset name from the output directory path
    dataset_name = output_dir.name.replace("_", " ")

    data = data.reset_index()

    # Iterate over each year
    for year in data['year'].unique():
        plt.figure(figsize=(10, 6))

        # Filter data for the current year
        year_data = data[data['year'] == year]

        # Calculate the mean values for the three_p_indexes
        mean_values = year_data[three_p_indexes].mean().to_frame().T

        # Calculate the correlation matrix for the mean values
        correlation_matrix = mean_values.corr()

        # Create a heatmap
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', cbar_kws={'label': 'Correlation Values'})

        # Highlight cells with values below 0.2 and above 0.8
        highlight_mask_low = correlation_matrix < 0.2
        highlight_mask_high = correlation_matrix > 0.8

        # Create custom colormaps for highlighting
        cmap = sns.color_palette("coolwarm", as_cmap=True)
        highlight_cmap_pessimistic = sns.light_palette("blue", as_cmap=True)
        highlight_cmap_optimistic = sns.light_palette("green", as_cmap=True)

        # Plot the heatmap with highlighting
        sns.heatmap(correlation_matrix, annot=True, cmap=cmap, mask=~(highlight_mask_low | highlight_mask_high), cbar_kws={'label': 'Correlation Values'})
        sns.heatmap(correlation_matrix, annot=True, cmap=highlight_cmap_pessimistic, mask=~highlight_mask_low, cbar=False)
        sns.heatmap(correlation_matrix, annot=True, cmap=highlight_cmap_optimistic, mask=~highlight_mask_high, cbar=False)

        plt.title(f'Correlation Heatmap of {dataset_name.capitalize()} Mean Values for {year}')

        output_png_file_path = output_dir / f"{year}_correlation_heatmap.png"
        plt.savefig(output_png_file_path)
        plt.close()

# Example usage:
# plot_correlation_heatmap(raw_data, BLD / "final" / "correlation_heatmaps" / "dataset_name")

# Error handling functions
def _fail_if_not_dataframe(data):
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Expected a DataFrame")


def _fail_if_empty_dataframe(data):
    if data.empty:
        raise ValueError("DataFrame is empty")
