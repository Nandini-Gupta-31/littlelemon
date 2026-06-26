Little Lemon Backend Capstone Project

API Endpoints

Home Page
http://127.0.0.1:8000/restaurant/

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