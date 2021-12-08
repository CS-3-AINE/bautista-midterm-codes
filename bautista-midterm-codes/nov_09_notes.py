class Dog:

    def eat(**kwargs):
        return "Eating..." + kwargs['name']

    def bark():
        return "Barking..."

    def run():
        return "Running..."
    
    def sleep():
        return "Sleeping..."

# how to call or instantiate a class
if __name__ == "__main__":

    dg = Dog
    action = dg.eat(name = "Saver")
    print(action) # will display allocation

    #ct = Dog
    #action = ct.eat(name="Tom")
    #print (action)
    
    #print (dg.eat())