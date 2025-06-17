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

#### LISTS OF COUNTRIES

# Latin America and the Caribbean
latin_america_caribbean = [
    "Antigua and Barbuda", "Argentina", "Aruba", "Bahamas", "Barbados",
    "Belize", "Bolivia", "Brazil", "British Virgin Islands", "Cayman Islands",
    "Chile", "Colombia", "Costa Rica", "Cuba", "Curacao", "Dominica",
    "Dominican Republic", "Ecuador", "El Salvador", "Grenada", "Guatemala",
    "Guyana", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama",
    "Paraguay", "Peru", "Puerto Rico", "Sint Maarten (Dutch part)",
    "St. Kitts and Nevis", "St. Lucia", "St. Martin (French part)",
    "St. Vincent and the Grenadines", "Suriname", "Trinidad and Tobago",
    "Turks and Caicos Islands", "Uruguay", "Venezuela", "Virgin Islands (U.S.)"
]

# South Asia
south_asia = [
    "Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives", "Nepal",
    "Pakistan", "Sri Lanka"
]

# East Asia and Pacific
east_asia_pacific = [
    "American Samoa", "Brunei Darussalam", "Cambodia", "China", "Fiji",
    "French Polynesia", "Guam", "Hong Kong SAR, China", "Indonesia", "Japan",
    "Kiribati", "Korea, Dem. People's Rep.", "Korea, Rep.", "Lao PDR",
    "Macao SAR, China", "Malaysia", "Marshall Islands", "Micronesia, Fed. Sts.",
    "Mongolia", "Myanmar", "Nauru", "New Caledonia", "Northern Mariana Islands",
    "Palau", "Papua New Guinea", "Philippines", "Samoa", "Singapore",
    "Solomon Islands", "Taiwan, China", "Thailand", "Timor-Leste", "Tonga",
    "Tuvalu", "Vanuatu", "Vietnam"
]

# Middle East and North Africa
middle_east_north_africa_countries = [
    "Algeria", "Bahrain", "Djibouti", "Egypt, Arab Rep.", "Iran, Islamic Rep.",
    "Iraq", "Jordan", "Kuwait", "Lebanon", "Libya", "Morocco", "Oman", "Qatar",
    "Saudi Arabia", "Sudan", "Syrian Arab Republic", "Tunisia", "Turkey",
    "United Arab Emirates", "West Bank and Gaza", "Yemen, Rep."
]

# Sub-Saharan Africa
sub_saharan_africa = [
    "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde",
    "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, Dem. Rep.",
    "Congo, Rep", "Côte d'Ivoire", "Equatorial Guinea", "Eritrea", "Eswatini",
    "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau",
    "Kenya", "Lesotho", "Liberia", "Madagascar", "Malawi", "Mali", "Mauritania",
    "Mauritius", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda",
    "São Tomé and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia",
    "South Africa", "South Sudan", "Tanzania", "Togo", "Uganda", "Zambia", "Zimbabwe"
]

# Sub-Saharan Africa excluding four positive outliers
ssa_excluding_outliers = [
    country for country in sub_saharan_africa
    if country not in {"Botswana", "Mauritius", "Seychelles", "South Africa"}
]

# European Union
european_union_countries = [
    "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark",
    "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland",
    "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland",
    "Portugal", "Romania", "Slovak Republic", "Slovenia", "Spain", "Sweden"
]

# Other Western Europe and Western Off-springs
other_western = [
    "Australia", "Canada", "Iceland", "Israel", "New Zealand", "Norway",
    "Switzerland", "United Kingdom", "United States"
]

# Other Eastern Europe
other_eastern_europe = [
    "Albania", "Armenia", "Belarus", "Bosnia and Herzegovina", "Georgia",
    "Greenland", "Kosovo", "Azerbaijan", "Moldova", "Montenegro", "North Macedonia",
    "Russian Federation", "Serbia", "Ukraine"
]

# Central Asia
central_asia = [
    "Kazakhstan", "Kyrgyz Republic", "Tajikistan", "Turkmenistan", "Uzbekistan"
]

# Not Included Anywhere Because Too Small
too_small_regions = [
    "Andorra", "Channel Islands", "Faroe Islands", "Gibraltar", "Isle of Man",
    "Liechtenstein", "Monaco", "San Marino"
]

# Conflic / Post-conflict (from Heydemann 2025)
conflict_countries = [
    "Libya", "Syrian Arab Republic", "Yemen, Rep."
] # Only Yemen as Libya and Syrian Arab Republic are not part of our dataset

conflict_and_postconflict_countries = [
    "Iraq", "Lebanon", "Libya", "Syrian Arab Republic", "Yemen, Rep."
] # We left out Iraq because of the data missing for provision index

# GCC countries (and repressive ones) (from Heydemann 2025)
gcc_high_income_countries = [
    "Bahrain", "Kuwait", "Oman", "Qatar", "Saudi Arabia", "United Arab Emirates"
]

repressive_countries = [
    "Egypt, Arab Rep.", "Jordan", "Morocco", "Tunisia"
] # Tunisia post-2020

gcc_and_repressive_countries = [
    "Bahrain", "Kuwait", "Oman", "Qatar", "Saudi Arabia", "United Arab Emirates", "Egypt, Arab Rep.", "Jordan", "Morocco", "Tunisia"
] # Tunisia post-2020

# Countries to leave out
countries_to_leave_out = [
    "Belarus",
    "Eswatini",
    "Gabon",
    "Iraq",
    "Papua New Guinea",
    "South Sudan",
    "Sudan",
    "Uzbekistan"
]

countries_to_leave_out_due_to_provision = [
    "Belarus",
    "Eswatini",
    "Gabon",
    "Iraq",
    "Papua New Guinea",
    "Sudan",
    "Uzbekistan"
]

countries_to_leave_out_due_to_protection = ["Eswatini"]

country_lists = {
    "conflict_countries": conflict_countries,
    "conflict_and_postconflict_countries": conflict_and_postconflict_countries,
    "gcc_high_income_countries": gcc_high_income_countries,
    "repressive_countries": repressive_countries,
    "gcc_and_repressive_countries": gcc_and_repressive_countries,
    # (from Heydemann 2025)
    "european_union_countries": european_union_countries,
    "middle_east_north_africa_countries": middle_east_north_africa_countries,
    # add countries to leave out to study these countries
    # "countries_to_leave_out": countries_to_leave_out
    } 


