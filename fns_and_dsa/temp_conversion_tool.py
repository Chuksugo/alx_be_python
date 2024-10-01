# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Conversion factor for Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Conversion factor for Celsius to Fahrenheit

# Global offsets
FAHRENHEIT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def main():
    while True:
        try:
            # Prompt the user for a temperature
            temperature = input("Enter the temperature to convert (or 'exit' to quit): ")
            if temperature.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break  # Exit the loop if the user types 'exit'

            temperature = float(temperature)  # Convert input to float
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()  # User input for unit

            if unit == 'C':
                converted_temp = convert_to_fahrenheit(temperature)  # Convert to Fahrenheit
                print(f"{temperature}°C is {converted_temp:.2f}°F")  # Format to 2 decimal places
            elif unit == 'F':
                converted_temp = convert_to_celsius(temperature)  # Convert to Celsius
                print(f"{temperature}°F is {converted_temp:.2f}°C")  # Format to 2 decimal places
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")  # Invalid unit handling

        except ValueError:  # Handle non-numeric temperature input
            print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()  # Run the main function
