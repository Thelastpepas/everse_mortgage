import unittest
import sys
sys.path.append("src")
from logic import  reverse_mortgage

class HipotecaInversaTest(unittest.TestCase):

    # Normal Cases: Tests with typical scenarios

    def test_Normal_1(self):
        # Input parameters
        property_value = 500000000
        property_condition = "excellent"
        marital_status = "married"
        owner_age = 70
        spouse_age = 68
        interest_rate = 0.5
        
        # Expected payment result
        expected_payment = 1041666.67

        # Execute and verify the result
        result = reverse_mortgage.calculate_reverse_mortgage_payment(
            property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)
        self.assertEqual(round(result, 2), expected_payment)

    def test_Normal_2(self):
        property_value = 400000000
        property_condition = "good"
        marital_status = "married"
        owner_age = 72
        spouse_age = 70
        interest_rate = 0.5
        
        expected_payment = 1000000

        result = reverse_mortgage.calculate_reverse_mortgage_payment(
            property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)
        self.assertEqual(round(result, 2), expected_payment)

    def test_Normal_3(self):
        property_value = 250000000
        property_condition = "average"
        marital_status = "married"
        owner_age = 65
        spouse_age = 67
        interest_rate = 0.07
        
        expected_payment = 416666.67

        result = reverse_mortgage.calculate_reverse_mortgage_payment(
            property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)
        self.assertEqual(round(result, 2), expected_payment)

    def test_Normal_4(self):
        property_value = 300000000
        property_condition = "average"
        marital_status = "married"
        owner_age = 70
        spouse_age = 68
        interest_rate = 0.5
        
        expected_payment = 500000

        result = reverse_mortgage.calculate_reverse_mortgage_payment(
            property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)
        self.assertEqual(round(result, 2), expected_payment)

    def test_Normal_5(self):
        property_value = 300000000
        property_condition = "excellent"
        marital_status = "married"
        owner_age = 75
        spouse_age = 65
        interest_rate = 0.06
        
        expected_payment = 625000

        result = reverse_mortgage.calculate_reverse_mortgage_payment(
            property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)
        self.assertEqual(round(result, 2), expected_payment)

    def test_Normal_6(self):
        property_value = 280000000
        property_condition = "good"
        marital_status = "married"
        owner_age = 80
        spouse_age = 70
        interest_rate = 0.08
        
        expected_payment = 700000

        result = reverse_mortgage.calculate_reverse_mortgage_payment(
            property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)
        self.assertEqual(round(result, 2), expected_payment)

    # Extraordinary Cases: Tests with edge cases and unusual scenarios

    def test_Extraordinary_1(self):
        # Spouse at the age limit
        property_value = 650000000
        property_condition = "good"
        marital_status = "married"
        owner_age = 90
        spouse_age = 85
        interest_rate = 0.05
        
        expected_payment = 1625000

        result = reverse_mortgage.calculate_reverse_mortgage_payment(
            property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)
        self.assertEqual(round(result, 2), expected_payment)

    def test_Extraordinary_2(self):
        # Spouse too young for a mortgage
        property_value = 300000000
        property_condition = "excellent"
        marital_status = "married"
        owner_age = 80
        spouse_age = 18
        interest_rate = 0.07
        
        expected_payment = 500000

        result = reverse_mortgage.calculate_reverse_mortgage_payment(
            property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)
        self.assertEqual(round(result, 2), expected_payment)

    def test_Extraordinary_3(self):
        # Very low interest rate
        property_value = 500000000
        property_condition = "excellent"
        marital_status = "married"
        owner_age = 70
        spouse_age = 68
        interest_rate = 0.0001
        
        expected_payment = 1041666.67

        result = reverse_mortgage.calculate_reverse_mortgage_payment(
            property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)
        self.assertEqual(round(result, 2), expected_payment)

    def test_Extraordinary_4(self):
        # Property value at the lower limit
        property_value = 200000000
        property_condition = "excellent"
        marital_status = "married"
        owner_age = 70
        spouse_age = 70
        interest_rate = 0.07
        
        expected_payment = 555555.56

        result = reverse_mortgage.calculate_reverse_mortgage_payment(
            property_value, property_condition, marital_status, owner_age, max(0, spouse_age), interest_rate)
        self.assertEqual(round(result, 2), expected_payment)

    def test_Extraordinary_5(self):
        # Significant age difference between owner and spouse
        property_value = 500000000
        property_condition = "good"
        marital_status = "married"
        owner_age = 70
        spouse_age = 85
        interest_rate = 0.07
        
        expected_payment = 1250000

        result = reverse_mortgage.calculate_reverse_mortgage_payment(
            property_value, property_condition, marital_status, min(120, owner_age), spouse_age, interest_rate)
        self.assertEqual(round(result, 2), expected_payment)

    def test_Extraordinary_6(self):
        # High property value at the upper limit with average condition
        property_value = 900000000
        property_condition = "average"
        marital_status = "married"
        owner_age = 70
        spouse_age = 65
        interest_rate = 0.1
        
        expected_payment = 1500000

        result = reverse_mortgage.calculate_reverse_mortgage_payment(
            property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)
        self.assertEqual(result, expected_payment)

    # Error Cases: Tests that expect exceptions

    def test_Error_1(self):
        # Invalid data type for property value
        property_value = ""
        property_condition = "excellent"
        marital_status = "married"
        owner_age = 70
        spouse_age = 68
        interest_rate = 0.07
        
        with self.assertRaises(reverse_mortgage.DataTypeError):
            reverse_mortgage.calculate_reverse_mortgage_payment(
                property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)

    def test_Error_2(self):
        # Invalid property value (zero)
        property_value = 0
        property_condition = "excellent"
        marital_status = "married"
        owner_age = 70
        spouse_age = 68
        interest_rate = 0.07
        
        with self.assertRaises(reverse_mortgage.InvalidPropertyValueError):
            reverse_mortgage.calculate_reverse_mortgage_payment(
                property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)

    def test_Error_3(self):
        # Valid property value with excessive interest rate
        property_value = 100000000
        property_condition = "excellent"
        marital_status = "married"
        owner_age = 70
        spouse_age = 68
        interest_rate = 0.04
        
        with self.assertRaises(reverse_mortgage.ExcessivePropertyValueError):
            reverse_mortgage.calculate_reverse_mortgage_payment(
                property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)

    def test_Error_4(self):
        # Invalid interest rate (zero)
        property_value = 400000000
        property_condition = "excellent"
        marital_status = "married"
        owner_age = 70
        spouse_age = 68
        interest_rate = 0
        
        with self.assertRaises(reverse_mortgage.InvalidInterestRateError):
            reverse_mortgage.calculate_reverse_mortgage_payment(
                property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)

    def test_Error_5(self):
        # Invalid property condition
        property_value = 300000000
        property_condition = "unknown"
        marital_status = "married"
        owner_age = 70
        spouse_age = 68
        interest_rate = 0.07
        
        with self.assertRaises(reverse_mortgage.InvalidPropertyConditionError):
            reverse_mortgage.calculate_reverse_mortgage_payment(
                property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)

    def test_Error_6(self):
        # Invalid marital status (empty string)
        property_value = 500000000
        property_condition = "excellent"
        marital_status = ""
        owner_age = 70
        spouse_age = 68
        interest_rate = 0.07
        
        with self.assertRaises(reverse_mortgage.InvalidMaritalStatusError):
            reverse_mortgage.calculate_reverse_mortgage_payment(
                property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)

    def test_Error_7(self):
        # Invalid input for property_value
        property_value = "300000000O"
        property_condition = "good"
        marital_status = "married"
        owner_age = 70  # 
        spouse_age = 68
        interest_rate = 0.07
        
        with self.assertRaises(reverse_mortgage.DataTypeError):
            reverse_mortgage.calculate_reverse_mortgage_payment(
                property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)

    def test_Error_8(self):
        # Invalid marital status (None)
        property_value = 300000000
        property_condition = "excellent"
        marital_status = None
        owner_age = 70
        spouse_age = 68
        interest_rate = 0.07
        
        with self.assertRaises(reverse_mortgage.InvalidMaritalStatusError):
            reverse_mortgage.calculate_reverse_mortgage_payment(
                property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)

    def test_Error_9(self):
        # Invalid interest rate (too high)
        property_value = 400000000
        property_condition = "excellent"
        marital_status = "married"
        owner_age = 70
        spouse_age = 68
        interest_rate = 2  # Invalid interest rate
        
        with self.assertRaises(reverse_mortgage.InvalidInterestRateError):
            reverse_mortgage.calculate_reverse_mortgage_payment(
                property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)

    def test_Error_10(self):
        # Property value exceeds the limit
        property_value = 950000000
        property_condition = "excellent"
        marital_status = "married"
        owner_age = 70
        spouse_age = 68
        interest_rate = 0.07
        
        with self.assertRaises(reverse_mortgage.ExcessivePropertyValueError):
            reverse_mortgage.calculate_reverse_mortgage_payment(
                property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)

    def test_Error_11(self):
        # Property value is excessively high
        property_value = 950000000
        property_condition = "excellent"
        marital_status = "married"
        owner_age = 70
        spouse_age = 68
        interest_rate = 0.07
        
        with self.assertRaises(reverse_mortgage.ExcessivePropertyValueError):
            reverse_mortgage.calculate_reverse_mortgage_payment(
                property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)

if __name__ == '__main__':
    unittest.main()


