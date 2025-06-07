import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import BackTester.strategy_backtester as sb


fig,ax=plt.subplots(2,2,figsize=(12,6))
def plot_line_chart(monthly_expenses,category_expenses):
 
 
  monthly_expenses.plot(kind='bar',ax=ax[0,0]) 
  ax[0,0].set_title("MONTHLY EXPENDITURE")
  ax[0,0].set_xlabel("MONTHS")
  ax[0,0].set_ylabel("EXPENDITURE(Rs.)")
  ax[0,0].grid(axis='y',linestyle="-")
 
  category_expenses.plot(kind='bar',ax=ax[0,1]) 
  ax[0,1].set_title("category wise expenditure")
  ax[0,1].set_xlabel("category")
  ax[0,1].set_ylabel("EXPENDITURE(Rs.)")
  ax[0,1].grid(axis='y',linestyle="-")
 
  #plt.xticks(rotation=45) 
  plt.tight_layout()
  plt.show()
 
#read csv file
df=pd.read_csv("expenses.csv")

#set datatypes 
df["DATE"]=pd.to_datetime(df["DATE"])
df["CATEGORY"]=df['CATEGORY'].astype('category')
df["DESCRIPTION"]=df['DESCRIPTION'].astype('string')
df["AMOUNT"]=df['AMOUNT'].astype('float32')


#Total monthly expense
df["MONTH"]=df['DATE'].dt.month_name()
monthly_expenditure=df.groupby("MONTH")["AMOUNT"].sum()
print(monthly_expenditure)

#Total annually expenses
print(monthly_expenditure.sum())

#category wise max expenses
max_expenses_category=df.groupby("CATEGORY",observed=True)["AMOUNT"].sum()
print(max_expenses_category)

#Daily average expenses
average_expenses=df['AMOUNT'].mean()
print(average_expenses)

#plot charts
plot_line_chart(monthly_expenditure,max_expenses_category)

#add new row 
df.loc[len(df)]=["2025-06-04","Entertainment","Netflix Subscription",499,"July"]

#add column
df["trial"]=[None]*6

#delete none columns
df.dropna(axis=1,thresh=6,ignore_index=True,inplace=True)

#modify row data
df.loc[df["CATEGORY"].str.startswith('Enter'),["CATEGORY"]]="aaaa"

print(df)










  
