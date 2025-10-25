from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True


user_data = {
    "id": 1,
    "username": "zara",
    "email": "zara.bond@gmail.com"
}

invalid_user_data = {
    "id": "1",
    "username": "zara",
    "email": "zara.bond@gmail.com"
}

user = User(**user_data)

try:
    invalid_user = User(**invalid_user_data)
except Exception as error:
    print("ОШибка валидации: ", error)
