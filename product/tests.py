from rest_framework.test import APITestCase

from user.models import User
from product.models import Product, FreeProduct
from product.serializers import ProductSerializer, FreeProductSerializer


class TestProduct(APITestCase):

    def test_not_admin_user_cannot_access(self):

        product_data = {

            "name": '10L water',
            "content": '<p>Water</p>',
            "price": "100.00",
            "is_active": "False"
        }
        user = User.objects.create_user(email='a@a.com', password='12345678', is_staff=False)
        self.client.force_login(user)

        product = Product.objects.create(**product_data)

        response_list = self.client.get('/api/v1/admin/product/list')
        self.assertEqual(response_list.status_code, 403)

        response_get = self.client.get(f'/api/v1/admin/product/detail/{product.id}')
        self.assertEqual(response_get.status_code, 403)

        response_create = self.client.post("/api/v1/admin/product/add", data=product_data)
        self.assertEqual(response_create.status_code, 403)

        response_put = self.client.put(f"/api/v1/admin/product/update/{product.id}", data=product_data)
        self.assertEqual(response_put.status_code, 403)
        
        response_delete = self.client.delete(f'/api/v1/admin/product/detail/{product.id}')
        self.assertEqual(response_delete.status_code, 403)


    def test_get_product_by_admin(self):

        product_data = {

            "name_uz": '10L suv',
            "name_ru": '10L water',
            "content": '<p>Water</p>',
            "price": "100.00",
            "is_active": "False"
        }

        product = Product.objects.create(**product_data)


        user = User.objects.create_user(email='a@a.com', password='12345678', is_staff=True)
        self.client.force_login(user)
        

        serializer = ProductSerializer(product)

        response = self.client.get(f'/api/v1/admin/product/detail/{product.id}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)



    def test_add_product_by_admin(self):

        product_data = {
            "name_uz": '10L suv',
            "name_ru": '10L water',
            "content_ru": '<p>Water</p>',
            "content_uz": '<p>Suv</p>',
            "price": "100.00",
            "is_active": False
        }
        
        user = User.objects.create_user(email='a@a.com', password='12345678', is_staff=True)
        self.client.force_login(user)

        response = self.client.post('/api/v1/admin/product/add', data=product_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name_uz"], "10L suv")
        self.assertEqual(response.data["content_ru"], "<p>Water</p>")

    
    def test_update_product_by_admin(self):

        old_product_data = {
            "name_uz": '10L suv',
            "name_ru": '10L water',
            "content_ru": '<p>Water</p>',
            "content_uz": '<p>Suv</p>',
            "price": "100.00",
            "is_active": False
        }

        new_product_data = {
            "name_uz": '20L suv',
            "name_ru": '20L water',
            "content_ru": '<p>Water</p>',
            "content_uz": '<p>Suv</p>',
            "price": "200.00",
            "is_active": True
        }
        
        user = User.objects.create_user(email='a@a.com', password='12345678', is_staff=True)
        self.client.force_login(user)

        product = Product.objects.create(**old_product_data)

        response = self.client.put(f'/api/v1/admin/product/update/{product.id}', data=new_product_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name_uz"], "20L suv")
        self.assertEqual(response.data["content_ru"], "<p>Water</p>")

    def test_delete_product_by_admin(self):

        product_data = {
            "name_uz": '10L suv',
            "name_ru": '10L water',
            "content_ru": '<p>Water</p>',
            "content_uz": '<p>Suv</p>',
            "price": "100.00",
            "is_active": False
        }

        user = User.objects.create_user(email='a@a.com', password='12345678', is_staff=True)
        self.client.force_login(user)

        product = Product.objects.create(**product_data)

        response = self.client.delete(f'/api/v1/admin/product/delete/{product.id}')

        self.assertEqual(response.status_code, 204)

    
    def test_list_product_by_admin(self):

        product_1_data = {
            "name_uz": '10L suv',
            "name_ru": '10L water',
            "content_ru": '<p>Water</p>',
            "content_uz": '<p>Suv</p>',
            "price": "100.00",
            "is_active": True
        }

        product_2_data = {
            "name_uz": '20L suv',
            "name_ru": '20L water',
            "content_ru": '<p>Water</p>',
            "content_uz": '<p>Suv</p>',
            "price": "200.00",
            "is_active": True
        }

        user = User.objects.create_user(email='a@a.com', password='12345678', is_staff=True)
        self.client.force_login(user)

        Product.objects.create(**product_1_data)
        Product.objects.create(**product_2_data)

        response = self.client.get('/api/v1/admin/product/list')


        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name_uz'], '10L suv')
        self.assertEqual(response.data[1]['price'], '200.00')





class TestFreeProduct(APITestCase):

    def test_not_admin_user_cannot_access(self):

        product_data = {
            "name_uz": '20L suv',
            "name_ru": '20L water',
            "content_ru": '<p>Water</p>',
            "content_uz": '<p>Suv</p>',
            "price": "200.00",
            "is_active": True
        }
        product = Product.objects.create(**product_data)

        free_product = {
            "product": product,
            "count": 12,
            "free_count": 5
        }
        
        free_product_obj = FreeProduct.objects.create(**free_product)

        user = User.objects.create_user(email='a@a.com', password='12345678', is_staff=False)
        self.client.force_login(user)

        response_list = self.client.get('/api/v1/admin/product/free/list')
        self.assertEqual(response_list.status_code, 403)

        response_get = self.client.get(f'/api/v1/admin/product/free/detail/{free_product_obj.id}')
        self.assertEqual(response_get.status_code, 403)

        response_create = self.client.post("/api/v1/admin/product/free/add", data=free_product)
        self.assertEqual(response_create.status_code, 403)

        response_put = self.client.put(f"/api/v1/admin/product/free/update/{free_product_obj.id}", data=free_product)
        self.assertEqual(response_put.status_code, 403)


    
    def test_get_free_product_by_admin(self):

        product_data = {
            "name_uz": '20L suv',
            "name_ru": '20L water',
            "content_ru": '<p>Water</p>',
            "content_uz": '<p>Suv</p>',
            "price": "200.00",
            "is_active": True
        }
        product = Product.objects.create(**product_data)

        free_product = {
            "product": product,
            "count": 12,
            "free_count": 5
        }
        
        free_product = FreeProduct.objects.create(**free_product)

        user = User.objects.create_user(email='a@a.com', password='12345678', is_staff=True)
        self.client.force_login(user)

        serializer = FreeProductSerializer(free_product)

        response = self.client.get(f'/api/v1/admin/product/free/detail/{product.id}')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)


    def test_add_free_product_by_admin(self):

        product_data = {
            "name_uz": '20L suv',
            "name_ru": '20L water',
            "content_ru": '<p>Water</p>',
            "content_uz": '<p>Suv</p>',
            "price": "200.00",
            "is_active": True
        }
        product = Product.objects.create(**product_data)

        free_product = {
            "product": product.id,
            "count": 12,
            "free_count": 5
        }
        

        user = User.objects.create_user(email='a@a.com', password='12345678', is_staff=True)
        self.client.force_login(user)

        response = self.client.post('/api/v1/admin/product/free/add', data=free_product)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["count"], 12)
        self.assertEqual(response.data["free_count"], 5)

    
    def test_update_product_by_admin(self):

        product_data = {
            "name_uz": '20L suv',
            "name_ru": '20L water',
            "content_ru": '<p>Water</p>',
            "content_uz": '<p>Suv</p>',
            "price": "200.00",
            "is_active": True
        }
        product = Product.objects.create(**product_data)

        free_product = {
            "product": product.id,
            "count": 12,
            "free_count": 5
        }
        

        user = User.objects.create_user(email='a@a.com', password='12345678', is_staff=True)
        self.client.force_login(user)

        product = Product.objects.create(**product_data)
        f_product = FreeProduct.objects.create(**free_product)

        new_free_product = {
            "product": product,
            "count": 10,
            "free_count": 4
        }

        response = self.client.put(f'/api/v1/admin/product/update/{f_product.id}', data=new_free_product)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 10)

    def test_delete_product_by_admin(self):

        product_data = {
            "name_uz": '10L suv',
            "name_ru": '10L water',
            "content_ru": '<p>Water</p>',
            "content_uz": '<p>Suv</p>',
            "price": "100.00",
            "is_active": False
        }

        user = User.objects.create_user(email='a@a.com', password='12345678', is_staff=True)
        self.client.force_login(user)

        product = Product.objects.create(**product_data)

        response = self.client.delete(f'/api/v1/admin/product/delete/{product.id}')

        self.assertEqual(response.status_code, 204)

    
    def test_list_product_by_admin(self):

        product_1_data = {
            "name_uz": '10L suv',
            "name_ru": '10L water',
            "content_ru": '<p>Water</p>',
            "content_uz": '<p>Suv</p>',
            "price": "100.00",
            "is_active": True
        }

        product_2_data = {
            "name_uz": '20L suv',
            "name_ru": '20L water',
            "content_ru": '<p>Water</p>',
            "content_uz": '<p>Suv</p>',
            "price": "200.00",
            "is_active": True
        }

        user = User.objects.create_user(email='a@a.com', password='12345678', is_staff=True)
        self.client.force_login(user)

        Product.objects.create(**product_1_data)
        Product.objects.create(**product_2_data)

        response = self.client.get('/api/v1/admin/product/list')


        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name_uz'], '10L suv')
        self.assertEqual(response.data[1]['price'], '200.00')

