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

# Running the Applications

## Train Decision Tree Model

### To start the training application, run:

```bash
python train_decision_tree.py
```

### This will start a FastAPI server on endpoint:

http://localhost:8000/api/v1/train

### Send a POST request with the following in the request body in json format:

```bash
{
   "criterion": "gini"
}
```

## To Load Decision Tree Model, run:

```bash
python load_model.py
```

### This will start a FastAPI server on endpoint:

http://localhost:8000/api/v1/load (POST)

### Send a POST request with the following in the request body in json format:

```bash
{
   "run_id": "your_run_id_here"
}
```
