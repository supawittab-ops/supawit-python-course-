"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"
 
 
def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
 
    bmi = weight / (height ** 2)
    category = get_bmi_category(bmi)
 
    print(f"\nYour BMI is: {bmi:.1f}")
    print(f"Category: {category}")
 
 
if __name__ == "__main__":
    main()

"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
EXCHANGE_RATE = 35.5  # 1 USD = 35.5 THB
 
 
def main():
    print("Currency Converter")
    print("1. THB to USD")
    print("2. USD to THB")
 
    choice = input("Choose conversion direction (1 or 2): ")
    amount = float(input("Enter the amount to convert: "))
 
    if choice == "1":
        result = amount / EXCHANGE_RATE
        print(f"\nFormula: USD = THB / {EXCHANGE_RATE}")
        print(f"{amount:.2f} THB = {result:.2f} USD")
    elif choice == "2":
        result = amount * EXCHANGE_RATE
        print(f"\nFormula: THB = USD * {EXCHANGE_RATE}")
        print(f"{amount:.2f} USD = {result:.2f} THB")
    else:
        print("Invalid choice. Please enter 1 or 2.")
 
 
if __name__ == "__main__":
    main()