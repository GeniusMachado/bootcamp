import unittest

# ---------------------------------------------------------
# Part A: The "Real" Code (This would usually be in main.py)
# ---------------------------------------------------------
def calculate_discount(price, is_member):
    if price < 0:
        raise ValueError("Price cannot be negative")

    if is_member:
        return price * 0.90  # 10% off
    else:
        return price

# ---------------------------------------------------------
# Part B: The "Test" Code (This is what the Pipeline runs)
# ---------------------------------------------------------
class TestShoppingLogic(unittest.TestCase):

    # Test 1: Does the discount work?
    def test_member_discount(self):
        result = calculate_discount(100, True)
        self.assertEqual(result, 90)  # Expect 90

    # Test 2: Does a non-member pay full price?
    def test_non_member(self):
        result = calculate_discount(100, False)
        self.assertEqual(result, 100) # Expect 100

    # Test 3: Edge Case - What if price is negative?
    def test_negative_price(self):
        # We assert that the code MUST crash (raise an error)
        with self.assertRaises(ValueError):
            calculate_discount(-50, True)

if __name__ == '__main__':
    unittest.main()
