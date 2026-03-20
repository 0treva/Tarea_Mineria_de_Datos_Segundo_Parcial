import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class FeatureEngineer(BaseEstimator, TransformerMixin):
    """
    Crea variables derivadas simples para fortalecer la regresión.
    """

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        df = X.copy()

        numeric_cols = [col for col in df.columns if col != "status"]
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        immunization_cols = [col for col in ["hepatitis_b", "polio", "diphtheria"] if col in df.columns]
        if immunization_cols:
            df["immunization_mean"] = df[immunization_cols].mean(axis=1)

        if {"adult_mortality", "infant_deaths"}.issubset(df.columns):
            df["adult_infant_ratio"] = df["adult_mortality"] / (df["infant_deaths"] + 1.0)

        if {"gdp", "population"}.issubset(df.columns):
            df["gdp_per_capita_proxy"] = df["gdp"] / (df["population"] + 1.0)

        if {"thinness_1_19_years", "thinness_5_9_years"}.issubset(df.columns):
            df["thinness_gap"] = df["thinness_1_19_years"] - df["thinness_5_9_years"]

        return df
