# Create your tests here.
import unittest
from django.test import Client
import requests


class MyUnitTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test(self):
        response = self.client.post('/api/post_rooms',data={"Room_Number": "501"},content_type='application/json',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid data.
        self.assertEqual(response.json().get('result'),"Room 501 is created")

        response = self.client.post('/api/post_rooms',data={"Room_Number": "502"},content_type='application/json',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid data.
        self.assertEqual(response.json().get('result'),"Room 502 is created")

        response = self.client.post('/api/post_rooms',data={"Room_Number": "502"},content_type='application/json',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid data.
        self.assertEqual(response.json().get('result'),"Room 502 already exists")
    
     
        response = self.client.post('/api/post_employee',data={"Email_Id_Of_Employee": "test1@test.com","Name_Of_Employee": "test1"},content_type='application/json',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid data.
        self.assertEqual(response.json().get('result'),"Employee test1 is created")

        response = self.client.post('/api/post_employee',data={"Email_Id_Of_Employee": "test2@test.com","Name_Of_Employee": "test2"},content_type='application/json',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid data.
        self.assertEqual(response.json().get('result'),"Employee test2 is created")

        response = self.client.post('/api/post_employee',data={"Email_Id_Of_Employee": "test3@test.com","Name_Of_Employee": "test3"},content_type='application/json',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid data.
        self.assertEqual(response.json().get('result'),"Employee test3 is created")

        response = self.client.post('/api/post_employee',data={"Email_Id_Of_Employee": "test4@test.com","Name_Of_Employee": "test4"},content_type='application/json',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid data.
        self.assertEqual(response.json().get('result'),"Employee test4 is created")

        response = self.client.post('/api/post_employee',data={"Email_Id_Of_Employee": "test5@test.com","Name_Of_Employee": "test5"},content_type='application/json',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid data.
        self.assertEqual(response.json().get('result'),"Employee test5 is created")

        response = self.client.post('/api/post_employee',data={"Email_Id_Of_Employee": "test6@test.com","Name_Of_Employee": "test6"},content_type='application/json',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid data.
        self.assertEqual(response.json().get('result'),"Employee test6 is created")

        response = self.client.post('/api/post_employee',data={"Email_Id_Of_Employee": "test3@test.com","Name_Of_Employee": "test3"},content_type='application/json',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid data.
        self.assertEqual(response.json().get('result'), "Employee test3 already exists")

   
        response = self.client.post('/api/reserve_room',data={"Email_Id_Of_Employee": "test1@test.com","From_Date": "2022-05-14","End_Date": "2022-05-15","Meeting_Agenda_Title": "Tech Stack Upgrade Meet","Invites_Email_Ids": "test2@test.com"},content_type='application/json',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid data.
        self.assertEqual(response.json().get('result'),"Reservations has been Successful")
        print(response.json().get('result'))
        response = self.client.post('/api/reserve_room',data={"Email_Id_Of_Employee": "test3@test.com","From_Date": "2022-05-14","End_Date": "2022-05-15","Meeting_Agenda_Title": "Tech Stack Upgrade Meet","Invites_Email_Ids": "test4@test.com"},content_type='application/json',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid data.
        self.assertEqual(response.json().get('result'),"Reservations has been Successful")
        print(response.json().get('result'))
        response = self.client.post('/api/reserve_room',data={"Email_Id_Of_Employee": "test1@test.com","From_Date": "2022-05-14","End_Date": "2022-05-15","Meeting_Agenda_Title": "Tech Stack Upgrade Meet","Invites_Email_Ids": "test2@test.com"},content_type='application/json',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid data.
        self.assertEqual(response.json().get('result'),"Reservation already exist")

        response = self.client.post('/api/reserve_room',data={"Email_Id_Of_Employee": "test5@test.com","From_Date": "2022-05-14","End_Date": "2022-05-15","Meeting_Agenda_Title": "Tech Stack Upgrade Meet","Invites_Email_Ids": "test6@test.com"},content_type='application/json',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid data.
        self.assertEqual(response.json().get('result'),"Reservations has been Unsuccessful , Please Try With Differnet From and End Date ")

    
     
        response = self.client.get('/api/get_rooms',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
    

 
        
        response = self.client.get('/api/get_employee',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
    
    

        response = self.client.post('/api/filter_reservation_by_employees?employee_email=test1%40test.com',content_type='application/json',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid data.
        self.assertEqual(response.json().get('result'), [{ "Booking_Id": 1, "Employee_Id": "test1@test.com", "Room_Id": "501","From_Date": "2022-05-14","End_Date": "2022-05-15", "Title": "Tech Stack Upgrade Meet","Invites_Email_Ids": "test2@test.com"}])
 
        print(response.json().get('result'))

        response = self.client.post('/api/Cancel_Reservations?employee_email=test1%40test.com&from_date=2022-05-14&end_date=2022-05-15',content_type='application/json',**{'HTTP_AUTHORIZATION': 'Basic YWRtaW46YWRtaW4='})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid data.
        self.assertEqual(response.json().get('result'), "Reservation Canceled Successfully")
        print(response.json().get('result'))


 
