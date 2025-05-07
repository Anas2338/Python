def main(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))

celsius_output = main(fahrenheit_input)

print(f"Temperature: {fahrenheit_input}F = {celsius_output}C")
