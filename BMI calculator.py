def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("**************Welcome to the BMI Calculator!**************")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi}")
    print(f"Your BMI category is: {category}")

main()
while True:
    cont = input("Do you want to another Measurement? (yes/no): ")
    if cont=="ÿes":
        main()
    else:
        print("Thank You for using")
    