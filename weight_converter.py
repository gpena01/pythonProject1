# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms (kg) or Pounds (lbs)?: ").lower()

if unit == "kg":
    weight = weight * 2.205
    unit = "lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "lbs":
    weight = weight / 2.205
    unit = "kgs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not valid")

