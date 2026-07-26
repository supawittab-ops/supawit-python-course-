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
    print("BMI Calculator")
 
    while True:
        weight_input = input("\nEnter your weight in kilograms (or 'q' to quit): ")
 
        if weight_input.lower() == "q":
            print("Goodbye!")
            break
 
        height_input = input("Enter your height in meters: ")
 
        weight = float(weight_input)
        height = float(height_input)
 
        bmi = weight / (height ** 2)
        category = get_bmi_category(bmi)
 
        print(f"Your BMI is: {bmi:.1f}")
        print(f"Category: {category}")
 
 
if __name__ == "__main__":
    main()
