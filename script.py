import mlflow
import mlflow.sklearn
from sklearn import tree 
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plot
import pandas as pd

file = pd.read_csv("powerlifting-database/openpowerlifting.csv")

def train_model(criterion):
	iris = load_iris()

	attributes = iris.data 
	labels = iris.target

	X_train, X_test, y_train, y_test = train_test_split(attributes, labels, test_size=0.2, random_state=42)

	class_tree = tree.DecisionTreeClassifier(criterion=criterion, max_depth=4, min_samples_leaf=4)
	class_tree.fit(attributes, labels)

	figure, axis = plot.subplots(figsize=(6,6))
	tree.plot_tree(class_tree, ax = axis, feature_names=["sepal length", "sepal width", "petal length", "petal width"])
	plot.show() 

	predictions = class_tree.predict([[5, 3.5, 1.3, 1.3]])
	accuracy = accuracy_score(42, predictions)
	print(predictions)

	return model, accuracy

def log_model(model, accuracy, criterion):
	with mlflow.start_run():
		mlflow.log_param("criterion", criterion)
		mlflow.log_metric("accuracy", accuracy)
		mlflow.sklearn.log_model(model, "model")
		print(f"Model with criterion={criterion} and accuracy={accuracy} logged.")

def main(criterion="entropy"):
	model, accuracy = train_model(criterion)
	log_model(model, accuracy, criterion)

if __name__ == "__main__":
	main()