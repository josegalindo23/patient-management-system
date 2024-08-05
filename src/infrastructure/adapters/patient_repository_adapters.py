from src.domain.model.patient_model import Patient
from src.domain.repository.patient_interface_repository import Patient_repository
from src.infrastructure.adapters.data_sources.entities.patient_entity import Patient_entity
from src.infrastructure.adapters.data_sources.db_config import db

class Patient_repository_adapter(Patient_repository):
    def create_patient_repository(self, patient: Patient) -> Patient:
        try:
            db_patient = Patient_entity(
                id=patient.id,
                name=patient.name,
                document=patient.document,
                date_of_birth=patient.date_of_birth,
                gender=patient.gender,
                blood_type=patient.blood_type,
                allergies=patient.allergies,
            )
            db.add(db_patient)
            db.commit()
            return Patient(
                id=db_patient.id,
                name=db_patient.name,
                document=db_patient.document,
                date_of_birth=db_patient.date_of_birth,
                gender=patient.gender,
                blood_type=db_patient.blood_type,
                allergies=db_patient.allergies,
            ).to_dict()
        except Exception as e:
            raise NameError(f"An error occurred creating the patient, check {e}")
        
    def get_patient_by_id_repository(self, patient_id: int) -> Patient:
        try:
            db_patient = (
                db.query(Patient_entity)
                .filter(Patient_entity.id == patient_id)
                .first()
            )
            if db_patient is not None:
                return Patient(
                    id=db_patient.id,
                    name=db_patient.name,
                    document=db_patient.document,
                    date_of_birth=db_patient.date_of_birth,
                    gender=db_patient.gender,
                    blood_type=db_patient.blood_type,
                    allergies=db_patient.allergies,
                ).to_dict()
            return None
        except Exception as e:
            raise NameError(f"An error occurred getting the patient, check {e}")

    def update_patient_repository(self, patient: Patient) -> Patient:
        try: 
            db_patient = (
                db.query(Patient_entity)
                .filter(Patient_entity.id == patient.id)
                .first()
            )
            db_patient.name = patient.name
            db_patient.document = patient.document
            db_patient.date_of_birth = patient.date_of_birth
            db_patient.gender = patient.gender
            db_patient.blood_type = patient.blood_type
            db_patient.allergies = patient.allergies
            db.commit()
            return Patient(
                id=db_patient.id,
                name=db_patient.name,
                document=db_patient.document,
                date_of_birth=db_patient.date_of_birth,
                gender=db_patient.gender,
                blood_type=db_patient.blood_type,
                allergies=db_patient.allergies,
            ).to_dict()
        except Exception as e:
            raise NameError(f"An error occurred updating the patient, check {e}")
        
    def get_patients_repository(self) -> list[Patient]:
        try:
            db_patients = db.query(Patient_entity).all()
            return [
                Patient(
                    id=patient.id,
                    name=patient.name,
                    document=patient.document,
                    date_of_birth=patient.date_of_birth,
                    gender=patient.gender,
                    blood_type=patient.blood_type,
                    allergies=patient.allergies,
                ).to_dict()
                for patient in db_patients
            ]
        except Exception as e:
            raise NameError(f"An error occurred getting the patients, check {e}")
        
    def delete_patient_repository(self, patient_id: int) -> None:
        try:
            db_patient = (
                db.query(Patient_entity)
                .filter(Patient_entity.id == patient_id)
                .first()
            )
            db.delete(db_patient)
            db.commit()
        except Exception as e:
            raise NameError(f"An error occurred while deleting the patient, check {e}")