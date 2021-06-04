#create class and object
class MyClass:
   x=5
p1= MyClass()
print(p1.x)

#__init__() function

class person:
 def __init__(self, name, age):
   self.name=name
   self.age=age

p1=person("john",32)
print(p1.name)
print(p1.age)

#delete the object

class Employee:
  id=10
  name="sri"
def display(self):
   print("ID: %d \nName: %s"%(self.id,self.name))

emp=Employee()

del emp.id
del emp
emp.display()
