# MLFlow FastAPI Example

This repository contains two FastAPI applications for training and loading machine learning models using MLFlow.

## Setup

1. Install dependencies:

   ```bash
   pip install fastapi uvicorn mlflow scikit-learn matplotlib pydantic
   ```

2. Start the MLFlow server:
   ```bash
   mlflow ui
   ```

## Running the Applications

### Train Decision Tree Model

## To start the training application, run:

```bash
python train_decision_tree.py
```

This will start a FastAPI server on http://0.0.0.0:8001

# Endpoint

http://0.0.0.0:8001/train (POST)

# Request Body (json):

{
"criterion": "gini"
}

## To start the loading application, run:

```bash
python load_model.py
```

This will start a FastAPI server on http://0.0.0.0:8002

# Endpoint

http://0.0.0.0:8002/load (POST)

# Request Body (json):

{
"run_id": "your_run_id_here"
}
