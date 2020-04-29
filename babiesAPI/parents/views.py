# from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from guardian.shortcuts import assign_perm, remove_perm

# from permissions.services import APIPermissionClassFactory
from parents.models import Parent
from parents.serializers import ParentSerializer
from permissions.services import APIPermissionClassFactory


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    permission_classes = (
        APIPermissionClassFactory(
            name='BabyPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': 'parents.view_parent',
                    'destroy': False,
                    'update': True,
                    'partial_update': 'change_parent',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        baby = serializer.save()
        user = self.request.user
        assign_perm('parents.change_parent', user, baby)
        assign_perm('parents.view_parent', user, baby)
        return Response(serializer.data)