class Dog():
    species = "Mammal"

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.species= Dog.species
    def bark(self,dotted):
        if dotted == True:
            dot= "dotted"
        else:
            dot= "not dotted"

        print("WOffffff...!!!"
              "My name is {} and my age is {} years and I am {} and my species is {}.".format(self.name,self.age,dot,my_dog.species))
def function_bark(dotted):
    if dotted == True:
        dot = "dotted"
    else:
        dot = "not dotted"

    print("WOffffff...!!!"
          "My name is {} and my age is {} years and I am {} and my species is {}.".format(my_dog.name, my_dog.age, dot,Dog.species))


my_dog = Dog("Keanu",4)
my_dog.bark(False)
function_bark(True)