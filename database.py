from typing import List 
from models import Item, User, uuid4, Gender, Role
    


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
