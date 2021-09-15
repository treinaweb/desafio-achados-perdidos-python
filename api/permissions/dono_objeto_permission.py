from rest_framework import permissions


class DonoObjetoPermission(permissions.BasePermission):
    message = 'Você não possui permissão para acessar este dado'

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj.local.usuario