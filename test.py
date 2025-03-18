import unittest
from Lab_1 import House, Tenant, Landlord, Contract

class TestHouse(unittest.TestCase):
    def setUp(self):
        self.house = House(1000000)

    def test_get_price(self):
        self.assertEqual(self.house.price, 1000000)

    def test_get_availability(self):
        self.assertTrue(self.house.availability)

    def test_set_price(self):
        self.house.price = 2000000
        self.assertEqual(self.house.price, 2000000)

    def test_set_availability(self):
        self.house.availability = False
        self.assertFalse(self.house.availability) 
        self.house.availability = True
        self.assertTrue(self.house.availability)  

    def test_get_number(self):
        self.assertEqual(self.house.number, 1)

class TestTenant(unittest.TestCase):
    def setUp(self):
        self.tenant = Tenant("Eren")
        self.house = House(100000)

    def test_get_name(self):
        self.assertEqual(self.tenant.name, "Eren")

    def test_set_name(self):
        self.tenant.name = "Armin"
        self.assertEqual(self.tenant.name, "Armin")

    def test_get_rental_house(self):
        self.assertIsNone(self.tenant.rental_house)

    def test_set_rental_house(self): 
        self.tenant.rental_house = self.house
        self.assertEqual(self.tenant.rental_house, self.house)

class TestLandlord(unittest.TestCase):
    def setUp(self):
        self.house = House(10000)
        self.landlord = Landlord("Eren")
        self.tenant = Tenant("Armin")

    def test_get_name(self):
        self.assertEqual(self.landlord.name, "Eren")
        
    def test_set_name(self):
        self.landlord.name = "Job"
        self.assertEqual(self.landlord.name, "Job") 

    def test_get_list_of_houses(self):
        self.assertEqual(self.landlord.list_of_houses, [])
        
    def test_add_available_house(self):
        self.landlord.add_available_house(self.house)
        self.assertIn(self.house, self.landlord.list_of_houses)

class TestContract(unittest.TestCase):
    def setUp(self):
        self.house = House(100000)
        self.landlord = Landlord("Bob")
        self.landlord.add_available_house(self.house)
        self.tenant = Tenant("Job")

    def test_add_contract(self):
        self.landlord.add_contract(self.house, self.landlord, self.tenant, "21.04.2025", "21.05.2025")
        self.contract = Contract.list_of_contracts[0]

        self.assertEqual(self.contract.)
        self.assertFalse(self.house.availability)

if __name__ == "__main__":
    unittest.main()