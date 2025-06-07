import pandas as pd
import pandas_ta as ta
import talib as Ta

class Technical_Indicators():
    def __init__(self,df:pd.DataFrame):     # class constructor
       self.df=df.copy()
        
    def SMA(self,period=10):               
        try:
         
         self.df[f"SMA:{period}"]=Ta.SMA(real=self.df["Close"],timeperiod=period)
         return self.df
         # self.df.to_csv(self.filename,index=False)
        except Exception as e:
          print("Exception occured:",e)  
    def EMA(self,period:int=10):
       try:
         
         self.df[f"EMA:{period}"]=Ta.EMA(real=self.df["Close"],timeperiod=period)
         return self.df
        # self.df.to_csv(self.filename,index=False)
       except Exception as e:
          print("Exception occured:",e)  
    def RSI(self,period:int=10):                                              #Momentum oscillator
       try:
         
         self.df[f"RSI:{period}"]=Ta.RSI(real=self.df["Close"],timeperiod=period)
         return self.df
         #self.df.to_csv(self.filename,index=False)
       except Exception as e:
          print("Exception occured:",e)
    def MACD(self, fast: float = 12, slow: float = 26, signal: float = 9):  # Momentum and trend indicator
     try:
        macd_line, macd_signal, macd_hist = Ta.MACD(real=self.df["Close"],
                                                    fastperiod=fast,
                                                    slowperiod=slow,
                                                    signalperiod=signal)
        
        macd_df = pd.DataFrame({
            f"MACD_{fast}_{slow}_{signal}": macd_line,
            f"MACDh_{fast}_{slow}_{signal}": macd_hist,
            f"MACDs_{fast}_{slow}_{signal}": macd_signal
        }, index=self.df.index)

        self.df = pd.concat([self.df, macd_df], axis=1)
        return self.df

     except Exception as e:
        print("Exception Occurred:", e)
    def OBV(self):                                                            #volume indicator
       try:
         self.df["OBV"]=Ta.OBV(self.df["Close"],self.df["Volume"])    
         return self.df 
       except Exception as e:
          print("Exception occured:",e)  
    def Accumulation_Distribution(self):                                      #volume indicator
     try:
         self.df["Accumulation_Distribution"]=Ta.AD(high=self.df["High"],
                                                    low=self.df["Low"],
                                                    close=self.df["Close"],
                                                    volume=self.df["Volume"])    
         return self.df
     except Exception as e:
          print("Exception occured:",e)  
    def Bollinger_Bands(self, period=20, up=2, down=2):
     try:
        upperband, middleband, lowerband = Ta.BBANDS(
            self.df["Close"],
            timeperiod=period,
            nbdevup=up,
            nbdevdn=down
        )
        bb = pd.DataFrame({
            f'BB_upper_{period}': upperband,
            f'BB_middle_{period}': middleband,
            f'BB_lower_{period}': lowerband,
        }, index=self.df.index)
        self.df = pd.concat([self.df, bb], axis=1)
        return self.df
     except Exception as e:
        print("Exception occurred:", e)
    def ADX(self,length=14):                                                 #Trend strength measurement
     try:
        adx =Ta.ADX(self.df["High"], self.df["Low"], self.df["Close"],timeperiod=length)
        self.df = pd.concat([self.df, adx], axis=1)
        return self.df
     except Exception as e:
        print("Exception occurred:", e)
    def SuperTrend(self,length=10,Multiplier=3):   
       try:                           #trend indicator
        supertrend=ta.supertrend(high=self.df["High"],
                                 low=self.df["Low"],
                                 close=self.df["Close"],
                                 length=length,
                                 multiplier=Multiplier)
        self.df = pd.concat([self.df, supertrend], axis=1)
        
        return self.df
       except Exception as e:
          print("Exception occurred:", e)  
    def ATR(self,period=14):
       try:
        self.df[f"ATR:{period}"]=Ta.ATR(high=self.df["High"],low=self.df["Low"],close=self.df["Close"],timeperiod=period)
        return self.df
       except Exception as e:
          print("Exception occurred:", e)  
       
    def Run_All_With_DefaultValues(self):
       self.SMA(20) 
       self.SMA(50)
       self.EMA()
       self.RSI()
       self.MACD()
       self.OBV()
       self.Accumulation_Distribution()
       self.Bollinger_Bands()
       self.ADX()
       self.SuperTrend()
       self.ATR()   
       
       return self.df   
       
       
#These are for temporary purpose to check logic other this class will be 
# controlled from Main_Control.py


