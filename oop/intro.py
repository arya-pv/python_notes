#..oop...object oriented programming...
#class...design pattern
#object..real world entity
#reference...operations

#class
class Person():
    def walk(self):   #instance keyword
        print("person is walking")
    def read(self):
        print("person is reading")

# object
pe1=Person()
pe1.walk()
pe1.read()

#object2
pe2=Person()
pe2.read()
pe2.walk()