import json
import numpy as np
import pandas as pd
import joblib
from azureml.core.model import Model

MODEL_NAME = 'german-credit-local-model'

def init():
    global model
    model_path = Model.get_model_path(MODEL_NAME)
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = pd.read_json(raw_data)
        input_df = pd.DataFrame.from_dict(data)
        proba = model.predict_proba(input_df)
        result = {"predict_proba":proba.tolist()}
        return result
    except Exception as e:
        error = str(e)
        return error