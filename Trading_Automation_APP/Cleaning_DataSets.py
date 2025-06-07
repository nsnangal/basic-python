import pandas as pd
from logging_manager import LoggerManager
import logging


class StockData_Cleaning:
 
 @LoggerManager.log_function_call(logging.INFO)
 def __init__(self,df:pd.DataFrame,filename:str):
   try:
    self.df=df
    self.filename=filename
    self.logger=LoggerManager().get_logger()
   except Exception as e:
     self.logger.error(f"Exception occurred in Stockdata_cleaning constructor:{e}")

 @LoggerManager.log_function_call(logging.INFO)
 def data_cleaning(self):                           
  try: 
     if "Trades" in  self.df.columns:
       self.df.drop(["Trades"],inplace=True,axis=1) 
       self.df.dropna(axis=0,how="any",inplace=True)
       self.df.to_csv(self.filename,index=False)
     return self.df
    
  except Exception as e:
      self.logger.error(f"Exception occurred in Stockdata_cleaning data_cleaning:{e}")