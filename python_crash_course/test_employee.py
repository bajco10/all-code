import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self, custom_raise=1000):
        self.first = "Marek"
        self.last = "Chaler"
        self.salary = 12000
        self.custom_raise = custom_raise
        self.employee = Employee(self.first, self.last, self.salary)
    
    def test_give_default_raise(self):
        raised_salary = int(self.salary) + 5000
        self.assertEqual(raised_salary, 17000)
    
    def test_give_custom_raise(self):
        raised_salary = int(self.salary) + self.custom_raise
        self.assertEqual(raised_salary, (int(self.salary)+self.custom_raise))

if __name__ == "__main__":
    unittest.main()
