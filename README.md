[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/RN_okVXh)

# *Exploring the 3P Index: Data-Driven Insights for the MENA Team*

# MEETING 28/5

- Markus -> We have identified the following possible independent variables as possible
  explaining ones:

  - Growth (or change in growth)
  - Revolutions, coups d’état, seizures of power,
  - Wars, civil wars
  - Terrorism
  - Changes in the share of tax revues as a share of GDP
  - Protests Please let us all think about:
  - Possible additional ones
  - Indicators to measure these variables In addition, Sergei will:
  - Try to add the data for 2022 for all three Ps for as many countries as possible.
  - Add at least 1-2Ps also for countries like Iraq where the data of 1-2 Ps are
    missing.
  - Add countries like South Sudan for the years for which we have data.
  - Double check the excel sheet if the issue about “median/average” has been settled
    now everywhere in the excel file.

- Amirah -> I am not sure we had planned to regress the index on growth or the change in
  the index on growth? Anyways, I thought it over again and just a quick note regarding
  the regression setup:

  - In case we regress the index on growth: regressing a level variable - such our index
    measuring government service provision - on a change variable like annual GDP growth
    can pose both conceptual and statistical challenges. The interpretation is not
    always straightforward, as this regression assumes that short-term economic growth
    leads directly to shifts in a stock or a structural outcome, which is unlikely to be
    the case unless the index is highly responsive to economic cycles. Also, there’s a
    potential mismatch in variable properties (levels vs. differences), which can lead
    to spurious results, especially if the index trends over time while GDP growth
    fluctuates. So it is more appropriate to regress changes in the index on GDP growth
    (likely I just missed that in our meeting), or using lagged GDP growth as a
    predictor of the index level to better capture delayed effects. I also realized that
    if we use year fixed effects shocks in specific years will be accounted for (such as
    the financial crisis and the COVID). It wasn’t clear that we plan to use fixed
    effects (although quite challenging with such a small sample).
  - In case we regress the ‘change’ in the index on growth: We will be faced with the v
    limited variation in the dependent variable (ΔIndex) which we have already seen in
    our results. This will reduce the statistical power of our regression. On the other
    hand, we have high volatility in our independent variable (GDP growth): This large
    fluctuation will likely introduce noise. Unless there's a strong, consistent
    relationship, this volatility could weaken coefficient significance and increase
    standard errors. Generally even if we do the change on change, government
    deliverables evolve gradually while GDP growth is cyclical and volatile. This
    mismatch could result in weak or insignificant correlations, especially over short
    time spans. Though of course the changes across sample countries despite the
    observations over time may produce reasonable results. So we can and should run the
    regressions anyway but we should be prepared for unwanted results. In such a case it
    maybe better to invest in interpreting the fantastic visual results produced
    focusing on the observed interesting trends and outliers.

- Amirah -> Please find below:

  1. a list of potential control variables and reasons why they may be relevant
  1. a suggestion for a good regression strategy. Markus will you please check and
     re-confirm with Sergei.

  - additional regressors/control variables - they should mainly “not” be correlated
    with our main regressor GDP growth:
    - Official Development Assistance (ODA): in low and middle -income countries, a
      large share of service delivery maybe funded externally.
    - log(population) and the urbanization level: population scale and density or the
      scale and geography of the population could affect service delivery (e.g. per
      capita coverage, logistical costs). level of urbanization measured as= (Urban
      population/ Total population) x 100
    - Institutional quality (Rule of Law, Government Effectiveness, Control of
      Corruption, Democracy Index/regime type: from the World Governance Indicators):
      strong institutions help translate GDP into actual service delivery. Countries
      with same income levels may differ a lot in performance due to governance quality
      and responsiveness.
    - Demographics such as % of population under 15, that is the dependency ratio: young
      populations require more education and health services, influencing both needs and
      policy priorities (the assumption would be the higher the rate the more we should
      observe gov provision.
    - Fiscal capacity such as government spending as % of GDP, tax revenue as % of GDP:
      GDP enables capacity, but actual government spending channels that capacity into
      services (I have doubts about this one but worth it to look into it, I see also
      the counter logic not to use it).
    - Human capital indicators such as the literacy rate (or illiteracy for that matter)
      and average years of schooling: These are both outcome variables but are also
      “facilitators” of service provision, especially in health and education sectors
      (the higher the easier is distribution so to speak).
    - Conflict such as the presence of conflict, fragility index, or dummy for fragile
      states: conflict-affected countries likely to experience service delivery
      breakdowns regardless of GDP. This variable is included in our protection index
      but not in the provision index so can be safely used as a regressor for the
      Provision P.
  - regression model: Despite the limited number of years we should make use of the
    panel nature of our dataset as Markus has stressed several times. We should:
    - Use panel data with country fixed effects to control for unobserved time-invariant
      characteristics.
    - Add year fixed effects to control for time shocks.
    - Consider using clustered standard errors at the country level to account for
      serial correlation.
    - Since GDP growth is quite volatile we could lag GDP growth, so for example use
      average growth over the past 2–3 years to reflect the delayed impact on government
      capabilities.
    - We should probably introduce the additional controls one after the other to see
      how the regression changes with additions and to observe the robustness in our
      variables. I just thought mostly about controls for the Provision P we should also
      think about suitable controls for the other Ps. I will do so after my return from
      my short holiday. So Markus (and Tina) please check and let us (particularly
      Segei) know what you think and whether you would like to further discuss any
      aspect. Sergei will you be able to get the variables and implement the regression
      strategy if we agree on it?

# NEXT STEPS

- Update data for protection in year 2007 (median to mean)

- Brainstorming for independent variables -> difference between years (RDD and DiD) ->
  observations and maybe motivation

- Protest data ?

- When where the shocks for each country / region?

- Changes for provision: was it one sub-index or a shift between different sub-indexes?

- Find data for 2022

- Add countries: analysis Sudan and South Sudan, and countries that were previously
  removed

- Remember:

  - Variance: Do the three indices display existing disparities between different
    countries? -> check interval / range.
  - Plausibility: Are the results in line with possible explanations? -> values as in
    the figures in chapter 4.2.
  - Consistency between indices: Are the indices scaled in a consistent way? -> compare
    the 3 Ps respective values as they cover a similar range, and their means and
    medians are not too different. check also the correlation between each other.
  - Consistency within indices: Are the components of the three indices (the values of
    their aspects) consistent, that is, reasonably correlated? -> check correlations of
    the components for each 3P index.
  - Consistency with other indices: Are the three indices in line with other indices
    (i.e. do they fulfil the criterion of “concurrent validity”)? -> check consistency
    with popular indicators such as per capita income and indices such as the HDI or the
    Global Peace Index.
  - Added value: Do the indices add information to other available indicators and
    indices? -> check which countries are better for each 3P index.

- Next paper -> development of countries over time, with an obvious focus on MENA
  countries (trends).

# Done

- Countries to leave out: Belarus (left out because data missing for provision index),
  Eswatini (left out because data missing for protection and provision index), Gabon
  (left out because data missing for provision index), Iraq (left out because data
  missing for provision index), Papua New Guinea (left out because data missing for
  provision index), South Sudan (left out because country has come into being during the
  period 2007-19), Sudan (left out because data missing for provision index), Uzbekistan
  (left out because data missing for provision index).
- Created sub-datasets for Conflict/Post-Conflict countries, GCC and Repressive
  Countries, and EU Countries.

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
  "3P" indexes (Protection, Provision, Participation), with each indicator standardized
  to a 0–1 scale and weighted based on its relevance to the respective index.
- The list of aspects included in each of the six elements of social contracts:
  Protection: collective security (i) against foreign threats and (ii) against acts of
  civil war; security of individuals/citizens (iii) against physical threats such as
  alleged or real terrorist and criminal acts and (iv) against political threats by own
  government; (v) human rights aspects of rule of law (including the law as such,
  especially the existence and enforcement of human and civil rights); and (vi) security
  against natural, environmental and other macro risks. Provision of economic and social
  services: (i) infrastructure (communication, information, transport, utilities), (ii)
  education, (iii) health services, (iv) social protection, (v) poverty reduction, (vi)
  employment, (vii) economic aspects of rule of law (transparency, fair competition,
  reliability of government regulation), (viii) a good business climate and (ix)
  resources in production (e.g. water, land). Participation by society in political
  decision-making by (i) free, fair and secret elections, (ii) open public debates and
  (iii) free mass media and other channels. Citizens’ acceptance of the rule of the
  government. Citizens’ delivery of (i) taxes and other obligations such as (ii)
  military or civil service, (iii) respect of public order, (iv) engagement in civil
  society (e.g. neighborly help, support for school child care) or (v) financial
  donations to social work. Deliverables exchanged between social groups and citizens:
  (i) mutual respect and recognition, (ii) dialogue on conflictive issues, (iii) mutual
  support (of course, there is some overlap in contents with engagement and financial
  donations, mentioned already in the previous element, but they also have an
  intra-societal specification).
- In particular, here is **a detailed overview of the three indices for government
  deliverables of social contracts**:
  - **Protection**:
    - External threats (Weight: 20.00%, Index: FFP Fragile States Index X1, Source: The
      Fund for Peace).
    - Civil wars (Weight: 20.00%, Index: UCDP data on fatalities in civil wars, Source:
      University of Uppsala).
    - Criminal acts (Weight: 20.00%, Index: Global Competitiveness Index Pillar 1
      (Security), Source: World Economic Forum).
    - State terror (Weight: 20.00%, Index: Political Terror Scale, Source: University of
      North Carolina).
    - Rule of law /human rights (Weight: 20.00%, Index: FFP Fragile States Index P3,
      Source: The Fund for Peace).
    - Environmental threats (Weight: not yet included).
  - **Provision**:
    - Water, Land (Weight: not yet included).
    - Infrastructure (1. Weight: 6.25%, Index: Global Competitiveness Index Pillar 2
      (Transport and utilities), Source: World Economic Forum; 2. Weight: 6.25%, Index:
      Telecommunication Infrastructure Index, Source: UN Statistics Division).
    - Education (1. Weight: 6.25%, Index: Gov't expenditure on primary and secondary
      education (% of GDP), Source: World Bank; 2. Weight: 6.25%, Index: Global
      Competitiveness Index Pillar 6.4 (Skills of future workforce), Source: World
      Economic Forum).
    - Health (1. Weight: 6.25%, Index: Gov't health expenditure (% of GDP), Source:
      World Bank; 2. Weight: 6.25%, Index: Out of pocket expenditure (% of total
      national health care spending), Source: World Bank).
    - Social protection (1. Weight: 6.25%, Index: Public social protection expenditure
      excl. health (% of GDP), Source: World Bank; 2. Weight: 6.25%, Index: Share of
      people above retirement age receiving an old-age pension, Source: International
      Labour Office).
    - Poverty reduction (1. Weight: 6.25%, Index: Public expenditure on social safety
      nets (% of GDP), Source: World Bank; 2. Weight: 6.25%, Index: Vulnerable persons
      covered by social assistance (%), Source: International Labour Office).
    - Employment (1. Weight: 6.25%, Index: Share of wage employment on work age
      population (%), Source: International Labour Office; 2. Weight: 6.25%, Index:
      Working poverty head-count rate (%), Source: International Labour Office).
    - Rule of law (economic) (1. Weight: 6.25%, Index: Global Competitiveness Index
      Pillar 1F (Property rights), Source: World Economic Forum; 2. Weight: 6.25%,
      Index: Global Competitiveness Index Pillar 1E (Incidence of corruption), Source:
      World Economic Forum).
    - Markets (1. Weight: 6.25%, Index: Global Competitiveness Index Pillar 7A (Market
      competition), Source: World Economic Forum; 2. Weight: 6.25%, Index: Global
      Competitiveness Index Pillar 1E (Public-sector performance), Source: World
      Economic Forum).
  - **Participation**:
    - V-Dem Index on electoral democracy (Weight: 50.00%, Source: University of
      Gothenburg).
    - Voice and Accountability Indicator (Weight: 50.00%, Source: World Bank).
- We also realized that it is difficult to find meaningful indicators for the last three
  elements, that is, the deliverables provided by and among society in general. Some of
  their aspects are covered by the questions included in the World Value Survey, but
  only few of their aspects. Other databases, such as the Afrobarometer, include more
  aspects, but they cover only a limited number of countries. For this reason, the
  measurement of social cohesion developed by Leininger et al. (2021) currently contains
  only data on African countries. Therefore, we decided to disregard these three
  elements in our first move towards measuring social contracts and instead focus fully
  on the three Ps that governments can give to society. We measure thus just the efforts
  of one side of the social contract; we cannot yet assess how much these efforts impact
  and depend on the deliverables of the other parties (e.g. the readiness of society to
  pay taxes, do military service and contribute to other public goods). We plan to
  conduct this second step in another paper.

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
