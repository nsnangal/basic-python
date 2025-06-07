import pandas as pd
import Cleaning_DataSets as cd
import IndicatorRunner as Strategy
from logging_manager import LoggerManager
from Signal_generator import SignalGenerator

logger=LoggerManager().get_logger()

# Load CSV data into DataFrame with specified dtypes

@LoggerManager.log_function_call()
def App_Load():
 
 filepath=r"C:\Users\Navjot Singh\Desktop\python\Trading_Automation_APP\DataSets\RELIANCE.csv"
 df_raw=pd.read_csv(filepath,
               dtype={"Symbol":"string",
                      "Series":"string",
                      "Prev Close":"float64",
                      "Open":"float64",
                      "High":"float64",
                      "Low":"float64",
                      "Last":"float64",
                      "Close":"float64",
                      "VWAP":"float64",
                      "Deliverable Volume":"float64",
                      "%Deliverable":"float64"})
 df_raw["Date"]=pd.to_datetime(df_raw["Date"])

 # Clean the data using custom cleaning module
 if df_raw is not None:
     
     Cleaner=cd.StockData_Cleaning(df_raw,filename=filepath)
     df_Cleaned=Cleaner.data_cleaning()

 #Just a Random testdata for checking core logic
     if df_Cleaned is None:
      logger.warning(f"df_Cleaned dataframe is Ready for run_indicator:-{df_Cleaned is not None}")  
      return
     
     testdata=[{
            'name': 'RSI',
            'source': 'talib',
            'input_sets': [ {'close': df_Cleaned["Close"]}],
            'param_grid': { 'timeperiod': [14,21,28,42,45] }
        },{
        'name': 'MACD',
        'source': 'talib',
        'input_sets': [{'close': df_Cleaned["Close"]}],
        'param_grid': {
            'fastperiod': [12,24],
            'slowperiod': [26,52],
            'signalperiod': [9,18]
             }
     }
     ]

     Runner=Strategy.UniversalIndicatorRunner()
     Runner.run_indicators(testdata)
     indicator_output=Runner.get_result_by_key(Runner.keystore)
     logger.info(f"Indicator Output Generated Successfully:-{indicator_output is not None}")
     
     Signal_Generation=SignalGenerator(Runner.results)
     Signal_Generation.generate_signals()
     logger.info(f"Signals Generated Successfully:-{Signal_Generation.get_signals() is not None}")
      
 else:
       logger.warning("Dataframe is Empty")


if __name__=="__main__":
 try:
  App_Load()
 except Exception as e:
    logger.error(f"Exception Occured in Main_Control.py:-{e}")
    






