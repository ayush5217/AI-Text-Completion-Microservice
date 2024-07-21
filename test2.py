import unittest
from unittest.mock import patch, MagicMock

from app import app


class TestSentenceCompleter(unittest.TestCase):

    def test_hello_route(self):
        # Test the '/' route for rendering the template
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<!DOCTYPE html>', response.data)  # Checking for basic HTML structure

    @patch('app.AutoModelForCausalLM.from_pretrained')
    def test_completions_route(self, mock_model):
        mock_model.return_value = MagicMock()
        mock_model.return_value.generate.return_value = {'generated_text': ' This is the completion.'}

        # Test the '/v1/yourchosenmodel/completions' route with valid data
        with app.test_client() as client:
            data = {'text': 'This is a test sentence'}
            response = client.post('/v1/yourchosenmodel/completions', json=data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'completed_text': 'This is a test sentence This is the completion.'})

        # Test with missing data in request body
        with app.test_client() as client:
            response = client.post('/v1/yourchosenmodel/completions', json={})
            self.assertEqual(response.status_code, 400)  # Expect bad request

if __name__ == '__main__':
    unittest.main()
