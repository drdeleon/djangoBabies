from django.contrib.auth.models import User

user_list = [
    {
        "username": "usuarioUno",
        "mail": "usuarioUno@user.com",
        "password": "usuarioUno",
    },
    {
        "username": "usuarioDos",
        "mail": "usuarioDos@user.com",
        "password": "usuarioDos",
    },
    {
        "username": "usuarioTres",
        "mail": "usuarioTres@user.com",
        "password": "usuarioTres",
    },
    {
        "username": "usuarioCuatro",
        "mail": "usuarioCuatro@user.com",
        "password": "usuarioCuatro",
    },
]

for user in user_list:
    u = User(username=user['username'], mail=user['mail'])
    u.set_password(user['password'])
    u.save()