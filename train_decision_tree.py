from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mlflow
import mlflow.sklearn
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
from matplotlib import pyplot as plt
import logging

mlflow.set_tracking_uri("http://127.0.0.1:5000")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class TrainModelRequest(BaseModel):
    criterion: str

def preprocess_data(df):
    df = df.dropna()
    features = df[["BodyweightKg", "BestSquatKg", "BestBenchKg", "BestDeadliftKg"]]
    target = df["Place"]
    
    target = target.apply(lambda x: 1 if x == "1" else 0)
    
    return features, target

def train_model(criterion):
    try:
        df = pd.read_csv("powerlifting-database/openpowerlifting.csv")
        features, target = preprocess_data(df)

        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

        class_tree = tree.DecisionTreeClassifier(criterion=criterion, max_depth=4, min_samples_leaf=4)
        class_tree.fit(X_train, y_train)

        fig, ax = plt.subplots(figsize=(8, 8))
        tree.plot_tree(class_tree, ax=ax, feature_names=features.columns)
        plt.show()
        plt.savefig("tree_plot.png")
        plt.close(fig)

        predictions = class_tree.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        logger.info(f"Predictions: {predictions}")
        logger.info(f"Accuracy: {accuracy}")

        return class_tree, accuracy
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

def log_model(model, accuracy, criterion):
    try:
        with mlflow.start_run():
            mlflow.log_param("criterion", criterion)
            mlflow.log_metric("accuracy", accuracy)
            mlflow.sklearn.log_model(model, "model")
            print(f"Model with criterion={criterion} and accuracy={accuracy} logged.")
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/train")
def train(request: TrainModelRequest):
    try:
        model, accuracy = train_model(request.criterion)
        log_model(model, accuracy, request.criterion)
        return {"criterion": request.criterion, "accuracy": accuracy}
    except HTTPException as e:
        logger.error(f"Error: {str(e.detail)}")
        raise e
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)