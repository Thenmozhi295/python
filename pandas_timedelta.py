#Example:

import pandas as pd

print(pd.Timedelta('3 days 3 hours 15 minutes 30 seconds'))


#Integer

import pandas as pd
print(pd.Timedelta(22,unit='h'))
print(pd.Timedelta(29,unit='h'))

#Data Offsets

import pandas as pd

print(pd.Timedelta(days=5))

#Operations

import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
print(df)

#Addition Operations

import pandas as pd

s = pd.Series(pd.date_range('2020-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
df['C']=df['A']+df['B']

print(df)


#Subtraction Operation

import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
df['C']=df['A']+df['B']
df['D']=df['C']+df['B']
print(df)
