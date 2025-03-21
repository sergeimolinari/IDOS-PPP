import pandas as pd

identifier_codes = {
    2: "1-1",
    3: "1-2",
    4: "1-3",
    5: "1-4",
    6: "1-5",
    8: "2-1-1",
    9: "2-1-2",
    10: "2-2-1",
    11: "2-2-2",
    12: "2-3-1",
    13: "2-3-2",
    14: "2-4-1",
    15: "2-4-2",
    16: "2-5-1",
    17: "2-5-2",
    18: "2-6-1",
    19: "2-6-2",
    20: "2-7-1",
    21: "2-7-2",
    22: "2-8-1",
    23: "2-8-2",
    25: "3-1",
    26: "3-2",
}

identifier_codes_underscore = {
    k: v.replace("-", "_") for k, v in identifier_codes.items()
}

three_p_indexes = ["protection", "provision", "participation"]

specific_column_mapping = {
    "1-2": "1_2_ucdp",
    "1-4": "1_4_political_terror",
    "1-5": "1_5_ffp_p3",
    "2-1-1": "2_1_1_wef_gcr_2nd_pillar:_infrastructure",
    "2-1-2": "2_1_2_un:_telecom",
    "2-2-1": "2_2_1_government_expend._on_primary_and_secondary_education,_total_(%_of_gdp)",
    "2-2-2": "2_2_2_wef_gcr_indicator_quality_of_primary_education",
    "2-3-1": "2_3_1_domestic_general_government_health_expenditure_(%_of_gdp)",
    "2-3-2": "2_3_2_out_of_pocket_expenditure_(%_of_total_national_health_care_spending)",
    "2-4-1": "2_4_1_public_social_protection_(excl._health)_expenditure_(%_of_gdp)",
    "2-4-2": "2_4_2_coverage_of_older_persons_by_sp_benefits",
    "2-6-1": "2_6_1_share_of_wage_employment_on_work_age_pop",
    "2-6-2": "2_6_2_working_poverty_head_count_rate_(percentage_of_persons_living_in_poverty_in_spite_of_being_employed)",
    "3-1": "3_1_v_dem_index_on_electoral_democracy",
    "3-2": "3_2_wb_voice_and_accountability_indicator",
}

years = [2007, 2010, 2013, 2016, 2019]

sheet_names = [
    f"Transformed {year}" if year != 2019 else "Transformed 2019 new" for year in years
]

missing_countries = pd.DataFrame(
    {
        "country_alpha3": ["ROM", "TMP", "ZAR"],
        "continent": [
            "Europe",
            "Oceania",
            "Africa",
        ],  # Replace with actual continent names if different
    }
)
