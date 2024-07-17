from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import uvicorn

model_path=r"D:\Surya files\DataScience\ML\Classification\SVM\breastCancerDetection\output\breast_cancer_model_detector.pkl"


with open(model_path,'rb') as file:
    model=pickle.load(file)
    

#defaining the fast api app
app=FastAPI()

#defining the input data model
class BreastCancerInputData(BaseModel):
    concave_points_worst: float
    perimeter_worst: float
    concave_points_mean: float
    radius_worst: float
    perimeter_mean: float
    area_worst: float
    radius_mean: float
    area_mean: float
    concavity_mean: float
    concavity_worst: float
    


@app.post("/predict")
def predict(data: BreastCancerInputData):
    #convert the input data into numpy array
    # input_data=np.array(data.features).reshape(1,-1)
    # Convert the input data to a numpy array
    input_data = np.array([data.concave_points_worst, data.perimeter_worst, data.concave_points_mean, 
                           data.radius_worst, data.perimeter_mean, data.area_worst, data.radius_mean, 
                           data.area_mean, data.concavity_mean, data.concavity_worst]).reshape(1, -1)
    
    #make prediction
    prediction=model.predict(input_data)
    result="Malignent" if prediction[0]==1 else "Bengin"
    
    return {"Prediction":result}


if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8090)
    

