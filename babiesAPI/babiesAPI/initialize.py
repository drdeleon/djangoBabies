from django.contrib.auth.models import User

users = [
    {
    "username": "usuarioUno",
    "email": "usuarioUno@user.com",
    "password": "userUnoPassword"
    },  
    {
    "username": "usuarioDos",
    "email": "usuarioDos@user.com",
    "password": "userDosPassword"
    },
    {
    "username": "usuarioTres",
    "email": "usuarioTres@user.com",
    "password": "userTresPassword"
    },
]

for user in users:
    new_user = User(username=user['username'], email=user['email'])
    new_user.set_password(user['password'])

