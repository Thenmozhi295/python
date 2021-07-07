#basic program

import pandas as pd
s= pd.Series()
print(s)

#create a series from ndarray

import pandas as pd
import numpy as np
data = np.array(['a','b','c','d','e'])
s=pd.Series(data)
print(s)

#another example

import pandas as pd
import numpy as np
data = np.array(['a','b','c','d','e'])
s=pd.Series(data,index=[100,101,102,103,104])
print(s)

