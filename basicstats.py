import pandas as pd
import sys


for chunk in pd.read_csv("train.csv", iterator=True, index_col=0, chunksize=10000, low_memory=False):
    #print len(chunk)
    print set(chunk["loss"])
    print len(chunk.columns)
    #sys.exit()