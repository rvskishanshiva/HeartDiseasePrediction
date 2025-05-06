from django.shortcuts import render
import pickle
import os
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



def home(request):
    return render(request,'home.html') 

@csrf_exempt
def predict(request):
    
    PICKLE_FILE_PATH = os.path.join(settings.BASE_DIR, "predict/model_files/model_and_scaler.pkl")

    with open(PICKLE_FILE_PATH, "rb") as f:
        loaded_data = pickle.load(f)
        model = loaded_data["model"] 
        scaler = loaded_data["scaler"]
    
    Age = int(request.POST["Age"])
    Gender =int(request.POST["Gender"])
    HeartRate = int(request.POST["HeartRate"])
    SystolicBloodPressure = int(request.POST["SystolicBloodPressure"])
    DiastolicBloodPressure = int(request.POST["DiastolicBloodPressure"])
    BloodSugar = int(request.POST["BloodSugar"])
    CKMB = float(request.POST["CK-MB"])
    Troponin = float(request.POST["Troponin"])
   
    
    list=[[Age,Gender,HeartRate, SystolicBloodPressure, DiastolicBloodPressure, BloodSugar,CKMB,Troponin]]
    
    input = scaler.transform(list)
    prediction =  model.predict(input)
    
    return render(request,'home.html',{'prediction':prediction})