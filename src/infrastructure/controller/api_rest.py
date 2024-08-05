from flask import Flask, request
from datetime import datetime
from src.domain.model.patient_model import Patient
from src.domain.use_case.patient_use_case import Patient_use_case
from src.infrastructure.adapters.patient_repository_adapters import Patient_repository_adapter

app = Flask(__name__)
patient_repository = Patient_repository_adapter()
patient_use_case = Patient_use_case(patient_repository)

@app.route("/api/add-patient", methods=["POST"])
def add_patient_api():
    data: dict = request.get_json()
    patient_data = Patient(
        name=data.get("name"),
        document=data.get("document"),
        date_of_birth=datetime.strptime(data.get("date_of_birth"), "%Y-%m-%d") if data.get("date_of_birth") else None,
        gender=data.get("gender"),
        blood_type=data.get("blood_type"),
        allergies=data.get("allergies")
    )
    response = patient_use_case.create_patient(patient_data)
    return {"response": response}

@app.route("/api/get-patient/<int:id>", methods=["GET"])
def get_patient_api(id: int):
    patient = patient_use_case.get_patient_by_id(id)
    return {"patient": patient}

@app.route("/api/update-patient", methods=["PUT"])
def update_patient_api():
    data: dict = request.get_json()
    patient_data = Patient(
        id=data.get("id"),
        name=data.get("name"),
        document=data.get("document"),
        date_of_birth=datetime.strptime(data.get("date_of_birth"), "%Y-%m-%d") if data.get("date_of_birth") else None,
        gender=data.get("gender"),
        blood_type=data.get("blood_type"),
        allergies=data.get("allergies")
    )
    response = patient_use_case.update_patient(patient_data)
    return {"response": response}

@app.route("/api/get-patients", methods=["GET"])
def get_patients_api():
    patients = patient_use_case.get_patients()
    return {"patients": patients}

@app.route("/api/delete-patient/<int:id>", methods=["DELETE"])
def delete_patient_api(id: int):
    patient_use_case.delete_patient(id)
    return {"message": "Patient deleted successfully"}

def page_not_found(e):
    return "<h1> The page you are trying to find does not exist </h1>" 



