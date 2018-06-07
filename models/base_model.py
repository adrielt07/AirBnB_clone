#!/usr/bin/python3
"""
BaseModel that defines all common attributes/methods for other classes
"""
import datetime

class BaseModel:
    """
    BaseModel Class
    """
    def __init__(self):
        import uuid
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()

    def save(self):
        self.update_at = datetime.datetime.today()

    def to_dict(self):
        from datetime import datetime, date, time
        new = self.__dict__.copy()
        new['__class__'] = type(self).__name__
        new['created_at'] = datetime.isoformat(self.created_at)
        new['updated_at'] = datetime.isoformat(self.updated_at)
        return new

    def __str__(self):
        print("[{}] ({}) {}".format(type(self).__name__,
                                    self.id, self.__dict__))
