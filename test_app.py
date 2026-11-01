import unittest
from app import get_status


class TestApp(unittest.TestCase):

    def test_project_status(self):
        result = get_status()
        self.assertEqual(result["status"], "Running")

    def test_project_name(self):
        result = get_status()
        self.assertEqual(
            result["project"],
            "Azure CI/CD Portfolio"
        )


if __name__ == "__main__":
    unittest.main()
