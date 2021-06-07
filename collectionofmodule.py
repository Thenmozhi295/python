#counter()

from collections import Counter
c=Counter()
list=[1,2,3,4,5,6,7]
Counter(list)
Counter({1:5,2:4})
list=[1,2,4,7,1,6,7,6,9,1]
c=Counter(list)
print(c[1])

#namedtuple()

from collections import namedtuple

hello=('thor',22,'m')
print(hello)

#orderedDict()

import collections

d1=collections.OrderedDict()
d1['A']=22
d1['B']=29
d1['C']=06
d1['D']=25

for s,r in d1.items():
   print(s,r)
