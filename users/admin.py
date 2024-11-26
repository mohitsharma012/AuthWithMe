from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Permission, RolePermission

admin.site.register(User, UserAdmin)
admin.site.register(Permission)
admin.site.register(RolePermission)