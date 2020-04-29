from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm, remove_perm
from parents.models import Parent

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

