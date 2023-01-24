from django.contrib.auth.models import User
from .models import MenuItem, Booking
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['title', 'price', 'inventory']

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ['name', 'no_of_guests', 'bookingdate']
