
import pandas as pd
left=pd.DataFrame({'id':[1,2,3,4],'Name':['John','parker','smith','Dev']})
right=pd.DataFrame({'id':[1,2,3,4],'Name':['William','Albert','Tony','Allen']})
print(left)
print(right)

#Merge two DataFrames on multiple keys

import pandas as pd
left=pd.DataFrame({'id':[1,2,3,4],'Name':['John','parker','smith','Dev'],'subject_id':['sub1','sub2','sub4','sub6']})
right=pd.DataFrame({'id':[1,2,3,4],'Name':['William','Albert','Tony','Allen'],'subject_id':['sub2','sub4','sub3','sub7']})
print(pd.merge(left,right,on='id'))


