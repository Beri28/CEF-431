import unittest

from app import app


class TestApp(unittest.TestCase):
    def setp(self):
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message":
                                         "Hello level 400 FET, Quality Assurancessssssssss!"})


if __name__ == '__main__':
    unittest.main()
