from enum import Enum
from typing import List, Dict

class Role(str, Enum):
    ADMIN = 'ADMIN'
    MANAGER = 'MANAGER'
    USER = 'USER'

    @classmethod
    def choices(cls) -> List[tuple]:
        return [(role.value, role.value) for role in cls]

    @classmethod
    def values(cls) -> List[str]:
        return [role.value for role in cls]

class RolePermissions:
    PERMISSIONS: Dict[Role, List[str]] = {
        Role.ADMIN: [
            'create_user',
            'update_user',
            'delete_user',
            'view_user',
            'manage_permissions',
            'manage_roles',
        ],
        Role.MANAGER: [
            'update_user',
            'view_user',
        ],
        Role.USER: [
            'view_user',
        ]
    }

    @classmethod
    def get_permissions(cls, role: Role) -> List[str]:
        return cls.PERMISSIONS.get(role, [])