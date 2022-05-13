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

@api.get("/get_rooms")
def get_rooms( request) :
        loggings.info("Get Rooms API called")
        
        sql_raw=Rooms.objects.raw('SELECT * FROM api_Rooms')
        res=[]
        for k in sql_raw:
            res.append(k.room_no)
        loggings.info("Get Rooms API is Sucessfull")
         
        return {"result":res}

@api.get("/get_employee")
def get_employee( request) :
        loggings.info("Get Employee API called")
        
        sql_raw=Employee.objects.raw('SELECT  *  FROM api_Employee ')
        res=[]
        for k in sql_raw:
           res.append([k.id,k.name,k.email])
        loggings.info("Get Employee API is Sucessfull")
        
        return {"result":res}

@api.post("/post_rooms")
def post_rooms( request,Item:Rooms_Model) :
     
        loggings.info(" Post Rooms API called")
        
        num = Item.room_no
        sql_raw=Rooms.objects.raw('INSERT INTO api_Rooms (room_no )  VALUES (%s )', [num])
        try:
            for k in sql_raw:
                pass
        except:
            pass   
        output="Room "+str(num)+" is created"

        loggings.info(" Post Rooms API is Sucessfull")
        return {"result":output}