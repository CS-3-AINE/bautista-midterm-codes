
def bmi (kg, cm):
    return (kg / cm**2)*10000
kg = int(input("Enter your weight: "))
cm = int(input("Enter you height: "))

print("Your BMI is: " + str(bmi(kg, cm)))

if bmi(kg, cm) < 18.5:
    print("Underweight")
    
elif bmi(kg,cm) >= 18.5 or bmi(kg, cm) <= 24.9:
    print("Normal weight")

elif bmi(kg, cm) >= 25 or bmi(kg, cm) <= 29.9:
    print("Overweight")
else:
    print("Obese")



