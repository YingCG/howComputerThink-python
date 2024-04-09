import unittest
from checkout import Checkout

class TestCheckout(unittest.TestCase):
    # can crate an instance of the checkout class
    def test_checkout_instance(self):
        cart = Checkout()
        self.assertIsInstance(cart, Checkout)

    # can add an item price
    def test_canAddItemPrice(self):
        cart = Checkout()
        cart.addItemPrice("egg", 5)
        # Add assertions to ensure item price is added correctly
        self.assertEqual(cart.products["egg"], 5)

    # can add an item
    def test_canAddItem(self):
        cart = Checkout()
        cart.addItem("egg")
        
    # can calculate the current total
    def test_GetCorrentTotal(self):
        cart = Checkout()
        cart.addItemPrice("jam", 5.99)
        total = cart.calculateTotal()
        self.assertEqual(total, 5.99)
        
    # can add multiple items and get correct total
    def test_GetMultipleItemCorrectTotal(self):
        cart = Checkout()
        # Add item prices
        cart.addItemPrice("jam", 5.99)
        cart.addItemPrice("bread", 2.49)
        cart.addItemPrice("milk", 1.99)
        
        total = cart.calculateTotal()

        # Calculate expected total
        expected_total = 5.99 + 2.49 + 1.99

        # Assert total
        self.assertEqual(total, expected_total)
        
    # can add discount rules
    # can apply discount rules to the total
    # Exception is thrown for item added without a price

if __name__ == '__main__':
    unittest.main()
