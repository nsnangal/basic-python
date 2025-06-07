import pandas as pd
import time

df = pd.DataFrame({'Open': [100]*100000, 'Close': [110]*100000})

# apply()
#start = time.time()
#df['Profit_apply'] = df.apply(lambda row: row['Close'] - row['Open'], axis=1)
#print(f"apply(): {time.time() - start:.4f} sec")

# vectorized
start = time.time()
df['Profit_vec'] = df['Close'] - df['Open']
print(f"vectorized: {time.time() - start:.4f} sec")
print(df.to_numpy())