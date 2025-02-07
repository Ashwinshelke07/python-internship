def calculate_bmi(weight_pounds, height_inches):
    """
    Calculate BMI given weight in pounds and height in inches.
    Formula: BMI = (weight in pounds / (height in inches)^2) * 703
    """
    return (weight_pounds / (height_inches ** 2)) * 703

def classify_bmi(bmi):
    """
    Classify BMI into categories.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        weight_pounds = float(input("Enter your weight in pounds: "))
        height_inches = float(input("Enter your height in inches: "))
        if weight_pounds <= 0 or height_inches <= 0:
            print("Weight and height must be positive numbers.")
            return

        bmi = calculate_bmi(weight_pounds, height_inches)
        category = classify_bmi(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")

    except ValueError:
        print("Invalid input. Please enter numerical values for weight and height.")

if __name__ == "__main__":
    main()
