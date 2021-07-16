#example:1
#.loc()
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

#select all rows for a specific column
print (df.loc[:,'A'])
print (df.loc[:,['A','C']])
# Select few rows for multiple columns, say list[]
print (df.loc[['a','b','f','h'],['A','C']])
# Select range of rows for all columns
print (df.loc['a':'h'])

#example:2 .iloc()


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# select all rows for a specific column
print (df.iloc[:4])
print (df.iloc[:4])
print (df.iloc[1:5, 2:4])

#example:3 .ix()

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# Integer slicing
print (df.ix[:4])
