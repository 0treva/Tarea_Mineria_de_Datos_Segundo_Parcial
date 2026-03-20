import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.config import (
    BASE_NUMERIC_COLUMNS,
    CATEGORICAL_COLUMNS,
    DERIVED_NUMERIC_COLUMNS,
    LOG_TRANSFORM_COLUMNS,
    METADATA_PATH,
    MODEL_PATH,
    RAW_TO_CLEAN_COLUMNS,
    REQUIRED_FEATURES,
)
from src.features import FeatureEngineer


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    renamed = df.rename(columns=RAW_TO_CLEAN_COLUMNS).copy()
    return renamed


def load_dataset(csv_path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df = clean_columns(df)
    return df


def prepare_features_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    frame = df.copy()
    for feature in REQUIRED_FEATURES:
        if feature not in frame.columns:
            frame[feature] = np.nan
    return frame[REQUIRED_FEATURES]


class LogTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, columns=None):
        self.columns = columns or []

    def fit(self, X, y=None):
        self.columns_ = [col for col in self.columns if col in X.columns]
        return self

    def transform(self, X):
        df = X.copy()
        for col in self.columns_:
            values = pd.to_numeric(df[col], errors="coerce")
            minimum = values.min(skipna=True)
            if pd.isna(minimum):
                continue
            shift = 1 - minimum if minimum <= 0 else 0
            df[col] = np.log1p(values + shift)
        return df


class IQRClipper(BaseEstimator, TransformerMixin):
    def __init__(self, factor: float = 1.5):
        self.factor = factor

    def fit(self, X, y=None):
        frame = pd.DataFrame(X).copy()
        self.columns_ = list(frame.columns)
        self.bounds_ = {}
        for col in self.columns_:
            values = pd.to_numeric(frame[col], errors="coerce")
            q1 = values.quantile(0.25)
            q3 = values.quantile(0.75)
            iqr = q3 - q1
            self.bounds_[col] = (q1 - self.factor * iqr, q3 + self.factor * iqr)
        return self

    def transform(self, X):
        frame = pd.DataFrame(X, columns=self.columns_).copy()
        for col in self.columns_:
            low, high = self.bounds_[col]
            frame[col] = pd.to_numeric(frame[col], errors="coerce").clip(low, high)
        return frame


def build_preprocessor() -> ColumnTransformer:
    numeric_features = BASE_NUMERIC_COLUMNS + DERIVED_NUMERIC_COLUMNS

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("outlier_clip", IQRClipper()),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    return ColumnTransformer(
        transformers=[
            ("numeric", numeric_pipeline, numeric_features),
            ("categorical", categorical_pipeline, CATEGORICAL_COLUMNS),
        ]
    )


def build_model_pipeline(model) -> Pipeline:
    return Pipeline(
        steps=[
            ("feature_engineering", FeatureEngineer()),
            ("log_transform", LogTransformer(columns=LOG_TRANSFORM_COLUMNS)),
            ("preprocess", build_preprocessor()),
            ("model", model),
        ]
    )


def save_model(model_pipeline, metadata: dict) -> None:
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model_pipeline, MODEL_PATH)
    METADATA_PATH.write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")


def load_model():
    return joblib.load(MODEL_PATH)
