from fastapi import FastAPI , Path , HTTPException , Query
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

@app.get("/")
def greet():
    return {"message" : "Patient Management System API"}

@app.get("/about")
def about():
    return {"message" :"A fully functional API to manage your patient records"}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/above_25_age")
def above_age():
    data = load_data()
    # return data
    result = {}

    for patient_id , patient in data.items():
        if patient["age"] >= 25:
            result[patient_id] = patient["name"]

    return result


#Path Parameter

@app.get("/patients/{patients_id}")
def view_patient(patients_id : str = Path(... , description = "ID of the patient in the DB" , example= "P001") ):
    data = load_data()
    if patients_id in data:
        return data[patients_id]
    else:
        # return {"error" : "patient not found"}
        raise HTTPException(status_code=404 , detail="Patient not found")


#Query Parameter

@app.get("/sort")
def sortpatients(sort_by:str = Query(..., description= "sort on the basis of hieght , weight or BMI"), order:str = Query('asc' , description= "sort in asc or desc order")):
    valid_fields = ["height" , "weight" , "BMI"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code= 400 , detail= f"Invalid Field , Select from {valid_fields}")
    
    if order not in ["asc" , "desc"]:
        raise HTTPException(status_code=400 , detail= "Invalid order , select between asc or desc")
                        
    data = load_data()
    
    sort_order = True if order=='desc' else False
    sorted_data = sorted(data.values() , key = lambda x:x.get(sort_by , 0) , reverse= sort_order)
    return sorted_data