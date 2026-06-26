from django.shortcuts import render
from rest_framework import generics
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


def index(request):
    return render(request, 'index.html', {})

# Menu API (GET all, POST)
class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# Single Menu Item API (GET one, PUT, PATCH, DELETE)
class SingleMenuItemView(
    generics.RetrieveUpdateAPIView,
    generics.DestroyAPIView
):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

## class BookingView(generics.ListCreateAPIView):
  #  queryset = Booking.objects.all()
   # serializer_class = BookingSerializer
   # permission_classes = [IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})    