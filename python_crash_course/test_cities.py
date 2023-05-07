import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""
    def test_city_country(self):
        test = city_country("santiago", "chile")
        self.assertEqual(test, "Santiago, Chile")
    
    def test_city_country_populaion(self):
        test = city_country("santiago", "chile", 5000000)
        self.assertEqual(test, "Santiago, Chile - population 5000000")

if __name__ == "__main__":
    unittest.main()

