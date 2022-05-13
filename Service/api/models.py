from django.db import models
from ninja import Schema,Field


# Let models be here
class Employee(models.Model):
	id=models.AutoField(default=1,primary_key=True)
	email = models.CharField(max_length=255,unique=True)
	name = models.CharField(max_length=255)
class Employees(models.Model):
	sid=models.AutoField(default=1,primary_key=True)
	#email = models.CharField(max_length=255,unique=True)
	email = models.CharField(max_length=255)
class Rooms(models.Model):
	room_no = models.CharField(max_length=255,primary_key=True)

class Reservations(models.Model):
	booking_id=models.AutoField(primary_key=True,default=1)
	User_id = models.CharField(max_length=255)
	Room_id = models.CharField(max_length=255)
	from_date = models.DateField()
	end_date = models.DateField()
	title = models.CharField(max_length=255)
	invites = models.CharField(max_length=255)

class Bookings(models.Model):
	uid=models.AutoField(primary_key=True,default=1)
	User_id = models.CharField(max_length=255)
	booking_id = models.CharField(max_length=255)

class Rooms_Model(Schema):
	room_no:str= Field("102", alias="Room_Number")
class Employees_Model(Schema):
 
	email : str =Field("user@example.com",alias="Email_Id_Of_Employee")
	name : str =Field("user",alias="Name_Of_Employee")
class Reservations_Model(Schema):
 
	User_id : str =Field("user@example.com",alias="Email_Id_Of_Employee")

	from_date : str =Field("2022-05-13",alias="From_Date")
	end_date : str =Field("2022-05-13",alias="End_Date")
	title: str =Field("Tech Stack Upgrade Meet",alias="Meeting_Agenda_Title")
	invites : str =Field("user1@example.com,user2@example.com",alias="Invites_Email_Ids")


class Bookings_Model(Schema):
	 
	User_id : str =Field("user@example.com",alias="Email_Id_Of_Employee")
	booking_id : str =Field("1",alias="Booking_Id")