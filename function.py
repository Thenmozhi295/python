# function definition

def hello_world():
   print("hi")

# function calling
hello_world()  


# arguments in function

def func(name):
   print("Hi",name)

func("vijay")


def my_func():
    x=10
    print("value inside function:",x)
x=20
my_func()
print("value outside function:",x)


#example of a user defined function

def add_numbers(x,y):
    sum=x+y
    return sum

num1=5
num2=6

print("The sum is",add_numbers(num1,num2))


#example of a build in function

print(format(123, "d"))

#binary format
print(format(12, "b"))
