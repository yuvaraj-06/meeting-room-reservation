from collections import defaultdict
from django.shortcuts import render
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
loggings = logging.getLogger()
loggings.setLevel(logging.INFO)

def view_rooms():

    sql_raw=Rooms.objects.raw('SELECT * FROM api_Rooms')
        
    res=[]
    
    d_room = defaultdict(list)
    for k in sql_raw:
        d_room['Room_Numbers'].append(k.room_no)
    
    res.append(d_room)

    return res


def view_employees():

    sql_raw=Employee.objects.raw('SELECT  *  FROM api_Employee ')
    res=[]
        
    for k in sql_raw:

        d_employee = defaultdict(list)
        d_employee["Employee_Id"] = k.id
        d_employee["Employee_Name"] = k.name   
        d_employee["Employee_Email"] = k.email  
        res.append(d_employee)
    
    return res

def add_room(num):

    search = view_rooms()   

    room_nums = search[0]["Room_Numbers"]
    print(str(num),room_nums)
    if str(num) not in room_nums:
        
        sql_raw=Rooms.objects.raw('INSERT INTO api_Rooms (room_no )  VALUES (%s )', [num])
        try:
            for i in sql_raw:
                pass
        except:
            pass
        
        return True
    return False 
    
def add_employee(email,name):

    search = view_employees()

    for i in search:

        if i["Employee_Name"] == name and i["Employee_Email"] == email:

            return False
        
    

    sql_raw=Employee.objects.raw('INSERT INTO api_Employee (email,name )  VALUES (%s,%s  )', [email ,name])
    try:
        for k in sql_raw:
            pass
    except:
        pass

    return True


def filter(emp_id):

    sql_raw=Bookings.objects.raw('SELECT * FROM api_Bookings WHERE User_id  = %s',[emp_id])
    all=[]
        
    try:
        loggings.info(" Reservations Found by this employee")
            
        for i in sql_raw: 
                    
            k1=i.booking_id
            sql_raw_1=Reservations.objects.raw('SELECT * FROM api_Reservations WHERE booking_id = %s',[k1])

                    
                    

            for k in sql_raw_1: 

                d_filter = defaultdict(list)

                d_filter["Booking_Id"] = k.booking_id 
                d_filter["Employee_Id"] = k.User_id
                d_filter["Room_Id"] = k.Room_id 
                d_filter["From_Date"] = k.from_date 
                d_filter["End_Date"] = k.end_date
                d_filter["Title"] = k.title 
                d_filter["Invites_Email_Ids"] = k.invites 

 
                all.append(d_filter)

        return all       
        
    except:
            
        return False

def checking(emp_id,from_time,end_time):

    sql_raw_1=Reservations.objects.raw('SELECT * FROM api_Reservations WHERE User_id = %s AND from_date= %s AND end_date = %s',[emp_id,from_time,end_time])

    for i in sql_raw_1:

        return False 
    
    return True


def helper(emp_id,from_time,invites):
          
        sql_raw_1=Reservations.objects.raw('SELECT * FROM api_Reservations WHERE User_id = %s AND from_date= %s AND invites = %s',[emp_id,from_time,invites])
        
        
    
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

def reserve(emp_id,title,from_time,end_time,invites):

    if checking(emp_id,from_time,end_time):

        

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
                
            helper(emp_id,from_time,invites)
            loggings.info(" Post Reservations API is Sucessfull")
            return "Reservations has been Successful"
                
            
        else:
            
            ans=(list(set(lp)-set(rows)))
            if ans==[]:
                    
                loggings.info("No Rooms are Available ")
                    
                return "Reservations has been Unsuccessful , Please Try With Differnet From and End Date "
                
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
                
            helper(emp_id,from_time,invites)
            loggings.info(" Post Reservations API is Sucessfull")
            return "Reservations has been Successful"
    else:

        return "Reservation already exist"
