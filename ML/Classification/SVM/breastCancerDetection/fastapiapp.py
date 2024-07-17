from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np


model_path=r"D:\Surya files\DataScience\ML\Classification\SVM\breastCancerDetection\output\breast_cancer_model_detector.pkl"


with open(model_path,'rb') as file:
    model=pickle.load(file)
    

#defaining the fast api app
app=FastAPI()

#defining the input data model
class BreastCancerInputData(BaseModel):
    features:list[float]
    
    
