import numpy as np
from numpy.random import default_rng
import pandas as pd

df=pd.DataFrame(columns=["NAME","MATH MARKS","SCIENCE MARKS","ENGLISH MARKS","SST MARKS"])
df.loc[0]=["NAVJOT SINGH",23,23,33,44]
df.loc[1]=(["abc",44,77,99,33])
df=df[["MATH MARKS","SCIENCE MARKS","ENGLISH MARKS","SST MARKS"]]
result=df.to_numpy()
totalmarks=result.sum()                         #overall sum of all elements but by using axis row-wise or col-wise sum possible
averagestudent=result.mean(axis=1)              #similarly average can be performed on three aspects as above with axis value
averagesubjectwise=result.mean(axis=0)
highest=result[:,:3].max()                        #Column specific is possible with the help of slicing.
lowest=result.min(axis=0)                         #minimum of each col with axis=0  
nopassstudents=(result>=33).cumsum().max()          
average=result.mean(axis=0)
print(average)
indices=np.argsort(-average)
print(indices)
print(result[:,indices])                            #column shifting w.r.t average of columns
#result.sort(axis=1)                                #Sort by two axis(row-wisw & col-wise) only and *return is nothing 
print(df) 
rng=default_rng(seed=42)
print(rng.uniform(5,10,(2,3)))
print(average) 
"""                  
print(totalmarks)
print(averagestudent)


print(averagesubjectwise)
print(highest)
print(lowest)
print(nopassstudents)
"""
print(result)