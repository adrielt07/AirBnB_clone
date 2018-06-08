#!/usr/bin/python3
"""
BaseModel that defines all common attributes/methods for other classes
"""


class BaseModel:
    """
    BaseModel Class
    """
    def __init__(self, *args, **kwargs):
        """
        creates uuid specific for each instance
        """
        from datetime import datetime
        import uuid

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value,"%Y-%m-%dT%H:%M:%S.%f"))
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def save(self):
        """updates time - last time instance object is modified"""
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        """
        returns a new copy of dictionary
        added '__class__' key
        Updated time to isoformat
        """
        from datetime import datetime, date, time
        new = self.__dict__.copy()
        new['__class__'] = type(self).__name__
        new['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        new['updated_at'] = datetime.isoformat(self.updated_at)
        return new

    def __str__(self):
        """Prints Classname, instance id, and dictionary"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)
