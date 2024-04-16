import unittest

from project.restaurant import Restaurant


class TestRestaurant(unittest.TestCase):
    def setUp(self):
        self.restaurant = Restaurant("Chez Panisse", 50)

    def test_init(self):
        self.assertEqual(self.restaurant.name, "Chez Panisse")
        self.assertEqual(self.restaurant.capacity, 50)
        self.assertEqual(len(self.restaurant.waiters), 0)

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            self.restaurant.name = ""

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError):
            self.restaurant.capacity = -1

    def test_add_waiter(self):
        response = self.restaurant.add_waiter("John")
        self.assertIn("has been added", response)
        self.assertEqual(len(self.restaurant.waiters), 1)

    def test_add_waiter_full_capacity(self):
        self.restaurant.capacity = 0
        response = self.restaurant.add_waiter("John")
        self.assertEqual(response, "No more places!")

    def test_add_duplicate_waiter(self):
        self.restaurant.add_waiter("John")
        response = self.restaurant.add_waiter("John")
        self.assertIn("already exists", response)

    def test_remove_waiter(self):
        self.restaurant.add_waiter("John")
        response = self.restaurant.remove_waiter("John")
        self.assertIn("has been removed", response)

    def test_remove_nonexistent_waiter(self):
        response = self.restaurant.remove_waiter("Jane")
        self.assertEqual(response, "No waiter found with the name Jane")

    def test_get_waiters(self):
        self.restaurant.add_waiter("John")
        self.restaurant.add_waiter("Jane")
        self.restaurant.waiters[0]['total_earnings'] = 100
        self.restaurant.waiters[1]['total_earnings'] = 200
        filtered_waiters = self.restaurant.get_waiters(min_earnings=150)
        self.assertEqual(len(filtered_waiters), 1)
        self.assertEqual(filtered_waiters[0]['name'], "Jane")

    def test_get_total_earnings(self):
        self.restaurant.add_waiter("John")
        self.restaurant.add_waiter("Jane")
        self.restaurant.waiters[0]['total_earnings'] = 100
        self.restaurant.waiters[1]['total_earnings'] = 300
        total = self.restaurant.get_total_earnings()
        self.assertEqual(total, 400)


if __name__ == '__main__':
    unittest.main()