import csv
import json
import requests
import datetime
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
import plotly.graph_objects as go

data=json.load(open('Stock List.json'))
def get_data():
    df=pd.DataFrame(data,columns=["date","open","high","low","close","symbol"])
    df.sort_values(by="date")
    return df
def get_sym():
    df=get_data()
    return df["symbol"].unique()

