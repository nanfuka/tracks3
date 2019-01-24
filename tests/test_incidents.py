import unittest
from app.views.views import app
from app.controllers.user_controllers import User_controller
import json
from app.db import DatabaseConnection
cont = User_controller()


class TestUsers(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()
        # db = DatabaseConnection()
        cont.drop_table('incidents')
        cont.drop_table('users')
        # # db.create_users_table
        # # db.create_incident_tables
        self.db = DatabaseConnection()
    
    # def signup(
    #     self,
    #     firstname="fhgfghfh",
    #     lastname="fried",
    #     othernames="dorotyh",
    #     email="kal@yahoo.com",
    #     phoneNumber=1111111111,
    #     username="dankie",
    #     isAdmin="false",
    #     password="dankie"):


    #     return self.client.post(
    #         'api/v1/auth/signup',
    #         data=json.dumps(dict(
    #             firstname=firstname,
    #             lastname=othernames,
    #             othernames=othernames,
    #             email=email,
    #             phoneNumber=phoneNumber,
    #             username=username,
    #             isAdmin=isAdmin,
    #             password=password,
                
                
    #         )
    #         ),
    #         content_type='application/json'
    #     )

    def test_index(self):
        """Method for testing the index route"""
        response = self.test_client.get('/')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "hi welcome to the ireporter")
        self.assertEqual(data['status'], 200)

    def test_create_an_intervention(self):
        report = {"createdby": 1,

                  "location": "22.98 33.25",
                  "status": "draft",
                  "images": "imagelocation",
                  "videos": "videolocation",
                  "comment": "this is over recurring",
                  "incident_type": "redflag"
                  }
        response = self.signup( "kalungi", "deborah", "dorothy", "kal@gmail.com", 11111, "dankie", "false", "dankie") 
        response = self.test_client.post(
            'api/v1/auth/intervention',
            content_type='application/json',
            data=json.dumps(report)
        )
        self.assertEqual(response.status_code, 201)
#         self.assertEqual(data['status'], 201)
#         # token = (data['data'][0]['token'])
#         # self.assertEqual(data['data'][0]['message'], 
#         #                  'You have signedup with ireporter as a user')
#         # self.assertEqual(data['data'][0]['token'], token)

#     # def test_delete_redflag(self):

#     #     response = self.test_client.post('/api/v1/red-flags', json=self.report)
#     #     response = self.test_client.delete('/api/v1/red-flags/1/redflag')
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertEqual(data['data'][0], {"id": 1, "message": "red-flag record has been deleted"})
#     #     self.assertEqual(data['status'], 200)

    
#     # def test_delete_redflag_with_wrong_redflag_id(self):
#     #     response = self.test_client.post('/api/v1/red-flags', json=self.report)
#     #     response = self.test_client.delete('/api/v1/red-flags/6/redflag')
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertEqual(data['message'], "no redflag to delete")
#     #     self.assertEqual(data['status'], 200)
    

#     # def test_create_redflag(self):
#     #     """This method tests whether a redflag can be created if all the
#     #      attributes are provided"""
#     #     response = self.test_client.post('/api/v1/red-flags', json=self.report)
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 201)
#     #     self.assertEqual(data['status'], 201)
#     #     self.assertEqual(
#     #         data['data'], [{'id': 1, 'message': 'Added a new incident'}])

#     # def test_create_red_flag_with_invalid_createdby_value(self):
#     #     """This method tests whether a redflag can return an error message if
#     #      all the created by key and/ or value is invalid are provided"""
#     #     report = {"createdby": "dfeefet",

#     #               "location": "22.98 33.25",
#     #               "status": "draft",
#     #               "images": "imagelocation",
#     #               "videos": "videolocation",
#     #               "comment": "this is over recurring",
#     #               "incident_type": "redflag"
#     #               }
#     #     response = self.test_client.post('/api/v1/red-flags', json=report)
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 400)
#     #     self.assertEqual(data['status'], 400)
#     #     self.assertEqual(
#     #         data['error'],
#     #         "createdby should be an id of the creator of the redflag")

#     # def test_create_red_flag_with_no_createdby_value(self):
#     #     """This method tests whether a redflag can return an error message if
#     #      all the created by key and/ or value is invalid are provided"""
#     #     report = {

#     #               "location": "22.98 33.25",
#     #               "status": "draft",
#     #               "images": "imagelocation",
#     #               "videos": "videolocation",
#     #               "comment": "this is over recurring",
#     #               "incident_type": "redflag"
#     #               }
#     #     response = self.test_client.post('/api/v1/red-flags', json=report)
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 400)
#     #     self.assertEqual(data['status'], 400)
#     #     self.assertEqual(
#     #         data['error'],
#     #         "please enter the id of the creator of this redflag")

#     # def test_create_red_flag_with_wrong_incidenttype_value(self):
#     #     """This method tests whether a redflag can return an error message if
#     #      all the location key and/ or value is invalid are provided"""
#     #     report = {"createdby": 2,

#     #               "location": "22.98 33.25",
#     #               "status": "draft",
#     #               "images": "imagelocation",
#     #               "videos": "videolocation",
#     #               "comment": "this is over recurring",
#     #               "incident_type": "theft"
#     #               }
#     #     response = self.test_client.post('/api/v1/red-flags', json=report)
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 400)
#     #     self.assertEqual(data['status'], 400)
#     #     self.assertEqual(
#     #         data,
#     #         {"error":
#     #          "Incident type should either be a redflag or intervention.",
#     #          "status": 400})

#     # def test_create_red_flag_with_no_incidenttype_value(self):
#     #     """This method tests whether a redflag can return an error message if
#     #      all the location key and/ or value is invalid are provided"""
#     #     report = {"createdby": 2,

#     #               "location": "22.98 33.25",
#     #               "status": "draft",
#     #               "images": "imagelocation",
#     #               "videos": "videolocation",
#     #               "comment": "this is over recurring"

#     #               }
#     #     response = self.test_client.post('/api/v1/red-flags', json=report)
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 400)
#     #     self.assertEqual(data['status'], 400)
#     #     self.assertEqual(
#     #         data,
#     #         {"error":
#     #          "Enter a incident type.",
#     #          "status": 400})

#     # def test_create_red_flag_where_incident_type_is_emptystring(self):
#     #     """This method tests whether a redflag can return an error message if
#     #      all the location key and/ or value is invalid are provided"""
#     #     report = {"createdby": 2,

#     #               "location": "22.98 33.25",
#     #               "status": "draft",
#     #               "images": "imagelocation",
#     #               "videos": "videolocation",
#     #               "comment": "this is over recurring",
#     #               "incident_type": " "
#     #               }
#     #     response = self.test_client.post('/api/v1/red-flags', json=report)
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 400)
#     #     self.assertEqual(data['status'], 400)
#     #     self.assertEqual(
#     #         data,
#     #         {"error":
#     #          "Enter a incident type.",
#     #          "status": 400})
   
#     # def test_create_red_flag_with_no_location(self):
#     #     """This method tests whether a redflag can return an error message if
#     #      all the location key and/ or value is invalid are provided"""
#     #     report = {"createdby": 2,

                 
#     #               "status": "draft",
#     #               "images": "imagelocation",
#     #               "videos": "videolocation",
#     #               "comment": "this is over recurring",
#     #               "incident_type": " "
#     #               }
#     #     response = self.test_client.post('/api/v1/red-flags', json=report)
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 400)
#     #     self.assertEqual(data['status'], 400)
#     #     self.assertEqual(
#     #         data,
#     #         {"error":
#     #          "please enter the location of this redflag",
#     #          "status": 400})
            
#     # def test_create_red_flag_with_invalid_location(self):
#     #     """This method tests whether a redflag can return an error message if
#     #      all the location key and/ or value is invalid are provided"""
#     #     report = {"createdby": 2,

#     #               "location": "kawanda",
#     #               "status": "draft",
#     #               "images": "imagelocation",
#     #               "videos": "videolocation",
#     #               "comment": "this is over recurring",
#     #               "incident_type": " "
#     #               }
#     #     string1 = 'invalid location, please enter the lat, long cordinates'
#     #     string2 = 'in this formant, 25.22 56.22'
        
#     #     response = self.test_client.post('/api/v1/red-flags', json=report)
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 400)
#     #     self.assertEqual(data['status'], 400)
#     #     self.assertEqual(
#     #         data,
#     #         {"error":
#     #          string1 + string2,
#     #          "status": 400})

#     # def test_create_red_flag_with_invalid_status(self):
#     #     """This method tests whether a redflag can return an error message if
#     #      all the location key and/ or value is invalid are provided"""
#     #     report = {"createdby": 2,

#     #               "location": "22.98 33.25",
#     #               "status": "nabbed",
#     #               "images": "imagelocation",
#     #               "videos": "videolocation",
#     #               "comment": "this is over recurring",
#     #               "incident_type": "redflag"
#     #               }
#     #     strg1 = 'status should either be draft'
#     #     strg2 = 'underinvestigation, resolved or rejected'
    
#     #     response = self.test_client.post('/api/v1/red-flags', json=report)
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 400)
#     #     self.assertEqual(data['status'], 400)
#     #     self.assertEqual(
#     #         data,
#     #         {"error":
#     #          strg1 + strg2,
#     #          "status": 400})

#     # def test_create_red_flag_with_no_comment(self):
#     #     """This method tests whether a redflag can return an error message if
#     #      all the location key and/ or value is invalid are provided"""
#     #     report = {"createdby": 2,

#     #              "location":"22.33 55.66",
#     #               "status": "draft",
#     #               "images": "imagelocation",
#     #               "videos": "videolocation",
               
#     #               "incident_type": "redflag"
#     #               }
#     #     response = self.test_client.post('/api/v1/red-flags', json=report)
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 400)
#     #     self.assertEqual(data['status'], 400)
#     #     self.assertEqual(
#     #         data,
#     #         {"error":
#     #          "Enter the comment",
#     #          "status": 400})

#     # # def test_create_red_flag_with_invalid_comment(self):
#     # #     """This method tests whether a redflag can return an error message if
#     # #      all the location key and/ or value is invalid are provided"""
#     # #     report = {"createdby": 2,
#     # #             "comment": 125454,
#     # #              "location":"22.33 55.66",
#     # #               "status": "draft",
#     # #               "images": "imagelocation",
#     # #               "videos": "videolocation",
               
#     # #               "incident_type": "redflag"
#     # #               }
#     # #     response = self.test_client.post('/api/v1/red-flags', json=report)
#     # #     data = json.loads(response.data)
#     # #     self.assertEqual(response.status_code, 400)
#     # #     self.assertEqual(data['status'], 400)
#     # #     self.assertEqual(
#     # #         data,
#     # #         {"error":
#     # #          "Comment should be a string",
#     # #          "status": 400})

#     # def test_edit_location(self):
#     #     """This method tests whether after posting valid
#     #     data, a redfalg's location can be modified with a patch method"""
#     #     report = {"createdby": 3,

#     #               "location": "22.98 33.26",
#     #               "status": "draft",
#     #               "images": "imagelocation",
#     #               "videos": "videolocation",
#     #               "comment": "this is over recurring",
#     #               "incident_type": "redflag"
#     #               }
#     #     response = self.test_client.post('/api/v1/red-flags', json=report)
#     #     edited_location = {"location": "22.33 44.56"}
#     #     response = self.test_client.patch('/api/v1/red-flags/1/location',
#     #                                       json=edited_location)
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertEqual(data['status'], 200)


#     #     response = self.test_client.patch('/api/v1/red-flags/8/location',
#     #                                       json=edited_location)
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertEqual(data['message'],
#     #                      'the redflag with redflag_id is not available')
#     #     self.assertEqual(data['status'], 200)

#     # def test_edit_comment(self):
#     #     """This method tests whether after posting valid
#     #     data, a redfalg's comment can be modified with a patch method"""
#     #     response = self.test_client.post('/api/v1/red-flags', json=self.report)
#     #     edited_comment = {"comment": "treat this very seriously"}
#     #     response = self.test_client.patch('/api/v1/red-flags/1/comment',
#     #                                       json=edited_comment)
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertEqual(data['status'], 200)
#     #     # self.assertEqual(data['data'][0], {"id": 1, "message": "Updated redflag"})

#     #     response = self.test_client.patch('/api/v1/red-flags/8/comment',
#     #                                       json=edited_comment)
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertEqual(data['message'],
#     #                      'the redflag with redflag_id is not available')
#     #     self.assertEqual(data['status'], 200)



#     # def test_get_one_redflag(self):
#     #     """This method tests whether after posting valid
#     #     data, a particular can be returned"""
#     #     report = {"createdby": 2,

#     #               "location": "22.98 33.26",
#     #               "status": "draft",
#     #               "images": "imagelocation",
#     #               "videos": "videolocation",
#     #               "comment": "this is over recurring",
#     #               "incident_type": "redflag"
#     #               }
#     #     response = self.test_client.post('/api/v1/red-flags', json=self.report)

#     #     response = self.test_client.get('/api/v1/red-flags/1')
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertEqual(data['status'], 200)
#     #     # self.assertEqual(data['data'][0], {
#     #     #     "comment": "this is over recurring"})
#     #     # #     "createdby": 2,
#     #     # #     "createdon": datetime.datetime.now(),
#     #     # #     "images": "imagelocation",
#     #     # #     "incident_type": "redflag",
#     #     # #     "location": "22.98 33.23",
#     #     # #     "redflag_id": 1,
#     #     # #     "status": "draft",
#     #     # #     "videos": "videolocation"
#     #     # # })
#     #     # # self.assertEqual(data['data']['createdby'], 2)
#     #     # # self.assertEqual(data['data']['images'], "imagelocation")
#     #     # # self.assertEqual(data['data']['incident_type'], "redflag")
#     #     # # self.assertEqual(data['data']['location'], "22.33 44.56")
#     #     # # self.assertEqual(data['data']['redflag_id'], 1)
#     #     # # self.assertEqual(data['data']['status'], "draft")
#     #     # # self.assertEqual(data['data']['videos'], "videolocation")
#     # def test_get_all_redflag(self):
#     #     """This method tests whether after posting valid
#     #     data, a particular can be returned"""
#     #     report = {"createdby": 2,

#     #               "location": "22.98 33.26",
#     #               "status": "draft",
#     #               "images": "imagelocation",
#     #               "videos": "videolocation",
#     #               "comment": "this is over recurring",
#     #               "incident_type": "redflag"
#     #               }
#     #     response = self.test_client.post('/api/v1/red-flags', json=report)

#     #     response = self.test_client.get('/api/v1/red-flags')
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 200)
