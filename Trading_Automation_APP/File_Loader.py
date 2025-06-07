import glob,os
import tkinter as tk
from tkinter import filedialog


def select_file():                                  
  filenames=glob.glob(r"C:\Users\Navjot Singh\.cache\kagglehub\datasets\rohanrao\nifty50-stock-market-data\versions\15\*.csv")
  root=tk.Tk()
  root.withdraw()
  filepath=filedialog.askopenfilename(title="Select a CSV file")
  root.destroy()
  if filepath.endswith("csv"):
    return filepath
  else:
   print("You didn't select a file or wrong file")
   exit()
