from django.db import models
from django.forms import DateField
from psycopg2 import Date
from ninja import Schema,Field


# Let models be here
class Employee(models.Model):
	id=models.AutoField(default=1,primary_key=True)
	email = models.CharField(max_length=255,unique=True)
	name = models.CharField(max_length=255)

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

