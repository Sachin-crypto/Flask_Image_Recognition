import unittest
from app import app
import os

class FlaskImageRecognitionTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def get_test_file_path(self, relative_path):
        # Construct the absolute path to the file
        script_dir = os.path.dirname(__file__)
        return os.path.join(script_dir, relative_path)

    def test_main_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_prediction_route_valid_image(self):
        file_path = self.get_test_file_path('test_images/2/Sign 2 (97).jpeg')
        with open(file_path, 'rb') as img_file:
            data = {'file': (img_file, 'test.jpg')}
            response = self.app.post('/prediction', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_prediction_route_invalid_image(self):
        file_path = self.get_test_file_path('requirements.txt')
        with open(file_path, 'rb') as img_file:
            data = {'file': (img_file, 'test.txt')}
            response = self.app.post('/prediction', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'File cannot be processed.', response.data)

    def test_prediction_route_get_request(self):
        response = self.app.get('/prediction')
        self.assertEqual(response.status_code, 405)  # 405 Method Not Allowed

    def test_prediction_route_missing_file(self):
        response = self.app.post('/prediction', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'File cannot be processed.', response.data)

    def test_unknown_route(self):
        response = self.app.get('/nonexistent_route')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()

