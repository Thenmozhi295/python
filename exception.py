a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=a/b
print("a/b=%d%c")

#try-except statement

try:
  a=int(input("Enter a:"))
  b=int(input("Enter b:"))
  c=a/b
except:
  print("can't divide with zero")
 
Raising exception

try:
   age=int(input("Enter the age:"))
   if(age<18):
      raise ValueError
   else:
      print("the age is valid")
except ValueError:
     print("the age is not valid")
