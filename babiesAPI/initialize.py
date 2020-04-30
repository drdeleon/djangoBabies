from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm, remove_perm
from parents.models import Parent

user_parent_list = [
    {
        "username": "usuarioUno",
        "name": "usuarioUno",
        "mail": "usuarioUno@user.com",
        "password": "usuarioUno",

    },
    {
        "username": "usuarioDos",
        "name": "usuarioDos",
        "mail": "usuarioDos@user.com",
        "password": "usuarioDos",
    },
    {
        "username": "usuarioTres",
        "name": "usuarioTres",
        "mail": "usuarioTres@user.com",
        "password": "usuarioTres",
    },
]

for user in user_parent_list:
    u = User(username=user['username'], email=user['mail'])
    u.set_password(user['password'])
    u.save()

    p = Parent(user=u, name=user['name'])
    p.save()
    print(p)


