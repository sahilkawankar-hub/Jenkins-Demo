
import unittest
from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(
            greet(),
            "Hello from Jenkins CI/CD Pipeline! Version 4"
        )

if __name__ == "__main__":
    unittest.main()
