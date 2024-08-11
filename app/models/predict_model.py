import joblib
import pandas as pd
import os

def load_prediction_model():
    try:
        model_path = os.path.join(os.path.dirname(__file__), '../..', 'database', 'success_prediction_model.joblib')
        
        loaded_model = joblib.load(model_path)
        
        return loaded_model
    except Exception as e:
        raise e

def predict_success(input_series: dict):
    try:
        model = load_prediction_model()

        input_series_renamed = {
            "category": input_series["category"],
            "size": input_series["size"],
            "type": input_series["type"],
            "price": input_series["price"],
            "content rating": input_series["content_rating"],
            "genres": input_series["genres"],
            "current ver": input_series["current_ver"],
            "android ver": input_series["android_ver"],
            "sentiment": input_series["sentiment"],
        }

        test_data = pd.DataFrame([input_series_renamed])

        predictions = model.predict(test_data)

        return int(predictions[0])
    except Exception as e:
        raise e