[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/RN_okVXh)

# Final Project Sergei Molinari: *Exploring the 3P Index: Data-Driven Insights for the MENA Team*

# Description

- This project uses the data from my work at IDOS (German Institute of Development and
  Sustainability) in the Stabilization and Development in the Middle East and North
  Africa team. My work has been conducted under the supervision of M. Loewe and T.
  Zintl, co-authors of the discussion paper "Operationalising social contracts: towards
  an index of government deliverables" (2024) (Further details are available here
  https://www.idos-research.de/en/mena/ and here
  https://www.idos-research.de/discussion-paper/article/operationalising-social-contracts-towards-an-index-of-government-deliverables/
  ). The research primarily focuses on the themes of Social Protection and Inclusive
  Growth.
- In recent months, and previously to the beginning of this project, our team has
  collected and processed data for 154 countries over a 12-year period (2007–2019). This
  work has resulted in a dataset designed to evaluate each country’s performance
  concerning social contracts. The dataset is structured to include indicators for the
  "3P" indexes(Protection, Provision, Participation), with each indicator standardized
  to a 0–1 scale and weighted based on its relevance to the respective index.

# Objectives

Building on this work, and recognizing the need for further data cleaning and analysis,
this project focuses mostly on data cleaning and management (data management) in order
to produce meaningful insights in the future for the research team. These will include
identifying trends, correlations, and visualizations (e.g., graphs and plots), with
potential emphasis on subsets of countries within the dataset (analysis and final
parts).

# How to run the project

## The Data

All the necessary data is present in the data folder in src/idos_ppp. It is possible to
download the dataset used to merge the continent variable with the cleaned dataset from
https://ourworldindata.org/grapher/continents-according-to-our-world-in-data .

## Programs set-up

To set up this project, you first need to install
[Miniconda](https://docs.conda.io/projects/miniconda/en/latest/) and
[Git](https://git-scm.com/downloads). Once those are installed, you can proceed with
creating and activating the environment.

## Creating and Activating the Environment

Start by navigating to the project's root directory in your terminal, and then type the
following into the console:

```console
$ mamba env create -f environment.yml
$ conda activate idos_ppp
```

## Building the Project

The `src` folder contains all the source code necessary to run this project. Files that
start with the prefix `task_` are `pytask` scripts, which execute when you run the
following command in the console, as they build up the whole project:

```console
$ pytask
```

The `tests` folder includes test scripts that check the functionality of the functions
defined in the source code. In order to run them, type:

```console
$ pytest
```

It is important to run `pytask` and then `pytest`, in this order, such that the tests
for the plots work.

If you encounter any issues, refer to the sections **"Preparing your system"** and
**"How to get started on a second machine"** in this
[website](https://econ-project-templates.readthedocs.io/en/stable/getting_started/index.html#preparing-your-system),
which is based on the template used for this project.

# Credits

The template for this project is from
[econ-project-templates](https://github.com/OpenSourceEconomics/econ-project-templates).

# Contributors

@SergeiMolinari
