from datetime import datetime

class Patient:
    def __init__(
            self,
            name: str,
            document: str,
            blood_type: str,
            id: int =None,
            date_of_birth: datetime = None,
            gender: str = None,
            allergies: str = None,
    ):
        self.id = id
        self.name = name
        self.document = document
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.blood_type = blood_type
        self.allergies = allergies
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "document": self.document,
            "date_of_birth": str(self.date_of_birth) if self.date_of_birth else None,
            "gender": self.gender,
            "blood_type": self.blood_type,
            "allergies": self.allergies,
        }
     