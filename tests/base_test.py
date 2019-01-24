# from flask_testing import TestCase
# from api import APP, DB
# from config import app_config
# import json


# class BaseTestCase(TestCase):
#     # def create_app(self):
#     #     self.test_client = app.test_client()
#     #     APP.config.from_object(app_config["testing"])
#     #     return APP

#     def setUp(self):
#         """
#         Create the database and commits any changes made permanently
#         """
#         self.client = APP.test_client(self)
#         self.db = DatabaseConnection()


#     def tearDown(self):
#         """
#         Drop the database data and remove session
#         """
#         cont.drop_table('incidents')
#         cont.drop_table('users')

    def signup(
        self,
        firstname="fhgfghfh",
        lastname="fried",
        othernames="dorotyh",
        email="kal@yahoo.com",
        phoneNumber=1111111111,
        username="dankie",
        isAdmin="false",
        password="dankie"):


        return self.client.post(
            'api/v1/auth/signup',
            data=json.dumps(dict(
                firstname=firstname,
                lastname=othernames,
                othernames=othernames,
                email=email,
                phoneNumber=phoneNumber,
                username=username,
                isAdmin=isAdmin,
                password=password
                name=name,
                email=email,
                password=password,
                is_admin=is_admin
            )
            ),
            content_type='application/json'
        )

#         def login_user(self, email, password):
#         """
#         Method for logging a user with dummy data
#         """
#         self.signup()
#         return self.client.post(
#             'api/v1/auth/login',
#             data=json.dumps(
#                 dict(
#                     email=email,
#                     password=password
#                 )
#             ),
#             content_type='application/json'
#         )

#     def get_token(self, username="dankie, password="dankie"):

#         response = self.login_user(username, password)
#         return json.loads(response.data.decode())['token']

#     def add_meal(self, meal_name="fries", price=10000):
#         """
#         Function to create a meal
#         """
#         token = self.get_token()
#         return self.client.post('api/v1/meals', data=json.dumps(
#             dict(
#                 meal_name=meal_name,
#                 price=price
#             )
#         ),
#             content_type='application/json',
#             headers=({"token": token})
#         )

#     def get_meals(self):
#         """
#         function to return meals
#         """
#         self.add_meal()
#         token = self.get_token()
#         return self.client.get('api/v1/meals', headers=({"token": token}))

#     def get_id(self):
#         res = self.get_meals()
#         return json.loads(res.data.decode())['meal_items'][0]['id']

#     def get_meal_id(self):
#         res = self.get_menu()
#         return json.loads(res.data.decode())['Menu'][0]['meal_id']

#     def delete_meal(self):
#         """
#         function to delete a meal
#         """
#         id = self.get_id()
#         token = self.get_token()
#         return self.client.delete('api/v1/meals/{}'.format(id), headers=({
#             "token": token
#         }))

#     def put_meal(self):
#         """
#         function to edit a meal
#         """
#         id = self.get_id()
#         token = self.get_token()
#         return self.client.put('api/v1/meals/{}'.format(id),
#                                data=json.dumps(dict(
#                                    meal_name="chips",
#                                    price=15000
#                                )),
#                                content_type='application/json',
#                                headers=({"token": token}))

#     def add_menu(self):
#         """
#         function to create a menu
#         """
#         id = self.get_id()
#         token = self.get_token()
#         return self.client.post(
#             'api/v1/menu/{}'.format(id),
#             content_type='application/json', headers=({"token": token}))

#     def get_menu(self):
#         """
#         function to return the menu
#         """
#         token = self.get_token()
#         self.add_menu()
#         return self.client.get('api/v1/menu', headers=({"token": token}))

#     def get_menu_id(self):
#         res = self.get_menu()
#         return json.loads(res.data.decode())['Menu'][0]['id']

#     def add_order(self):
#         """
#         function to make an order
#         """
#         id = self.get_meal_id()
#         menu_id = self.get_menu_id()
#         token = self.get_token()
#         return self.client.post(
#             'api/v1/orders/{}/{}'.format(menu_id, id),
#             headers=({"token": token}))

#     def get_admin_orders(self):
#         """
#         function to return orders for authenticated admin
#         """
#         # self.add_order()
#         token = self.get_token()
#         return self.client.get('api/v1/orders', headers=({"token": token}))

#     def get_user_orders(self):
#         """
#         function to return all orders for a customer
#         """
#         self.add_order()
#         token = self.get_token()
#         return self.client.get('api/v1/user/orders',
#                                headers=({"token": token}))

#     def customer(self):
#         self.register_user("marie", "marie@gmail.com", "marie", "False")
#         res = self.client.post('api/v1/auth/login', data=json.dumps(
#             dict(
#                 email="marie@gmail.com",
#                 password="marie"
#             )
#         ),
#             content_type='application/json'
#         )
#         return json.loads(res.data.decode())['token']