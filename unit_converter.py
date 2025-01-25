# Simple Unit Converter

def convert_length(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 0.001,
        'miles': 0.000621371,
        'feet': 3.28084
    }
    if from_unit in length_units and to_unit in length_units:
        return round(value * (length_units[to_unit] / length_units[from_unit]), 4)
    return None

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'kilograms': 1,
        'grams': 1000,
        'pounds': 2.20462,
        'ounces': 35.274
    }
    if from_unit in weight_units and to_unit in weight_units:
        return round(value * (weight_units[to_unit] / weight_units[from_unit]), 4)
    return None

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return round((value * 9/5) + 32, 2)
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return round((value - 32) * 5/9, 2)
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return round(value + 273.15, 2)
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return round(value - 273.15, 2)
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return round((value - 32) * 5/9 + 273.15, 2)
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return round((value - 273.15) * 9/5 + 32, 2)
    return None

def main():
    print("Welcome to the Unit Converter!")
    print("Available categories: Length, Weight, Temperature")

    while True:
        category = input("\nEnter conversion category (length/weight/temperature) or 'exit' to quit: ").strip().lower()

        if category == 'exit':
            print("Thank you for using the Unit Converter!")
            break
        
        if category not in ['length', 'weight', 'temperature']:
            print("Invalid category. Please choose length, weight, or temperature.")
            continue

        value = input(f"Enter the value to convert: ")
        try:
            value = float(value)
        except ValueError:
            print("Invalid number. Please enter a numeric value.")
            continue

        from_unit = input("Enter the unit you have: ").strip().lower()
        to_unit = input("Enter the unit to convert to: ").strip().lower()

        if category == 'length':
            result = convert_length(value, from_unit, to_unit)
        elif category == 'weight':
            result = convert_weight(value, from_unit, to_unit)
        elif category == 'temperature':
            result = convert_temperature(value, from_unit, to_unit)
        
        if result is not None:
            print(f"{value} {from_unit} is equal to {result} {to_unit}.")
        else:
            print("Invalid unit conversion. Please try again.")

if __name__ == "__main__":
    main()
