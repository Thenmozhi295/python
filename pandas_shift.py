#example:

import pandas as pd  
info= pd.DataFrame({'a_data': [45, 28, 39, 32, 18],  
'b_data': [26, 37, 41, 35, 45],  
'c_data': [22, 19, 11, 25, 16]})  
info.shift(periods=2)  
print(info.shift(2))


#fill the missing values in dataframe using fill_value

import pandas as pd  
info= pd.DataFrame({'a_data': [45, 28, 39, 32, 18],  
'b_data': [26, 38, 41, 35, 45],  
'c_data': [22, 19, 11, 25, 16]})  
info.shift(periods=2)  
info.shift(periods=2,axis=1,fill_value= 70)  
print(info)
