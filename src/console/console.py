# Solicitar valores al usuario
import sys
sys.path.append("src")
from logic import  reverse_mortgage
from logic.reverse_mortgage import (
    calculate_reverse_mortgage_payment,
    get_input,
    InvalidInputError,
    DataTypeError,
    InvalidPropertyValueError,
    InvalidInterestRateError,
    InvalidPropertyConditionError,
    InvalidMaritalStatusError,
    ExcessivePropertyValueError
)

def main():
    """Main function to interact with the user and calculate the mortgage payment."""
    try:
        property_value = get_input("Enter the property value: ", float)
        property_condition = get_input("Enter the property condition (excellent, good, average): ", str, ["excellent", "good", "average"])
        marital_status = get_input("Enter your marital status (married, single, divorced): ", str, ["married", "single", "divorced"])
        owner_age = get_input("Enter the owner's age: ", int)
        spouse_age = get_input("Enter the spouse's age: ", int)
        interest_rate = get_input("Enter the interest rate (e.g., 0.05 for 5%): ", float)

        monthly_payment = calculate_reverse_mortgage_payment(property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)
        
        print(f"The monthly reverse mortgage payment is: {monthly_payment}")

    except (InvalidInputError, DataTypeError, InvalidPropertyValueError, 
            InvalidInterestRateError, InvalidPropertyConditionError, 
            InvalidMaritalStatusError, ExcessivePropertyValueError) as error:
        print(f"Error: {error}")
        print("Please correct the error and try again.")
        return  # Stop the program if there's an error


if __name__ == "__main__":
    main()
