import unittest
import json
from app import app

class FlaskTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_completion_endpoint(self):
        data = {"text": "The capital of france is"}
        response = self.app.post('/v1/yourchosenmodel/completions', json=data)
        self.assertEqual(response.status_code, 200)    #checking response code of llm model func
        json_data = response.get_json()
        self.assertIn("completed_text", json_data)
        completed_text = json_data["completed_text"]
        self.assertIsInstance(completed_text, str)      #cheching data type of the completed text

if __name__ == '__main__':
    unittest.main()
