import csv
import json
import requests
import datetime
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit.components.v1 as components
from p1 import*

def getgraph(t1,t2,symbol):
    df=get_data()
    mask1=df["date"]>=t1#[T,F,T.......]
    mask2=df["date"]<=t2#[T,F,T.......]
    mask3=df["symbol"]==symbol
    l=mask1 & mask2 & mask3
    df1=df[l]
    return df1
