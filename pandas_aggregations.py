#example 1

import pandas as pd  
import numpy as np  
df=pd.DataFrame([[1,5,7],[10,12,15],[18,21,24],[np.nan,np.nan,np.nan]],columns=['X','Y','Z'])  
print(df)
print(df.agg(['sum','min'])) 

#example 2
import pandas as pd  
import numpy as np  
df=pd.DataFrame([[1,5,7],[10,12,15],[18,21,24],[np.nan,np.nan,np.nan]],columns=['A','B','C'])  
print(df.agg({'A':['sum', 'min'],'B':['min', 'max']}))

#example 3

import pandas as pd  
import numpy as np  
df=pd.DataFrame([[1,5,7],[10,12,15],[18,21,24],[np.nan,np.nan,np.nan]],columns=['A','B','C'])
print(df.agg("mean", axis="columns"))
print(df.agg("mean", axis="rows"))

