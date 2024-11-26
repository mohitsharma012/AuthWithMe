from django.contrib.auth.models import AbstractUser
from django.db import models
from .roles import Role

class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices(),
        default=Role.USER.value
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_role_permission(self, permission: str) -> bool:
        from .roles import RolePermissions
        return permission in RolePermissions.get_permissions(self.role)

class Permission(models.Model):
    name = models.CharField(max_length=100)
    codename = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class RolePermission(models.Model):
    role = models.CharField(max_length=20, choices=Role.choices())
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('role', 'permission')