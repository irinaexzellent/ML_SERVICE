import io
from typing import List

import joblib

import numpy as np
import pandas as pd
from pydantic import BaseModel

from fastapi import FastAPI


class Model(BaseModel):
    X: List[str]


app = FastAPI()

loaded_model = joblib.load('model.pkl')


@app.post('/predict')
@app.get('/predict')
def predict_model(model: Model):
    string_data = """datetime,Accelerometer1RMS,Accelerometer2RMS,Current,Pressure,Temperature,Thermocouple,Voltage,Volume Flow RateRMS
    """ + '\r\n'.join(model.X)
    df = pd.read_csv(io.StringIO(string_data), sep=',', index_col='datetime')
    result = loaded_model.predict(df)
    return {"result": ','.join(map(str, result))}


def main():
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)


if __name__ == '__main__':
    main()



