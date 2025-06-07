import pandas as pd
import numpy as np
import matplotlib.pyplot as plot 

series=pd.Series(['navjot singh','gurjinder kaur',
                'viraj singh nangal','jasraj singh nangal'],
                name="NAME",
                index=["HEAD OF FAMILY",'WIFE','ELDER SON','YOUNGER SON'],
                copy=True,
                dtype="string")

result=series.isin(["viraj singh nangal"])
print(result.astype("string").str.count("True").sum())
series.replace(to_replace="viraj singh nangal",value="singh",inplace=True)
series.sort_values(inplace=True,ignore_index=True,
                   )
print(pd.date_range(start="1-1-2025",periods=5,freq="ME").dayofweek)
print(series.str.upper())
