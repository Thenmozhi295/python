#Example:1

import pandas as pd
s = pd.Series(["a","b","c","a"], dtype="category")
print(s)

#example:2
import pandas as pd
info = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
info = info=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'])
print(info)

#example:3
import pandas as pd
info = info=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'],ordered=True)
print(info)

#example:4
import pandas as pd
import numpy as np
info = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
df = pd.DataFrame({"info":info, "s":["a", "c", "c", np.nan]})
print(df.describe())
print(df["info"].describe())

#example:5

import pandas as pd
s = pd.Series(["a","b","c","a"], dtype="category")
print ("Original object:")
print(s)

print("After removal:")
print(s.cat.remove_categories("a")
