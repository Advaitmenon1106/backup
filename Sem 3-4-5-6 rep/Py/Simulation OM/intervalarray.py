arr = [0-1, 1-5, 6-7]
print (arr)
import pandas as pd
df = pd.DataFrame({
    "Days": [1, 2, 3, 4, 5, 6, 7],
    "Col 2": [1, 4, 7, 12, 0, 21, 2]
})
df.set_index("Days", inplace= True)
print (df[1])
print (df)