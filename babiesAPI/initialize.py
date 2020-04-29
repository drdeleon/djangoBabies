from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm, remove_perm
from parents.models import Parent

user_parent_list = [
    {
        "username": "usuarioCinco",
        "name": "Papá Cuatro",
        "mail": "usuarioCuatro@user.com",
        "password": "usuarioCuatro",

    },
    {
        "username": "usuarioDos",
        "name": "Papá Dos",
        "mail": "usuarioDos@user.com",
        "password": "usuarioDos",
    },
    {
        "username": "usuarioTres",
        "name": "Papá Tres",
        "mail": "usuarioTres@user.com",
        "password": "usuarioTres",
    },
]

# for user in user_parent_list:
#     u = User(username=user['username'], email=user['mail'])
#     u.set_password(user['password'])
#     u.save()

#     p = Parent(user=u, name=user['name'])
#     p.save()


print('USERS:')
for usuario in User.objects.all():
    print(usuario.id, usuario)

print('PARENTS:')
for parent in Parent.objects.all():
    print(parent)

# u = User.objects.get(pk=7)
# print(u.username)

u = Parent.objects.get(name='Papá Dos')

for baby in u.baby_set.all():
    print(baby)



