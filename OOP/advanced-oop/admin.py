from typing import Any, Dict
from user import User
from database import Database


class Admin(User):
    def __init__(self, username, password, access):
        super(Admin, self).__init__(username, password)
        self.access = access
        
    def __repr__(self) -> str:
        return f'<Admin {self.username} access {self.access}'
    
    def to_dict(self) -> Dict[str, Any]:
        return {'username': self.username,
                "password": self.password,
                "access": self.access}
        
    def save(self):
        Database.insert(self.to_dict())    