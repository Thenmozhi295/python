
import pandas as pd
import numpy as np

s = pd.Series(['Shaheer', 'William', 'John', 'Alber@t', np.nan, '1234','Dev'])
print(s)

#lower()

import pandas as pd
import numpy as np

s = pd.Series(['Shaheer', 'William', 'John', 'Alber@t', np.nan, '1234','Dev'])
print(s.str.lower())

#upper()

import pandas as pd
import numpy as np

s = pd.Series(['Shaheer', 'William', 'John', 'Alber@t','Dev'])
print(s.str.upper())

#len()

import pandas as pd
import numpy as np

s = pd.Series(['Shaheer', 'William', 'John', 'Alber@t','Dev'])
print(s.str.len())

#strip()

import pandas as pd
import numpy as np

s = pd.Series(['Shaheer', 'William', 'John', 'Alber@t','Dev'])
print(s)
print(s.str.strip())

#split(pattern)

import pandas as pd
import numpy as np

s = pd.Series(['Shaheer', 'William', 'John', 'Alber@t','Dev'])
print(s)
print("split pattern:")
print(s.str.split(' '))


