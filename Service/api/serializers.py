from rest_framework import serializers
from .models import Employee,Rooms,Reservations,Bookings


class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = '__all__'#('email', 'name')


class RoomsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rooms
		fields = '__all__'#('room_no')

class ReservationsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reservations
		fields = ('User_id','Room_id','from_date','end_date','title','invites')

class BookingsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bookings
		fields = '__all__'#('User_id','booking_id')