import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
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
            f"Boxplot of {dataset_name.title()}' {index.title()} Over The Years",
        )

        output_png_file_path = output_dir / f"{index.capitalize()}_boxplot.png"
        plt.savefig(output_png_file_path)
        plt.close()


# Scatterplots for correlations -> Function: Create a function to create a heatmap for the correlation of the 3P indexes over the years.


def plot_correlation(data, output_dir):
    """Plot correlation values over the years and highlight pessimistic and optimistic values, as well as observations with low p-values.

    Arguments:
    - data: pd.DataFrame containing the raw data.
    - output_dir: Path, directory to save the output plots.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    dataset_name = output_dir.name.replace("_", " ")

    folder_name = output_dir.parent.name.replace("_", " ")

    if "year" not in data.columns:
        data = data.reset_index()

    filtered_data = data[
        (abs(data["correlation"]) < 0.2)
        | (abs(data["correlation"]) > 0.8)
        | (data["p_value"] < 0.1)
    ]

    plt.figure(figsize=(10, 6))

    plt.scatter(
        filtered_data["year"],
        filtered_data["correlation"],
        c=filtered_data["correlation"],
        cmap="viridis",
    )

    pessimistic_data = filtered_data[abs(filtered_data["correlation"]) < 0.2]
    plt.scatter(
        pessimistic_data["year"],
        pessimistic_data["correlation"],
        color="red",
        label="Low (< 0.2)",
        zorder=5,
    )

    optimistic_data = filtered_data[abs(filtered_data["correlation"]) > 0.8]
    plt.scatter(
        optimistic_data["year"],
        optimistic_data["correlation"],
        color="green",
        label="High (> 0.8)",
        zorder=5,
    )

    # Highlight data with low p-values
    low_p_value_data = filtered_data[filtered_data["p_value"] < 0.1]
    plt.scatter(
        low_p_value_data["year"],
        low_p_value_data["correlation"],
        color="purple",
        label="Low p-value (< 0.1)",
        zorder=5,
    )

    plt.xlabel("Year")
    plt.title(f"{folder_name.title()} of {dataset_name.title()} Over The Years")

    # Add description about high p-values
    description = "Low p-values (typically < 0.1): Indicate strong evidence against the null hypothesis (H0: corr = 0)."
    plt.figtext(
        0.5,
        0.01,
        description,
        ha="center",
        fontsize=10,
        bbox={"facecolor": "orange", "alpha": 0.5, "pad": 5},
    )

    plt.legend()

    output_png_file_path = output_dir / f"{output_dir.name}_correlation.png"
    plt.savefig(output_png_file_path)
    plt.close()


# Bar Charts -> Create a bar chart to compare the values of key indices between countries for a specific year.


def plot_comparative_bar_chart(data, year, indices):
    """Plot a comparative bar chart for the given indices between countries for a specific year.

    Arguments:
    - data: pd.DataFrame containing the filtered data.
    - year: int, the year to plot.
    - indices: list containing the indices to compare.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    plt.figure(figsize=(12, 6))

    # Filter data for the specific year
    year_data = data[data["year"] == year]

    # Melt the data for plotting
    melted_data = year_data.melt(
        id_vars=["country_name"],
        value_vars=indices,
        var_name="Index",
        value_name="Value",
    )

    countries = melted_data["country_name"].unique()

    # Create a bar chart
    sns.barplot(data=melted_data, x="Index", y="Value", hue="country_name")

    plt.title(
        f"Comparison of Key Indices between countries for {year}" # {countries[0]} and {countries[1]}
    )
    plt.ylabel("Value")
    plt.legend(title="Country")


# Create interactive plots using Plotly to allow to explore the data dynamically.


def plot_trends_interactive_plots(data, indices, output_dir, list_name):
    """Plot interactive plots for the given indices over time for the considered countries.

    Arguments:
    - data: pd.DataFrame containing the filtered data.
    - indices: list containing the indices to plot.
    - output_dir: Path, directory to save the output plots.
    - list_name: str, name of the list to use in the output file name.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    melted_data = data.melt(
        id_vars=["country_name", "year"],
        value_vars=indices,
        var_name="Index",
        value_name="Value",
    )

    countries = melted_data["country_name"].unique()

    fig = px.line(
        melted_data,
        x="year",
        y="Value",
        color="country_name",
        line_group="Index",
        line_dash="Index",
        hover_name="Index",
    )

    fig.add_vline(
        x=2011,
        line_width=3,
        line_dash="dash",
        line_color="orange",
        annotation_text="2011",
        annotation_position="bottom left",
    )

    fig.for_each_trace(
        lambda t: t.update(
            name=t.name.replace("country_name=", "Country Name: ")
            .replace("Index=", "")
            .title()
        )
    )

    if len(countries) > 2:
        fig.update_layout(title="Trends of 3P Indices Over Time")
    elif len(countries) == 2:
        fig.update_layout(
            title=f"Trends of 3P Indices Over Time for {countries[0]} and {countries[1]}"
        )
    else:
        fig.update_layout(title=f"Trends of 3P Indices Over Time for {countries[0]}")

    fig.write_html(output_dir / f"{list_name}_interactive_plot.html")


# Create interactive plots using Plotly to allow to explore the growth datasets dynamically.


def plot_growth_interactive_plots(data, indices, output_dir, list_name):
    """Plot interactive plots for the given growth indices over time for the considered countries.

    Arguments:
    - data: pd.DataFrame containing the filtered data.
    - indices: list containing the growth indices to plot.
    - output_dir: Path, directory to save the output plots.
    - list_name: str, name of the list to use in the output file name.
    """
    _fail_if_not_dataframe(data)
    _fail_if_empty_dataframe(data)

    melted_data = data.melt(
        id_vars=["country_name", "year"],
        value_vars=indices,
        var_name="Index",
        value_name="Value",
    )

    countries = melted_data["country_name"].unique()

    fig = px.line(
        melted_data,
        x="year",
        y="Value",
        color="country_name",
        line_group="Index",
        line_dash="Index",
        hover_name="Index",
    )

    fig.add_vline(
        x=2011,
        line_width=3,
        line_dash="dash",
        line_color="orange",
        annotation_text="2011",
        annotation_position="bottom left",
    )

    fig.add_hline(y=1.1, line_width=6, line_dash="dash", line_color="green")

    fig.add_hline(y=0.9, line_width=6, line_dash="dash", line_color="red")

    fig.for_each_trace(
        lambda t: t.update(
            name=t.name.replace("country_name=", "Country Name: ")
            .replace("Index=", "")
            .title()
        )
    )

    if len(countries) > 2:
        fig.update_layout(title="Growth of 3P Indices Over Time")
    elif len(countries) == 2:
        fig.update_layout(
            title=f"Growth of 3P Indices Over Time for {countries[0]} and {countries[1]}"
        )
    else:
        fig.update_layout(title=f"Growth of 3P Indices Over Time for {countries[0]}")

    fig.write_html(output_dir / f"{list_name}_growth_interactive_plot.html")


# Error handling functions
def _fail_if_not_dataframe(data):
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Expected a DataFrame")


def _fail_if_empty_dataframe(data):
    if data.empty:
        raise ValueError("DataFrame is empty")
