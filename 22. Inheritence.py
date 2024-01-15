class Animals:   #Parent class is Animals 
    alive = True

    def eat(self):  # defining common function  
        print("This animal is eating")

    def sleep(self):# defining common function
        print("This animal is sleeping")
    
    def fly(self): # defining common function
        print("This animal flies ")
    
    def run(self): # defining common function
        print("THis animal can run ")

    def swim(self): # defining common function
        print("THis animal can swim")

class Rabit(Animals): # Child class #have all properties of parent class
    pass

class Fish(Animals): 
    pass

class Hawk(Animals): 
    pass

rabit = Rabit() # Creating objects from class

fish = Fish() # Creating objects from class

hawk = Hawk() # Creating objects from class

print(rabit.alive)
rabit.run()
fish.eat()
hawk.fly()