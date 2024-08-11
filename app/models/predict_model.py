import joblib
import pandas as pd
import os

def load_prediction_model():
    try:
        model_path = os.path.join('../../database', 'success_prediction_model.joblib')
        loaded_model = joblib.load(model_path)
        return loaded_model
    except Exception as e:
        raise e

def predict_success(input_series: dict):
    try:
        model = load_prediction_model()

        test_data = pd.DataFrame([input_series])

        predictions = model.predict(test_data)

        return int(predictions[0])
    except Exception as e:
        raise e