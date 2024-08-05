
import psycopg2
from abc import ABC, abstractmethod
from typing import List
from src.domain.model.patient_model import Patient

class Patient_repository(ABC):
    
    @abstractmethod
    def create_patient_repository(self, patient: Patient) -> Patient:
        pass
    
    @abstractmethod
    def get_patient_by_id_repository(self, id_patient: int) -> Patient:
        pass

    @abstractmethod
    def update_patient_repository(self, patient: Patient) -> Patient:
        pass

    @abstractmethod
    def get_patients_repository(self) -> List[Patient]:
        pass

    @abstractmethod
    def delete_patient_repository(self, id_patient: int) -> None:
        pass
