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


def helper(emp_id,from_time):
          
        sql_raw_1=Reservations.objects.raw('SELECT * FROM api_Reservations WHERE User_id = %s AND from_date= %s',[emp_id,from_time])
        
    
        for i in sql_raw_1:
            
            bid=i.booking_id
            tm=i.invites.split(",")
            
            for o in tm:
                
                
                sql_raw_2=Reservations.objects.raw('INSERT INTO api_Bookings (User_id,booking_id) VALUES (%s,%s)',[o,bid])
                try:
                    
                    for k in sql_raw_2:
                       pass
                except:
                    pass

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

@api.post("/reserve_room")
def reserve_room( request,Item:Reservations_Model) :
    
        loggings.info("Post Reservations  API is Called")
        
        emp_id=Item.User_id
        title=Item.title
        from_time=Item.from_date 
        end_time=Item.end_date 
        invites=Item.invites
         
        sql_raw=Reservations.objects.raw('SELECT * FROM api_Reservations WHERE from_date<=%s AND %s<=end_date OR from_date<=%s AND %s<=end_date',[from_time,from_time,end_time,end_time])
        rows=[]
        for i in sql_raw:
           
            rows.append(i.Room_id)
       
        sql_raw_1=Rooms.objects.raw("SELECT * FROM api_Rooms")
        lp=[]
        for i in sql_raw_1:
          
            lp.append(i.room_no)
        
        if rows==[]:
            
            loggings.info("All Rooms are Available So Allocating The First Room")
            
            sql_raw_2=Reservations.objects.raw("INSERT INTO api_Reservations (User_id,Room_id,from_date,end_date,title,invites) VALUES (%s,%s,%s,%s,%s,%s)",[emp_id,lp[0],from_time,end_time,title,invites])
            try:
                for k in sql_raw_2:
                    pass
            except:
                pass

            sql_raw_3=Reservations.objects.raw('SELECT * FROM api_Reservations WHERE User_id = %s AND from_date= %s',[emp_id,from_time])
            k=[]
            for i in sql_raw_3:
                k.append(i.booking_id)
            
            k=k[0]
            sql_raw_4=Reservations.objects.raw('INSERT INTO api_Bookings (User_id,booking_id) VALUES (%s,%s)',[emp_id,k])
            try:
                for k in sql_raw_4:
                    pass
            except:
                pass
            
            helper(emp_id,from_time)
            
            loggings.info(" Post Reservations API is Sucessfull")
            
            return {"result":"Reservations has been Successful"}
        
        else:
        
            ans=(list(set(lp)-set(rows)))
            if ans==[]:
                
                loggings.info("No Rooms are Available ")
                
                return {"result":"Reservations has been Unsuccessful , Please Try With Differnet From and End Date "}
            
            loggings.info(" Rooms are Available ")
            
            sql_raw_5=Reservations.objects.raw("INSERT INTO api_Reservations (User_id,Room_id,from_date,end_date,title,invites) VALUES (%s,%s,%s,%s,%s,%s)",[emp_id,ans[0],from_time,end_time,title,invites])
            try:
                for k in sql_raw_5:
                    pass
            except:
                pass
            
            sql_raw_6=Reservations.objects.raw('SELECT * FROM api_Reservations WHERE User_id = %s AND from_date= %s',[emp_id,from_time])
            k=[]
            for i in sql_raw_6:
                k.append(i.booking_id)
            
            k=k[0]
            sql_raw_7=Reservations.objects.raw('INSERT INTO api_Bookings (User_id,booking_id) VALUES (%s,%s)',[emp_id,k])
            try:
                for k in sql_raw_7:
                    pass
            except:
                pass
            
            helper(emp_id,from_time)
            
            loggings.info(" Post Reservations API is Sucessfull")
            
            return {"result":"Reservations has been Successful"}
