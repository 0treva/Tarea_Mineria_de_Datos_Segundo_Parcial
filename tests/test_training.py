import json
from pathlib import Path

from src.config import METADATA_PATH, METRICS_PATH, MODEL_PATH
from src.train import run_training


def test_training_creates_artifacts():
    metrics = run_training()
    assert "best_experiment" in metrics
    assert MODEL_PATH.exists()
    assert METRICS_PATH.exists()
    assert METADATA_PATH.exists()

    saved_metrics = json.loads(Path(METRICS_PATH).read_text(encoding="utf-8"))
    assert "experiments" in saved_metrics
    assert len(saved_metrics["experiments"]) == 2
