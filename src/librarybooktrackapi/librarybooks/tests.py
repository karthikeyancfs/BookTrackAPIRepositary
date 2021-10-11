from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

import json


# initialize the APIClient app
client = Client()

# Create your tests here.

class CreateNewBookTest(TestCase):
    """ Test module for insert the Book record """

    def setUp(self):
        """ Define Test payload """
        self.valid_payload = { "title": "The 5 AM Club",
                               "author_name": "Robin Sharma",
                               "isbn_num": "978-3-16-148410-0",
                               "genre": "Self-help book",
                               "description": "A little known formula you can use instantly to wake up early feeling inspired, focused and flooded with a fiery drive to get the most out of each day"
                            }

    def test_create_book_record(self):
        """ Test the Book create api """
        response = client.post('/book/', self.valid_payload, format='json')
        # response = client.post(
        #     url = 'http://127.0.0.1:8000/book/',
        #     data=json.dumps(self.valid_payload),
        #     content_type='application/json'
        # )
        print(f'Response is {response}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)