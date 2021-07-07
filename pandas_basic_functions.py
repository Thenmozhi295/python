#basic program

import pandas as pd
import numpy as np

#create a series with 100 random numbers
s=pd.Series(np.random.randn(4))
print(s)

#axes

import pandas as pd
import numpy as np
s=pd.Series(np.random.randn(4))
print("The axes are:",s.axes)

#empty

import pandas as pd
import numpy as np
s=pd.Series(np.random.randn(4))
print("Is the object empty?:",s.empty)

#ndim

import pandas as pd
import numpy as np
s=pd.Series(np.random.randn(4))
print(s)
print("The dimensions of the object:",s.ndim)

#size

import pandas as pd
import numpy as np
s=pd.Series(np.random.randn(4))
print(s)
print("The size of the object:",s.size)

#values

import pandas as pd
import numpy as np
s=pd.Series(np.random.randn(4))
print(s)
print("The actual data series is:",s.values)

#head&tail

import pandas as pd
import numpy as np
s=pd.Series(np.random.randn(4))
print("The original series is:")
print(s)

print("The first two rows of the data series:",s.head(2))

print("The last two rows of the data series:",s.tail(2))

