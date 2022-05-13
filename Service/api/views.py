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

@api.post("/post_employee")
def post_employee( request,Item:Employees_Model) :
        loggings.info(" Post Employee API called")
        
        email=Item.email
        name=Item.name
        sql_raw=Employee.objects.raw('INSERT INTO api_Employee (email,name )  VALUES (%s,%s  )', [email ,name])
        try:
            for k in sql_raw:
                pass
        except:
            pass
        output="Employee "+str(name)+" is created"
        
        loggings.info(" Post Employee API is Sucessfull")
        return {"result":output}

@api.post("/filter_reservation_by_employees")
def filter_employee(request, employee_email:str) :
 
        loggings.info("Post Filter Employee API is Called")
        
        emp_id=employee_email
        sql_raw=Bookings.objects.raw('SELECT * FROM api_Bookings WHERE User_id  = %s',[emp_id])
        all=[]
        
        try:
            loggings.info(" Reservations Found by this employee")
            
            for i in sql_raw: 
                    
                    k1=i.booking_id
                    sql_raw_1=Reservations.objects.raw('SELECT * FROM api_Reservations WHERE booking_id = %s',[k1])
                    for k in sql_raw_1: 
                        
                        all.append([k.booking_id,k.User_id,k.Room_id,k.from_date,k.end_date,k.title,k.invites ])
        
        except:
            
            loggings.info("No Reservations made by this employee or he is not the host of the meet")
            loggings.info(" Post Filter Employee is Sucessfull")
            
            return {"result":"No Reservations made by this employee "}
        
        loggings.info(" Post Filter Employee is Sucessfull")
       
        return {"result":all}
