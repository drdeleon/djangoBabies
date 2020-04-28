# from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# from permissions.services import APIPermissionClassFactory
from babies.models import Baby
from babies.serializers import BabySerializer


class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer

    # permission_classes = (
    #     APIPermissionClassFactory(
    #         name='BabyPermission',
    #         permission_configuration={
    #             'base': {
    #                 'create': True,
    #                 'list': True,
    #             },
    #             'instance': {
    #                 'retrieve': 'babies.view_baby',
    #                 'destroy': False,
    #                 'update': True,
    #                 # 'update_permissions': 'users.add_permissions'
    #                 # 'archive_all_students': phase_user_belongs_to_school,
    #                 # 'add_clients': True,
    #             }
    #         }
    #     ),
    # )