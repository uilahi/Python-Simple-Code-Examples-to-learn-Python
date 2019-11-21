class Person():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def printname(self):
        print(self.first_name,self.last_name)

    def printfirstname(self):
        print(self.first_name)

####### Multi level Inheritence ###############
class Child(Person):

    def __init__(self,first_name,last_name,age):
        Person.__init__(self,first_name,last_name)
        self.age = age

    def printage(self):
        Person.printname(self)
        print("I am {} {} & y age is {} ".format(self.first_name,self.last_name, self.age))


class School():

    def __init__(self, school_name, school_id):
        self.school_name = school_name
        self.school_id = school_id

    def printschooldetails(self ):
        print(self.school_name," : ",+self.school_id)

####### Multi pple Inheritence ###############

class GrandChild(Child,School):

    def __init__(self,first_name,last_name,age,school_name, school_id,place):
        Child.__init__(self,first_name,last_name,age)
        School.__init__(self, school_name, school_id)
        self.place = place

    def printplace(self):
        Child.printage(self)
        print("And I live in {}".format(self.place))


my_child = GrandChild("Yassar","Yelurkar",20,"H A School",9221,"Pune")

### We can call method / properties (values from init method) all 4 classes####

my_child.printfirstname()
my_child.printschooldetails()



