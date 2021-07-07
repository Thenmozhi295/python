#basic programs

import pandas as pd
data={"calories":[420,380,390],
      "duration":[50,40,45]}
df=pd.DataFrame(data)
print(df)

#example locate row

import pandas as pd
data={"calories":[420,380,390],
      "duration":[50,40,45]}
df=pd.DataFrame(data)
print(df.loc[0])

# named indexes

import pandas as pd
data={"calories":[420,380,390],
      "duration":[50,40,45]}
df=pd.DataFrame(data,index=["day1","day2","day3"])
print(df)
