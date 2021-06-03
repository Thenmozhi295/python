
#lists
a =[23,22,1,-229,65]
a.append(22)
print(a)
a.insert(0,1)
print(a)
a.remove(-229)
a.reverse()
print(a)

#using lists as stack and queue

x=[1,2,3,4,5,6,7]
print(x)

x.pop(0)
x.pop(1)
print(x)

x.append(3)
print(x)


#tuples

a=('fedora','ubuntu','debian')

print(a)

print(type(a))

#sets

a = set('abcdefghijkl')
b = set('pqrstuvwxyz')
print(a,b)


print(a-b)

#dictionaries

data={'actor_:vijay','os:ubuntu'}
print(data)



del data['actor_']
print(data)


