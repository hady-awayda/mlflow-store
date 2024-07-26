from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import mlflow
import mlflow.sklearn
from sklearn import tree 
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plot
import pandas as pd

# file = pd.read_csv("powerlifting-database/openpowerlifting.csv")

app = FastAPI()

class TrainModelRequest(BaseModel):
	criterion: str

def train_model(criterion):
	iris = load_iris()

	attributes = iris.data 
	labels = iris.target

	X_train, X_test, y_train, y_test = train_test_split(attributes, labels, test_size=0.2, random_state=42)

	class_tree = tree.DecisionTreeClassifier(criterion=criterion, max_depth=4, min_samples_leaf=4)
	class_tree.fit(attributes, labels)

	figure, axis = plot.subplots(figsize=(10,10))
	tree.plot_tree(class_tree, ax = axis, feature_names=["sepal length", "sepal width", "petal length", "petal width"])
	plot.show() 

	predictions = class_tree.predict(X_test)
	accuracy = accuracy_score(y_test, predictions)
	print(predictions)

	return model, accuracy

def log_model(model, accuracy, criterion):
	with mlflow.start_run():
		mlflow.log_param("criterion", criterion)
		mlflow.log_metric("accuracy", accuracy)
		mlflow.sklearn.log_model(model, "model")
		print(f"Model with criterion={criterion} and accuracy={accuracy} logged.")

@app.post("/train")
def train(request: TrainModelRequest):
	model, accuracy = train_model(request.criterion)
	log_model(model, accuracy, criterion)
	return {"criterion": request.criterion, "accuracy": accuracy}

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=8001)