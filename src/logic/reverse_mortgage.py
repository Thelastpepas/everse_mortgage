# reverse_mortgage.py
class DataTypeError(Exception):
    """Exception raised for errors in data types."""
    pass

class InvalidPropertyValueError(Exception):
    """Exception raised for invalid property values (e.g., zero or negative)."""
    pass

class InvalidInterestRateError(Exception):
    """Exception raised for invalid interest rates."""
    pass

class InvalidPropertyConditionError(Exception):
    """Exception raised for invalid property conditions."""
    pass

class InvalidMaritalStatusError(Exception):
    """Exception raised for invalid marital status."""
    pass

class ExcessivePropertyValueError(Exception):
    """Exception raised for property values that exceed the acceptable limit."""
    pass

class LowPropertyValueError(Exception):
    """Exception raised for property values that fall below the acceptable limit."""
    pass

class InvalidInputError(Exception):
    """Custom exception for invalid inputs."""
    pass

def get_input(prompt: str, expected_type: type = str, valid_values: list = None):
    """
    Generalized input function to handle different data types and validation.
    
    Args:
        prompt (str): The input prompt message.
        expected_type (type): The expected type of the input (e.g., int, float, str).
        valid_values (list): List of valid values for string inputs.
        
    Returns:
        The user input converted to the expected type.
    """
    while True:
        user_input = input(prompt).strip()
        
        if expected_type == float:
            # Check for invalid characters like commas
            if ',' in user_input:
                print(f"Error: Invalid characters found in input: '{user_input}'. Please use a decimal point instead of a comma.")
                continue
            
            try:
                value = float(user_input)
                
                # Custom validation based on the prompt
                if "interest rate" in prompt.lower():
                    if value <= 0 or value > 1:
                        print(f"Error: Interest rate must be between 0 and 1. You entered: {value}.")
                        continue
                
                return value
            except ValueError:
                print(f"Error: Invalid value entered: '{user_input}'. Expected a valid float.")
        
        elif expected_type == int:
            # Check for invalid characters like commas
            if ',' in user_input:
                print(f"Error: Invalid characters found in input: '{user_input}'. Please remove commas.")
                continue
            
            try:
                value = int(user_input)
                
                # Custom validation for integer inputs
                if "property value" in prompt.lower():
                    if value <= 0:
                        print(f"Error: Property value must be a positive number. You entered: {value}.")
                        continue
                    elif value < 200000000 or value > 900000000:
                        print(f"Error: Property value must be between 200,000,000 and 900,000,000. You entered: {value}.")
                        continue
                
                elif "age" in prompt.lower():
                    if value < 18:
                        print(f"Error: Age must be at least 18. You entered: {value}.")
                        continue
                
                return value
            except ValueError:
                print(f"Error: Invalid value entered: '{user_input}'. Expected a valid integer.")
        
        elif expected_type == str:
            value = user_input.lower()
            
            if valid_values and value not in valid_values:
                print(f"Error: Invalid value entered: '{value}'. Valid options are: {', '.join(valid_values)}.")
            else:
                return value
                
        else:
            print("Error: Unsupported expected_type provided.")
def validate_inputs(property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate):
    """
    Function to validate inputs, raising exceptions if inputs are invalid.
    
    Args:
        property_value (int or float): The value of the property.
        property_condition (str): The condition of the property.
        marital_status (str): The marital status of the owner.
        owner_age (int): The age of the owner.
        spouse_age (int): The age of the spouse.
        interest_rate (float): The interest rate of the mortgage.
        
    Raises:
        DataTypeError: If any input has an incorrect data type.
        InvalidPropertyValueError: If the property value is invalid.
        ExcessivePropertyValueError: If the property value exceeds the acceptable limit.
        InvalidInterestRateError: If the interest rate is invalid.
        InvalidPropertyConditionError: If the property condition is invalid.
        InvalidMaritalStatusError: If the marital status is invalid.
    """
    # Type verification
    if not isinstance(property_value, (int, float)):
        raise DataTypeError(f"Property value must be a number. You entered: {property_value}.")
    
    if not isinstance(owner_age, int) or not isinstance(spouse_age, int):
        raise DataTypeError(f"Owner and spouse ages must be integers. You entered: owner age = {owner_age}, spouse age = {spouse_age}.")
    
    if not isinstance(interest_rate, (int, float)):
        raise DataTypeError(f"Interest rate must be a number. You entered: {interest_rate}.")
    
    # Validation
    if property_value <= 0:
        raise InvalidPropertyValueError(f"Property value must be a positive number. You entered: {property_value}.")
    
    if not (200_000_000 <= property_value <= 900_000_000):
        raise ExcessivePropertyValueError(f"Property value must be between 200,000,000 and 900,000,000. You entered: {property_value}.")
    
    min_age = min(owner_age, spouse_age)
    if min_age > 85:
        raise InvalidPropertyValueError("Owner and spouse age must not exceed 85.")
    
    if owner_age < 18 or spouse_age < 18:
        raise InvalidPropertyValueError(f"Owner and spouse must be at least 18 years old. You entered: owner age = {owner_age}, spouse age = {spouse_age}.")
    
    if not (0 < interest_rate <= 1):
        raise InvalidInterestRateError(f"Interest rate must be between 0 and 1. You entered: {interest_rate}.")
    
    valid_conditions = ["excellent", "good", "average"]
    if property_condition not in valid_conditions:
        raise InvalidPropertyConditionError(f"Invalid property condition: '{property_condition}'. Must be one of {', '.join(valid_conditions)}.")
    
    valid_marital_statuses = ["married", "single", "divorced"]
    if marital_status not in valid_marital_statuses:
        raise InvalidMaritalStatusError(f"Invalid marital status: '{marital_status}'. Must be one of {', '.join(valid_marital_statuses)}.")

def calculate_reverse_mortgage_payment(property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate):
    """
    Calculate the monthly reverse mortgage payment.
    
    Args:
        property_value (int or float): The value of the property.
        property_condition (str): The condition of the property.
        marital_status (str): The marital status of the owner.
        owner_age (int): The age of the owner.
        spouse_age (int): The age of the spouse.
        interest_rate (float): The interest rate of the mortgage.
        
    Returns:
        float: The calculated monthly mortgage payment.
    """
    # Validate inputs
    validate_inputs(property_value, property_condition, marital_status, owner_age, spouse_age, interest_rate)

    # Adjust property value based on condition
    condition_adjustment = {"excellent": 1, "good": 0.9, "average": 0.8}
    adjusted_value = property_value * condition_adjustment[property_condition]

    # Calculate life expectancy
    youngest_age = min(owner_age, spouse_age)
    life_expectancy_years = get_life_expectancy(youngest_age)
    life_expectancy_months = life_expectancy_years * 12

    # Calculate mortgage payment
    loan_percentage = 0.50
    mortgage_amount = adjusted_value * loan_percentage
    monthly_interest_rate = (1 + interest_rate) ** (1/12) - 1
    monthly_payment = mortgage_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -life_expectancy_months)

    total_payment = monthly_payment * life_expectancy_months
    if total_payment > mortgage_amount:
        monthly_payment = mortgage_amount / life_expectancy_months

    return round(monthly_payment, 2)

def get_life_expectancy(age):
    """
    Return life expectancy based on age.
    
    Args:
        age (int): The age of the person.
        
    Returns:
        int: Estimated life expectancy in years.
    """
    if age >= 70:
        return 15
    elif age >= 65:
        return 20
    else:
        return 25









