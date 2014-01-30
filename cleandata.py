import pandas as pd
import sys
import pandas as pd
import numpy as np

def largeinthelper(idx):
    def handlelargeint(x):
        if type(x) == str:
            return np.log( float(x[:len(x)-idx] + "."  + x[len(x)-idx:]))
        return x
    return handlelargeint

g = np.vectorize(largeinthelper(10))



nr = 10000
df = pd.read_csv("train.csv",  index_col=0, nrows=nr, low_memory=False)
dtypes = [(h, df[h].dtype ) for h in df.columns if df[h].dtype not in (np.float64, np.int64) ]
for h, dh in dtypes:
    df[h] = g(df[h])    

W = df.apply(lambda x: pd.notnull(x).sum(), axis=0)
print W[W != nr].to_string()
print len(W)

#h0 = dtypes[0][0]

#print df
