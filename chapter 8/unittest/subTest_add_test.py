import unittest

def my_function(number: int):
    return "odd" if number % 2 == 0 else "even"

class TestMyFunction(unittest.TestCase):
    def test_eo(self):
        test_cases = [
            (2, "odd"),
            (5, "odd"),
            (-2354, "odd"),
        ]
        
        for number, expected in test_cases:
            with self.subTest(number=number, expected=expected):
                self.assertEqual(my_function(number), expected)

# if __name__ == "__main__":
#     unittest.main()
