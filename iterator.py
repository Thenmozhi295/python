mytuple=("vijay","ashwin","ironman")
myit=iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#looping through an iterator

mytuple=("ironman","hulk","captionamerica")

for x in mytuple:
  print(x)

#another example

class MyNumbers:
  def __iter__(self):
    self.a =1
    return self
  
  def __next__(self):
    x=self.a
    self.a +=1
    return x

myclass=MyNumbers()
myiter=iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

