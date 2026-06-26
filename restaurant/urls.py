from django.urls import path
from . import views
from .views import MenuView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='home'),

    path('menu/', MenuView.as_view(), name='menu'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='single-menu'),

    path('message/', views.msg, name='message'),
    
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
 ##   path('booking/', BookingView.as_view(), name='booking'),
]