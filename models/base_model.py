"""Ce module contient la classe de base des modèles de l'application."""
import models
import uuid
from datetime import datetime
import time

class BaseModel:
    """
    Cette classe définit toutes les méthodes communs aux autres classes
    This class defines all common methods or attributes for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initialisation de la classe de base."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "created_at":
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    setattr(self, key, value)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()
        
    def to_dict(self):
        """to_dict method"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict                  

    def __str__(self):
        """String representation of the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)