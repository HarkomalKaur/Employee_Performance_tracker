#Test Code - V2 - 2024-10-03

import unittest

class TestEmployeePerformanceTracker(unittest.TestCase):

    def setUp(self):
        """Set up initial environment, like test client or preconditions."""
        self.valid_username = "test_user"
        self.valid_password = "test_password"
        self.invalid_username = "invalid_user"
        self.invalid_password = "invalid_password"
        self.dashboard_data = {"tasks_completed": 10, "performance_score": 80}
        self.database = {"test_user": {"password": "test_password", "data": self.dashboard_data}}

    def login(self, username, password):
        """Simulate a login functionality, returning True for valid credentials."""
        if username in self.database and self.database[username]["password"] == password:
            return True
        return False

    def get_dashboard(self, username):
        """Simulate fetching dashboard data for a logged-in user."""
        if username in self.database:
            return self.database[username]["data"]
        return None

    def test_valid_login(self):
        """Test login with valid credentials."""
        self.assertTrue(self.login(self.valid_username, self.valid_password), 
                        "Valid login should succeed")

    def test_invalid_login(self):
        """Test login with invalid credentials."""
        self.assertFalse(self.login(self.invalid_username, self.invalid_password), 
                         "Invalid login should fail")

    def test_dashboard_access(self):
        """Smoke test that the dashboard loads properly for a valid user."""
        data = self.get_dashboard(self.valid_username)
        self.assertIsNotNone(data, "Dashboard should load for valid users")
        self.assertEqual(data["tasks_completed"], 10, 
                         "Task count should match expected value")
        self.assertEqual(data["performance_score"], 80, 
                         "Performance score should match expected value")

    def test_dashboard_no_access(self):
        """Smoke test that the dashboard does not load for an invalid user."""
        data = self.get_dashboard(self.invalid_username)
        self.assertIsNone(data, "Dashboard should not load for invalid users")

    def test_database_interaction(self):
        """Test that database returns the correct data for a valid user."""
        data = self.get_dashboard(self.valid_username)
        self.assertEqual(data["tasks_completed"], 10, 
                         "Database should return the correct task count")
        self.assertEqual(data["performance_score"], 80, 
                         "Database should return the correct performance score")

    def test_invalid_database_interaction(self):
        """Test that the database does not return data for an invalid user."""
        data = self.get_dashboard(self.invalid_username)
        self.assertIsNone(data, "No data should be returned for an invalid user")

if __name__ == '__main__':
    unittest.main()
