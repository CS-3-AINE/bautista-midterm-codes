#Bautista Aine

class Calc:
    def add(*args):
        sum = 0
        for val in args:
            sum = sum + val
        print(sum)

    def sub(*args):
        diff = 0
        for val in args:
            diff = val - diff
        print(diff)

    if __name__== "__main__":

        choice = input("Select operator\n(1) add (2) subtract: ")
        if choice in ('1', '2'):
            value = [float(value) for value in input("Enter series of numbers: ").split(',')]     
        else:
            print("Invalid input!")
        
        if choice == '1':
                add(*value)
        elif choice == '2':
            sub(*value)  