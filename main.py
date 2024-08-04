
import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])

for item in s:
    print(item)


print("This line will be printed.")