from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
from matplotlib import pyplot as plt
from app.services.preprocess import preprocess_data
from app.utils.logger import logger

def train_model(criterion):
    try:
        df = pd.read_csv("database/powerlifting-database/openpowerlifting.csv")
        features, target = preprocess_data(df)

        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

        class_tree = tree.DecisionTreeClassifier(criterion=criterion, max_depth=4, min_samples_leaf=4)
        class_tree.fit(X_train, y_train)

        fig, ax = plt.subplots(figsize=(8, 8))
        tree.plot_tree(class_tree, ax=ax, feature_names=features.columns)
        plt.close(fig)

        predictions = class_tree.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        logger.info(f"Predictions: {predictions}")
        logger.info(f"Accuracy: {accuracy}")

        return class_tree, accuracy
    except Exception as e:
        logger.error(f"Error: {e}")
        raise e
