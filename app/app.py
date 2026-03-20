from pathlib import Path
import sys

from flask import Flask, jsonify, request

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.predict import predict_from_payload
from src.preprocessing import load_model


app = Flask(__name__)
MODEL = load_model()


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.post("/predict")
def predict():
    try:
        payload = request.get_json(silent=True)
        if payload is None:
            return jsonify({"error": "El cuerpo de la petición debe ser JSON válido."}), 400

        prediction = predict_from_payload(payload, model=MODEL)
        return jsonify({"prediction": prediction}), 200

    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    except TypeError as exc:
        return jsonify({"error": f"Tipo de dato inválido: {exc}"}), 400
    except Exception as exc:
        return jsonify({"error": f"Error interno del servidor: {exc}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
