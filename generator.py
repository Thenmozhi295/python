def simple():
  for i in range(10):
    if(i%2==0):
      yield i

for i in simple():
   print(i)


#multiple yield

def multiple_yield():
  str1="hello"
  yield str1
  
  str2="frnd"
  yield str2
 
obj=multiple_yield()
print(next(obj))
print(next(obj))

#generator expression

list=[1,2,3,4,5]
z=[x**3 for x in list]


a=(x**3 for x in list)

print(a)
print(z)


import sys

#list comprehension

nums_squared_list=[1*2 for i in range(1000)]
  print(sys.getsizeof("memory in bytes:"nums_squared_list))

#generator expression

nums_squared_gc=(i**2 for i in range(1000))
  print(sys.getsizeof("memory in bytes:",nums_squared_gc))
