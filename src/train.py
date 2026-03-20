import argparse
import json

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from src.config import (
    DATA_PATH,
    METADATA_PATH,
    METRICS_PATH,
    MODEL_CANDIDATES,
    REQUIRED_FEATURES,
    TARGET_COLUMN,
)
from src.preprocessing import build_model_pipeline, load_dataset, prepare_features_dataframe, save_model


def evaluate_regression(y_true, y_pred) -> dict:
    rmse = float(np.sqrt(mean_squared_error(y_true, y_pred)))
    mae = float(mean_absolute_error(y_true, y_pred))
    r2 = float(r2_score(y_true, y_pred))
    return {"rmse": rmse, "mae": mae, "r2": r2}


def run_training(data_path: str = str(DATA_PATH)) -> dict:
    df = load_dataset(data_path)
    df = df[df[TARGET_COLUMN].notna()].copy()

    X = prepare_features_dataframe(df)
    y = pd.to_numeric(df[TARGET_COLUMN], errors="coerce")

    metrics = {"dataset_rows_after_target_drop": int(len(df)), "experiments": {}}
    best_experiment_name = None
    best_r2 = float("-inf")
    best_pipeline = None
    best_split = None

    for experiment_name, test_size in MODEL_CANDIDATES.items():
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )

        pipeline = build_model_pipeline(LinearRegression())
        pipeline.fit(X_train, y_train)
        predictions = pipeline.predict(X_test)

        experiment_metrics = evaluate_regression(y_test, predictions)
        experiment_metrics["train_rows"] = int(len(X_train))
        experiment_metrics["test_rows"] = int(len(X_test))
        experiment_metrics["test_size"] = float(test_size)
        metrics["experiments"][experiment_name] = experiment_metrics

        if experiment_metrics["r2"] > best_r2:
            best_r2 = experiment_metrics["r2"]
            best_experiment_name = experiment_name
            best_pipeline = pipeline
            best_split = {"train_rows": int(len(X_train)), "test_rows": int(len(X_test)), "test_size": float(test_size)}

    metadata = {
        "best_experiment": best_experiment_name,
        "required_features": REQUIRED_FEATURES,
        "target_column": TARGET_COLUMN,
        "best_split": best_split,
    }

    metrics["best_experiment"] = best_experiment_name
    save_model(best_pipeline, metadata)
    METRICS_PATH.write_text(json.dumps(metrics, indent=2, ensure_ascii=False), encoding="utf-8")
    return metrics


def main():
    parser = argparse.ArgumentParser(description="Entrena y serializa el modelo de regresión.")
    parser.add_argument("--data_path", type=str, default=str(DATA_PATH))
    args = parser.parse_args()

    metrics = run_training(args.data_path)
    print(json.dumps(metrics, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
