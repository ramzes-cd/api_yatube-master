from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение на уровне объектов, позволяющее редактировать объект только
    его автору.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешить чтение для всех запросов
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить запись только автору объекта
        return obj.author == request.user
