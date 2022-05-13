from django.shortcuts import render
from .utils import *
# Create your views here.
from .models import Employee,Rooms,Reservations,Bookings,Employees_Model,Rooms_Model,Reservations_Model,Bookings_Model
from .serializers import EmployeeSerializer,RoomsSerializer,ReservationsSerializer,BookingsSerializer
from rest_framework.decorators import api_view 
from ninja import NinjaAPI
from ninja.security import HttpBasicAuth
import logging
from collections import defaultdict
 
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
loggings = logging.getLogger()
loggings.setLevel(logging.INFO)
class GlobalAuth(HttpBasicAuth):
    def authenticate(self,  request, username, password):
         
     
        if username == "admin" and password == "admin":
            return username
api = NinjaAPI(auth=GlobalAuth(),title="Meeting Room Reservations")

@api.get("/get_rooms",auth=GlobalAuth())
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

@api.post("/Cancel_Reservations")
def Cancel_Reservations(request, employee_email:str,from_date:str,end_date:str) :
        loggings.info(" Post Cancel_Reservations API is Called")
        emp_id=employee_email
        from_date= from_date 
        end_date= end_date 
        sa=Reservations.objects.raw('SELECT * FROM api_Reservations WHERE User_id  = %s AND from_date=%s AND end_date=%s ',[emp_id,from_date,end_date])
        all=[]
        k2=emp_id
        k1=None
        for i in sa: 
                k1=i.booking_id
            # k2=k2+","+i.invites
                #print(k1,k2)
        if k1!=None:
            loggings.info(" Reservations Made By This User is Found ")
            pa=Reservations.objects.raw('DELETE FROM api_Reservations WHERE booking_id=%s',[k1])
            try:
                for i in pa:
                        print(i)
            except:
                    pass
            
            pa=Bookings.objects.raw('DELETE FROM api_Bookings WHERE booking_id=%s',[k1])
            try:
                for i in pa:
                        print(i)
            except:
                    pass
            loggings.info(" Post Cancel_Reservations API is Sucessfull")
            return {"result":"Reservation Canceled Successfully"}
        else:
            loggings.info("No Reservations Made By This User is Found ")
            loggings.info(" Post Cancel_Reservations API is Sucessfull")
            return {"result":"No Meetings reserved with this user"} 

 