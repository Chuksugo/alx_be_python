# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Ensure this line is present

# Lambda functions for conversion
convert_to_celsius = lambda fahrenheit: (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
convert_to_fahrenheit = lambda celsius: (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt user for temperature input
        temperature = float(input("Enter the temperature to convert: "))
        
        # Prompt user to specify if the temperature is in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "F":
            # Convert from Fahrenheit to Celsius using lambda
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        
        elif unit == "C":
            # Convert from Celsius to Fahrenheit using lambda
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        
        else:
            # Handle invalid unit input
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError as ve:
        # Handle invalid numeric input and display error message
        print(f"Error: {ve}\nInvalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
