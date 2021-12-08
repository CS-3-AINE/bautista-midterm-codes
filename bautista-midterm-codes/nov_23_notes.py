# def get_bmi(*args):
#     BMI = args[0] / (args[1]/100)**2
#     if BMI <= 18.4:
#         print("You are underweight.")
#     elif BMI <= 24.9:
#         print("You are healthy.")
#     elif BMI <= 29.9:
#         print("You are over weight.")
#     elif BMI <= 34.9:
#         print("You are severely over weight.")
#     elif BMI <= 39.9:
#         print("You are obese.")
#     else:
#         print("You are severely obese.")

def get_bmi2(**kwargs):
    result = ''
    BMI = kwargs['weight'] / (kwargs['height']/100)**2
    if BMI <= 18.4:
        result = "underweight."
    elif BMI <= 24.9:
        result = "healthy."
    elif BMI <= 29.9:
        result = "weight."
    elif BMI <= 34.9:
        result = "weight."
    elif BMI <= 39.9:
        result = "obese."
    else:
        result = "severely obese."

    return result

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

bmi = get_bmi2(weight=weight, height=height)

print (f"Your BMI is {bmi}")