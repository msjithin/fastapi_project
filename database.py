from typing import List 
from models import Item, User, uuid4, Gender, Role
    
items = []

db: List[User] = [
    User(
         first_name = "James", 
         last_name = "Roger", 
         gender = Gender.female,
         roles = [Role.student]),
    User(
         first_name = "Alex", 
         last_name = "Jones", 
         gender = Gender.male,
         roles = [Role.admin, Role.user])
]

fake_db = {
    "tim": {
        "username": "tim",
        "full_name": "Tim Rogers",
        "email": "timrogers@gmail.com",
        "hashed_password": "$2b$12$VNuiMp84WzhhvIuOtPT9XeT86SGX61PFwzryEVdG1Kz/fkAxRXtMW",
        "disabled": False
    }
}

