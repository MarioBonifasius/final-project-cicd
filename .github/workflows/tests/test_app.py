import unittest
from app import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
    
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        print("✓ Home page test passed")
    
    def test_service_endpoint(self):
        response = self.app.get('/service')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SERVICERUNNING', response.data)
        print("✓ SERVICERUNNING test passed")

if __name__ == '__main__':
    unittest.main()
