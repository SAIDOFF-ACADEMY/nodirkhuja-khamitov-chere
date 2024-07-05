from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


from user.models import User, UserContactApplication
from user.serializers import UserContacApplicationSerializer

class TestLogIn(APITestCase):

    

    def test_check_password_and_email(self):

        login_data = {
            "email": 'a@a.com',
            "password": 'abcd1234'
        }

        token_count = 0
        User.objects.create_user(**login_data, is_staff=True)
        
        response = self.client.post("/api/v1/admin/user/login", data=login_data)
        token_count = Token.objects.count()

        self.assertEqual(response.status_code, 200, "Login failed with valid credentials")
        self.assertIn('token', response.data, 'Token is not send')
        self.assertEqual(token_count, 1)

class TestUserContactApplication(APITestCase):

    def test_unauthenticated_user_cannot_list_user_contact_application(self):

        response = self.client.get("/api/v1/admin/user/list")

        self.assertEqual(response.status_code, 401)


    def test_only_admin_can_list_user_contact_application(self):

        login_data = {
            "email": 'a@a.com',
            "password": 'abcd1234'
        }

        User.objects.create_user(**login_data, is_staff=True)
        self.client.login(**login_data)
        response = self.client.post("/api/v1/admin/user/login", data=login_data)

        response = self.client.get("/api/v1/admin/user/list")
    
        self.assertEqual(response.status_code, 200)

    def test_contact_application_list_with_admin(self):

        login_data = {
            "email": 'a@a.com',
            "password": 'abcd1234'
        }

        user = User.objects.create_user(**login_data, is_staff=True)

        # CERATE USER CONTACT APPLICATION
        self.contact1 = UserContactApplication.objects.create(
            full_name='John Doe', 
            phone_number='+998978824042', 
            user=user
        )

        # LOGIN
        self.client.login(**login_data)
        
        # SERIALIZER.DATA
        contacts = UserContactApplication.objects.all()
        
        serializer = UserContacApplicationSerializer(contacts, many=True)

        response = self.client.get("/api/v1/admin/user/list")
        self.assertEqual(response.data, serializer.data)


    def test_only_admin_can_edit_user_contact_application(self):

        login_data = {
            "email": 'a@a.com',
            "password": 'abcd1234'
        }

        user = User.objects.create_user(**login_data, is_staff=True)

    
        self.client.force_login(user)


        old_data = {
            "full_name": "nodirkhuja",
            "phone_number": "+998978824141",
            "user": user
        }

        contact = UserContactApplication.objects.create(**old_data)
        
        new_data = {
            "full_name":'boburkhuja',
            "phone_number": "+998978804040"
        } 

        response = self.client.put(f"/api/v1/admin/user/edit/{contact.id}", data=new_data)
        
    
        assert response.status_code == 200
        assert response.data["full_name"] == "boburkhuja"

        