

class person:
  def __init__(self, fname, lname):
     self.firstname=fname
     self.lastname=lname

  def printname(self):
     print(self.firstname,self.lastname)

x=person("verti","maran")
x.printname()

#multi-level inheritance

class animal:
   def speak(self):
      print("animal speacking")

class dog(animal):
   def bark(self):
      print("dog barking")
class dogchild(dog):
   def eat(self):
      print("eating bread...")

d=dogchild()
d.bark()
d.speak()
d.eat()
