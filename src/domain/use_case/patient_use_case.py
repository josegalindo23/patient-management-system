from typing import List
from src.domain.repository.patient_interface_repository import Patient_repository
from src.domain.model.patient_model import Patient

class Patient_use_case:
    def __init__(self, patient_repository: Patient_repository): 
        self.patient_repository = patient_repository

    def create_patient(self, patient: Patient) -> Patient:
        return self.patient_repository.create_patient_repository(patient)
    
    def get_patient_by_id(self, id: int) -> Patient:
        return self.patient_repository.get_patient_by_id_repository(id)
    
    def update_patient(self, patient: Patient) -> Patient:
        return self.patient_repository.update_patient_repository(patient)
    
    def get_patients(self) -> List[Patient]:
        return self.patient_repository.get_patients_repository()
    
    def delete_patient(self, id: int) -> None:
        return self.patient_repository.delete_patient_repository(id)