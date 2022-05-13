from django.shortcuts import render

# Create your views here.
from .models import Employee,Rooms,Reservations,Bookings,Employees_Model,Rooms_Model,Reservations_Model,Bookings_Model
from .serializers import EmployeeSerializer,RoomsSerializer,ReservationsSerializer,BookingsSerializer
from rest_framework.decorators import api_view 
from ninja import NinjaAPI
from ninja.security import HttpBearer
import logging
 
 
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
loggings = logging.getLogger()
loggings.setLevel(logging.INFO)
class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        if token == "1":
            return token
api = NinjaAPI(auth=GlobalAuth(),title="Meeting Room Reservations")
