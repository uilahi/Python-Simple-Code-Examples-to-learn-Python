class SpecialMethod():

    def __init__(self,name,age,place):
        self.name = name
        self.age= age
        self.place = place

    def __str__(self):
        return f"My name is {self.name} age is {self.age} and place is {self.place}"

    def __len__(self):
        return len(self.name)

    def __del__(self):
        print("Object Deleted")

sm = SpecialMethod("Yassar", 20, "Pune")

print(sm)

print(str(sm))

print(len(sm))

del sm


