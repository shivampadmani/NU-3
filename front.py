import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import json
import requests
from p2 import*
from p1 import*

st.title("OHLC Engine Dashboard")
st.markdown("The dashboard will help to know \
more about the given datasets and it's output")

st.sidebar.title("Select Visual Charts")
st.sidebar.markdown("Select the Chart accordingly:")

chart_visual = st.sidebar.selectbox('Select Chart type',('OHLC Chart','Candlestick Chart','Hollow Candle Chart'))

company_visual = st.sidebar.selectbox('Select Company Symbol',get_sym())


t1=st.text_input("Enter start time","2021-01-01")
t2=st.text_input("Enter end time","2021-08-20")
data=getgraph(t1,t2,company_visual)

if chart_visual == 'OHLC Chart':
	fig=go.Figure(data=[go.Ohlc(x=data["date"],open=data["open"], high=data["high"],low=data["low"], close=data["close"])])
	fig.update_layout(title='OHLC Chart for '+company_visual+' Price for '+t1+' to '+t2)
	fig.update_xaxes(title_text='Date')
	fig.update_yaxes(title_text=company_visual+' Price',tickprefix='$')

elif chart_visual == 'Candlestick Chart':
	fig=go.Figure(data=[go.Candlestick(x=data["date"],open=data["open"], high=data["high"],low=data["low"], close=data["close"])])
	fig.update_layout(title='OHLC Chart for '+company_visual+' Price for '+t1+' to '+t2)
	fig.update_xaxes(title_text='Date')
	fig.update_yaxes(title_text=company_visual+' Price',tickprefix='$')

elif chart_visual == 'Hollow Candle Chart':
	fig=go.Figure(data=[go.Candlestick(x=data["date"],open=data["open"], high=data["high"],low=data["low"], close=data["close"],increasing_line_color= 'red', decreasing_line_color= 'green')])
	fig.update_layout(title='OHLC Chart for '+company_visual+' Price for '+t1+' to '+t2)
	fig.update_xaxes(title_text='Date')
	fig.update_yaxes(title_text=company_visual+' Price',tickprefix='$')

st.plotly_chart(fig)
