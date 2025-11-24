import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestAPI(unittest.TestCase):

    def test_root(self):
        r = client.get("/")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), {"message": "Hello from your Python API with Docker & CI/CD!"})

    def test_add(self):
        r = client.get("/add/2/3")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["result"], 5)

if __name__ == "__main__":
    unittest.main()
