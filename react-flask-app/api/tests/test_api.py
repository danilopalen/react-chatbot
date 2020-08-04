import unittest
import json
# from flask import Flask
from api import app
from flask import request

class TestApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # app = Flask(__name__) # new app!!! Won't work
        app.config["TESTING"] = True
        cls.test_app = app.test_client()
        # Need to start the chatbot
        cls.test_app.post("/input", json={ "text": "" })

    def test_input_joke(self):
        # No success with data=dict(text="mission")
        # But json={ "text": "mission" } works (need to use obj.get_json())
        # data="<some_string>" also works (need to use obj.data)
        # Same as below
        response = self.test_app.post("/input",
                                      json={ "text": "mission" },
                                      follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Great work all of you: BA, UX and AI people!", response.data)
        
        # print(json.dumps(json.loads(response.data), indent=2))
        
        # No success with data=dict(text="mission")
        # But json={ "text": "mission" } works
        # Want to see what is in the request object
        '''
        with app.test_request_context(path="/input", json={ "text": "mission" }):
            print("testrequest", request.path)
            print("testrequest", request.full_path)
            print("testrequest", request.data)
            print("testrequest", request.get_json())
        '''

    def test_input_001_welcome(self):
        response = self.test_app.post("/input",
                                      json={ "text": "" },
                                      follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"How can I help you today?", response.data)
        self.assertIn(b"Get a Claim", response.data)
        self.assertIn(b"claim", response.data)
        self.assertIn(b"Get a Quote", response.data)
        self.assertIn(b"quote", response.data)

    def test_input_002_get_a_quote(self):
        response = self.test_app.post("/input",
                                      json={ "text": "quote" },
                                      follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Before we begin, did you know you could trade in your old car or get Finance through us?", response.data)
        self.assertIn(b"No thanks, I like my car.", response.data)
        self.assertIn(b"car", response.data)
        self.assertIn(b"Trade-in", response.data)
        self.assertIn(b"trade", response.data)
        self.assertIn(b"Finance", response.data)
        self.assertIn(b"finance", response.data)
        self.assertIn(b"Back", response.data)
        self.assertIn(b"back", response.data)
        
        
