# Django Role-Based Authorization System

A robust Django REST API with JWT authentication and role-based authorization system. This project implements a secure and scalable user management system with different roles and permissions.

## Features

- 🔐 JWT Authentication
- 👥 Role-Based Access Control (RBAC)
- 🔑 Custom User Model
- 🛡️ Granular Permissions System
- 🌐 CORS Support
- ✉️ Email Configuration Ready
- 🔒 Environment Variables Support

## Role Hierarchy

The system includes three default roles:

1. **ADMIN**
   - Full system access
   - Can manage users, roles, and permissions
   - All CRUD operations available

2. **MANAGER**
   - Can view and update users
   - Limited administrative access

3. **USER**
   - Basic access rights
   - Can view user information

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mohitsharma012/AuthWithMe.git
   cd AuthWithMe
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` file with your configurations.

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication

- **Register**: `POST /api/register/`
  ```json
  {
    "email": "user@example.com",
    "username": "username",
    "password": "password",
    "password2": "password"
  }
  ```

- **Login**: `POST /api/login/`
  ```json
  {
    "email": "user@example.com",
    "password": "password"
  }
  ```

- **Refresh Token**: `POST /api/token/refresh/`
  ```json
  {
    "refresh": "your-refresh-token"
  }
  ```

### User Management

- **List Users**: `GET /api/users/`
- **Create User**: `POST /api/users/`
- **Get User**: `GET /api/users/{id}/`
- **Update User**: `PUT /api/users/{id}/`
- **Delete User**: `DELETE /api/users/{id}/`
- **Current User**: `GET /api/users/me/`
- **Available Roles**: `GET /api/users/roles/`

### Permissions

- **List Permissions**: `GET /api/permissions/`
- **Create Permission**: `POST /api/permissions/`
- **Get Permission**: `GET /api/permissions/{id}/`
- **Update Permission**: `PUT /api/permissions/{id}/`
- **Delete Permission**: `DELETE /api/permissions/{id}/`

### Role Permissions

- **List Role Permissions**: `GET /api/role-permissions/`
- **Assign Permission to Role**: `POST /api/role-permissions/`
- **Get Role Permission**: `GET /api/role-permissions/{id}/`
- **Update Role Permission**: `PUT /api/role-permissions/{id}/`
- **Delete Role Permission**: `DELETE /api/role-permissions/{id}/`

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. Include the token in the Authorization header:

```
Authorization: Bearer <your-access-token>
```

## Permission System

Permissions are managed through the `HasRolePermission` class. Available permissions:

- `create_user`
- `update_user`
- `delete_user`
- `view_user`
- `manage_permissions`
- `manage_roles`

## Environment Variables

Key environment variables to configure:

```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000

JWT_ACCESS_TOKEN_LIFETIME_MINUTES=60
JWT_REFRESH_TOKEN_LIFETIME_DAYS=7

DATABASE_URL=sqlite:///db.sqlite3

EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password
```

## Security Considerations

1. Always use HTTPS in production
2. Keep your SECRET_KEY secure
3. Set DEBUG=False in production
4. Configure proper CORS settings
5. Regularly update dependencies
6. Use strong passwords
7. Implement rate limiting for API endpoints

## Project Structure

```
├── core/                   # Project core settings
│   ├── settings.py        # Project settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── users/                 # Users app
│   ├── models.py         # User and permission models
│   ├── serializers.py    # API serializers
│   ├── views.py          # API views
│   ├── permissions.py    # Custom permissions
│   ├── roles.py          # Role definitions
│   └── urls.py           # Users app URLs
├── .env                  # Environment variables
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.