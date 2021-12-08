class getbmi:
    def bmiFunc (**kwargs):
        kg = kwargs['kg']
        cm = kwargs['cm']
    def under():
        return "Underweight"
    def normal():
        return "Normal weight"
    def over():
        return "Overweight"
    def ob():
        return "Obese"

kg = int(input("Enter your weight: "))
cm = int(input("Enter your height: "))

if __name__ == "__main__":
    result = (kg / cm**2)*10000
    print("Your BMI is: " + str(result))

if result < 18.5:
    bmi = getbmi
    stat = bmi.under()
    print(stat)

elif result >= 18.5 or result <= 24.9:
    bmi = getbmi
    stat = bmi.normal()
    print(stat)

elif result >= 25 or result <= 29.9:
    bmi = getbmi
    stat = bmi.over()
    print(stat)
#else:
    bmi = getbmi
    stat = bmi.ob()
    print(stat)