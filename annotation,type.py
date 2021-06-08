#Ex1

def fib(n: 'int', output: 'list'=[])-> 'list':
    if n == 0:
        return output
    else:
        if len(output)<2:
          output.append(1)
          fib(n-1, output)
        else:
          last = output[-1]
          second_last = output[-2]
  	  output.append(last + second_last)
          fib(n-1, output)
        return output
print(fib(5))

#Ex2
from typing import List,Tuple, Sequence, Optional

values: List[int] = []
city: int = 350


def get_details()-> Tuple[str, int]:
   return "python", 5

name: str
marks: int
name, marks = get_details()

def print_all(values: Sequence) -> None:
   for v in values:
      print(v)

print_all([1,2,3])
print_all({"name": "kushal","class": 5})

def add_ten (number: Optimal[int] = None) ->int:
   if number:
     return number + 10
   else:
     return 42
print(add_ten())
print(add_ten(12))


#Example program in type hinting
def factorial(i: int) -> int:
   if i<0:
     return None
   if i == 0:
     return 1
   return 1 * factorial(i-1)

print(factorial(5.01))

