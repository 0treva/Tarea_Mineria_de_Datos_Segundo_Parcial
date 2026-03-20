from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "life_expectancy_data.csv"
MODEL_DIR = PROJECT_ROOT / "model"
MODEL_PATH = MODEL_DIR / "model.pkl"
METRICS_PATH = MODEL_DIR / "metrics.json"
METADATA_PATH = MODEL_DIR / "metadata.json"

RAW_TO_CLEAN_COLUMNS = {
    "Country": "country",
    "Year": "year",
    "Status": "status",
    "Life expectancy ": "life_expectancy",
    "Life expectancy": "life_expectancy",
    "Adult Mortality": "adult_mortality",
    "infant deaths": "infant_deaths",
    "Alcohol": "alcohol",
    "percentage expenditure": "percentage_expenditure",
    "Hepatitis B": "hepatitis_b",
    "Measles ": "measles",
    "Measles": "measles",
    " BMI ": "bmi",
    "BMI": "bmi",
    "under-five deaths ": "under_five_deaths",
    "under-five deaths": "under_five_deaths",
    "Polio": "polio",
    "Total expenditure": "total_expenditure",
    "Diphtheria ": "diphtheria",
    "Diphtheria": "diphtheria",
    " HIV/AIDS": "hiv_aids",
    "HIV/AIDS": "hiv_aids",
    "GDP": "gdp",
    "Population": "population",
    " thinness  1-19 years": "thinness_1_19_years",
    "thinness  1-19 years": "thinness_1_19_years",
    " thinness 5-9 years": "thinness_5_9_years",
    "thinness 5-9 years": "thinness_5_9_years",
    "Income composition of resources": "income_composition_of_resources",
    "Schooling": "schooling",
}

TARGET_COLUMN = "life_expectancy"
DROP_COLUMNS = ["country"]
CATEGORICAL_COLUMNS = ["status"]

BASE_NUMERIC_COLUMNS = [
    "year",
    "adult_mortality",
    "infant_deaths",
    "alcohol",
    "percentage_expenditure",
    "hepatitis_b",
    "measles",
    "bmi",
    "under_five_deaths",
    "polio",
    "total_expenditure",
    "diphtheria",
    "hiv_aids",
    "gdp",
    "population",
    "thinness_1_19_years",
    "thinness_5_9_years",
    "income_composition_of_resources",
    "schooling",
]

DERIVED_NUMERIC_COLUMNS = [
    "immunization_mean",
    "adult_infant_ratio",
    "gdp_per_capita_proxy",
    "thinness_gap",
]

REQUIRED_FEATURES = [
    "year",
    "status",
    "adult_mortality",
    "infant_deaths",
    "alcohol",
    "percentage_expenditure",
    "hepatitis_b",
    "measles",
    "bmi",
    "under_five_deaths",
    "polio",
    "total_expenditure",
    "diphtheria",
    "hiv_aids",
    "gdp",
    "population",
    "thinness_1_19_years",
    "thinness_5_9_years",
    "income_composition_of_resources",
    "schooling",
]

LOG_TRANSFORM_COLUMNS = [
    "infant_deaths",
    "percentage_expenditure",
    "measles",
    "under_five_deaths",
    "hiv_aids",
    "gdp",
    "population",
    "adult_infant_ratio",
    "gdp_per_capita_proxy",
]

MODEL_CANDIDATES = {
    "linear_regression_70_30": 0.30,
    "linear_regression_80_20": 0.20,
}

EXAMPLE_PAYLOAD = {
    "year": 2015,
    "status": "Developing",
    "adult_mortality": 263.0,
    "infant_deaths": 62,
    "alcohol": 0.01,
    "percentage_expenditure": 71.27962362,
    "hepatitis_b": 65.0,
    "measles": 1154,
    "bmi": 19.1,
    "under_five_deaths": 83,
    "polio": 6.0,
    "total_expenditure": 8.16,
    "diphtheria": 65.0,
    "hiv_aids": 0.1,
    "gdp": 584.25921,
    "population": 33736494.0,
    "thinness_1_19_years": 17.2,
    "thinness_5_9_years": 17.3,
    "income_composition_of_resources": 0.479,
    "schooling": 10.1,
}
