from django.shortcuts import render
from .utils import *
# Create your views here.
from .models import Employee,Rooms,Reservations,Bookings,Employees_Model,Rooms_Model,Reservations_Model,Bookings_Model
from .serializers import EmployeeSerializer,RoomsSerializer,ReservationsSerializer,BookingsSerializer
from rest_framework.decorators import api_view 
from ninja import NinjaAPI
from ninja.security import HttpBearer
import logging
from collections import defaultdict
 
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
def get_rooms(request) :

    loggings.info("Get Rooms API called")
        
    res = view_rooms()

    loggings.info("Get Rooms API is Sucessfull")
         
    return {"result":res}

@api.get("/get_employee")
def get_employee( request) :
    loggings.info("Get Employee API called")
    
    res = view_employees()
        
    loggings.info("Get Employee API is Sucessfull")
        
    return {"result":res}

@api.post("/post_rooms")
def post_rooms( request,Item:Rooms_Model) :
     
        loggings.info(" Post Rooms API called")
        num = Item.room_no
        
        check = add_room(num)
        
        output = ""
        if check:    
            output="Room "+str(num)+" is created"
        else:
            output="Room "+str(num)+" already exists"
        loggings.info(" Post Rooms API is Sucessfull")
        return {"result":output}

@api.post("/post_employee")
def post_employee( request,Item:Employees_Model) :
        loggings.info(" Post Employee API called")
        
        email=Item.email
        name=Item.name
        check = add_employee(email,name) 
        output=""
        if check:
            output="Employee "+str(name)+" is created"
        else:
            output="Employee "+str(name)+" already exists"
        loggings.info(" Post Employee API is Sucessfull")
        return {"result":output}


@api.post("/filter_reservation_by_employees")
def filter_employee(request, employee_email:str) :
 
        loggings.info("Post Filter Employee API is Called")
        emp_id=employee_email
        all = filter(emp_id) 
        if not all:

            loggings.info("No Reservations made by this employee or he is not the host of the meet")
            all = "No Reservations made by this employee "

        loggings.info(" Post Filter Employee is Sucessfull")
       
        return {"result":all}

@api.post("/reserve_room")
def reserve_room( request,Item:Reservations_Model) :
    
    loggings.info("Post Reservations  API is Called")
    emp_id=Item.User_id
    title=Item.title
    from_time=Item.from_date 
    end_time=Item.end_date 
    invites=Item.invites
        
    res = reserve(emp_id,title,from_time,end_time,invites)
            
    return {"result":res}