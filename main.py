from fastapi import FastAPI , Path , HTTPException
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

@app.get("/patients/{patients_id}")
def view_patient(patients_id : str = Path(... , description = "ID of the patient in the DB" , example= "P001") ):
    data = load_data()
    if patients_id in data:
        return data[patients_id]
    else:
        # return {"error" : "patient not found"}
        raise HTTPException(status_code=404 , detail="Patient not found")


