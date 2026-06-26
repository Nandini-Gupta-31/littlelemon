Little Lemon Backend Capstone Project

Developer: Nandini Gupta

Project Description
-------------------
This project is a Django REST Framework backend application for the Little Lemon Restaurant.

Features:
- Django Templates and Static Files
- MySQL Database
- Menu API (CRUD)
- Table Booking API
- Djoser User Registration
- Token Authentication
- Django Admin Panel
- Unit Tests
- Tested using Insomnia REST Client


API Endpoints

Home Page
http://127.0.0.1:8000/restaurant/

Admin Panel
http://127.0.0.1:8000/admin/

Browsable Menu API
GET / POST
http://127.0.0.1:8000/restaurant/menu/

Single Menu Item
GET / PUT / DELETE
http://127.0.0.1:8000/restaurant/menu/<id>/

Protected Booking API
http://127.0.0.1:8000/restaurant/booking/tables/

Protected Message API
http://127.0.0.1:8000/restaurant/message/

Generate Authentication Token
POST
http://127.0.0.1:8000/restaurant/api-token-auth/

Register User
POST
http://127.0.0.1:8000/auth/users/

Login
POST
http://127.0.0.1:8000/auth/token/login/

Logout
POST
http://127.0.0.1:8000/auth/token/logout/

Menu API
GET     /restaurant/menu/
POST    /restaurant/menu/
GET     /restaurant/menu/<id>/
PUT     /restaurant/menu/<id>/
DELETE  /restaurant/menu/<id>/

Booking API
GET     /restaurant/booking/tables/
POST    /restaurant/booking/tables/

Authentication
POST    /restaurant/api-token-auth/
POST    /auth/users/
POST    /auth/token/login/
POST    /auth/token/logout/

Protected API
GET     /restaurant/message/

Run Unit Tests
python manage.py test

Requirements
- Python
- MySQL
- Django
- Django REST Framework
- Djoser

Setup
1. Install dependencies
   pip install django djangorestframework djoser mysqlclien
2. Configure MySQL
3. Run migrations:
   python manage.py migrate
4. Start server:
   python manage.py runserver

Run tests:
python manage.py test

The project APIs have been verified using:
- Django REST Framework Browsable API
- Insomnia REST Client

GitHub Repository
=========================================

Repository:
https://github.com/Nandini-Gupta-31/littlelemon