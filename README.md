
# Corner Case Technologies - API Assignment

## Meeting Room Reservation API using Django
[![Corner Case Technologies|Django](https://www.cornercasetech.com/static/e5a3f47a3b77fdf490df90d88ff4155c/93826/header-cct-logo.webp)](https://www.cornercasetech.com/)
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Description

This projects provides api routes to book meeting rooms for internal and external meetings. Employee can check rooms availability and book or cancel a reservation through this api.

### Routes
- Authentication
- Creating meeting room
- Creating Employee
- Get meeting room reservations and filter by employee 
- Create reservation
- Cancel reservation
- Logout

### Tech Stack Used
This project uses number of open source libraries and frameworks described below:
- Django Rest API
- Django ninja
- Django Rest API Swagger
- Docker

### Instruction to run the API
#### Normal Python Enviroment
Create a `python=3.6` env
```
conda create -n DjangoApi python=3.6
conda activate DjangoApi
```
Install the dependencies
```
cd service
pip install -r requirements.txt
```
Now, Run the service
```
python manage.py runserver
```
Also, To Run Unit Tests that are created
```
python manage.py test test
```

Check Logger File  ,
```

logger.log

```


#### Docker

```
Docker build -t "dockername:tag" .
Docker run -p 8000:8000 "dockername:tag"
```

Now, visit localhost:8000/api/docs/ to access the api. Create a Auth token and access the api routes and use them as per your requirements 

# API Usage Screenshots

![App](https://github.com/yuvaraj-06/meeting-room-reservation/blob/main/screenshots/api.png)

## Authentication of the API
<p float="left">
  <img src="https://github.com/yuvaraj-06/meeting-room-reservation/blob/main/screenshots/auth.png?raw=true" width="400" />
  <img src="https://github.com/yuvaraj-06/meeting-room-reservation/blob/main/screenshots/auth-1.PNG?raw=true" width="400" /> 
  
</p>

## GET & POST Routes for Meeting Rooms

<p float="left">
  
  <img src="https://github.com/yuvaraj-06/meeting-room-reservation/blob/main/screenshots/post_room.PNG?raw=true"    /> 
  <img src="https://github.com/yuvaraj-06/meeting-room-reservation/blob/main/screenshots/get_room.png?raw=true"   />
  
</p>

## GET & POST Routes for Employees 

<p float="left">
  
  <img src="https://github.com/yuvaraj-06/meeting-room-reservation/blob/main/screenshots/post_emp.PNG?raw=true"    /> 
  <img src="https://github.com/yuvaraj-06/meeting-room-reservation/blob/main/screenshots/get_emp.png?raw=true"   />
  
</p>
 
## POST Routes for Making Reservation  

<p float="left">
  
  <img src="https://github.com/yuvaraj-06/meeting-room-reservation/blob/main/screenshots/post_res.png?raw=true"    /> 
  
</p>

## POST Routes for  Filter Reservations by Employee and Canceling Reservation  

<p float="left">
   <img src="https://github.com/yuvaraj-06/meeting-room-reservation/blob/main/screenshots/post_filter.png?raw=true"    /> 
  <img src="https://github.com/yuvaraj-06/meeting-room-reservation/blob/main/screenshots/post_cancel.png?raw=true"    /> 
   
 
 
</p>

 

