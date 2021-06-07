def first(msg):

  print(msg)

first("hello")

second=first

second("hello")
  
#inner function

def func():
  print("we are in first function")
  
def func1():
    print("This is first child function")

def func2():
    print("This is second child function")
   
func1()
func2()
func()

#function can return another function

def hello():
 def hi():
  print("hello")
 return hi

new=hello()
new()
