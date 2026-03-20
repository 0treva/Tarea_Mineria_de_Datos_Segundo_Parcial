import argparse
import json
from pathlib import Path

import pandas as pd

from src.config import METADATA_PATH, REQUIRED_FEATURES
from src.preprocessing import load_model, prepare_features_dataframe


def validate_payload(payload: dict) -> tuple[bool, list[str]]:
    missing = [feature for feature in REQUIRED_FEATURES if feature not in payload]
    return (len(missing) == 0, missing)


def payload_to_frame(payload: dict) -> pd.DataFrame:
    is_valid, missing = validate_payload(payload)
    if not is_valid:
        raise ValueError(f"Faltan variables requeridas: {missing}")

    frame = pd.DataFrame([payload])
    frame = prepare_features_dataframe(frame)
    return frame


def predict_from_payload(payload: dict, model=None) -> float:
    model = model or load_model()
    frame = payload_to_frame(payload)
    prediction = model.predict(frame)[0]
    return float(prediction)


def load_metadata() -> dict:
    return json.loads(Path(METADATA_PATH).read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description="Realiza una predicción a partir de un JSON.")
    parser.add_argument("--json_path", type=str, required=True, help="Ruta de un archivo JSON con las variables de entrada.")
    args = parser.parse_args()

    payload = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
    prediction = predict_from_payload(payload)
    print(json.dumps({"prediction": prediction}, ensure_ascii=False))


if __name__ == "__main__":
    main()
