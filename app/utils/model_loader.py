import joblib
import os

def load_model():
    model_path = os.path.join('../', 'models', 'success_prediction_model.joblib')
    loaded_model = joblib.load(model_path)
    return loaded_model
