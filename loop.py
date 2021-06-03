for i in range(10):
  print(i)


num1=10
num2=20
if num1>num2:
   print("%r is greater than %r"%(num1,num2))
else:
   print("%r is greater than %r"%(num2,num1))



a, b = 0, 1
while b<100:
  print(b)
  a, b = b, a+b



row = int(input("Enter the number of rows:"))
n = row
while n>=0:
  x ="*"* n
  print(x)
  n -=1
