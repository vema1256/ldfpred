import pandas  as pd
import numpy as np
import sys

TRAINFNM = "C:\Users\MaheshV\Downloads\\dp\\train.csv"
chunk = pd.read_csv(TRAINFNM, index_col=0, nrows=10)
print chunk.columns
columnnames = chunk.columns

def largeinthelper(idx):
    def handlelargeint(x):
        if type(x) == str:
            return np.log( float(x[:len(x)-idx] + "."  + x[len(x)-idx:]))
        return x
    return handlelargeint

transform2float = np.vectorize(largeinthelper(10))

mnvec = []
sdvec = []
objcolnames = []

for i in np.arange(len(columnnames) - 5, len(columnnames) + 1):
    feature = columnnames[i-1]
    chunkcol = pd.read_csv(TRAINFNM, index_col=0, usecols=[0,i] )[feature]
    
    if( chunkcol.dtype in (np.float64, np.int64, np.float, np.int) ):
        pass
    else:
        chcol_ = transform2float( chunkcol )
        chunkcol  = pd.Series( chcol_, index = chunkcol.index)
        objcolnames.append( feature)

    mn = chunkcol.dropna().mean() 
    sd =  chunkcol.dropna().std() 
    
    mnvec.append( mn )
    sdvec.append( sd )

outfile = "normmoments.npz"
np.savez(outfile, np.array(mnvec), np.array(sdvec), np.array(objcolnames))
        
