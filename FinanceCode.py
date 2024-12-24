import streamlit as st 
import yfinance as yf
import pandas as pd

st.write(""" # Simple Stock Price Application
Shown are the Stock **clothing Price** and **volume** of Google
""")

TrickerSymbol = 'AApl'
TrickerData = yf.Ticker(TrickerSymbol)
TrickedDf = TrickerData.history(period='1d',start='2010-5-31',end='2023-5-31')

st.write(""" ## Closing Price """)
st.line_chart(TrickedDf.Close)
st.write(""" ## Volume Price """)
st.line_chart(TrickedDf.Volume)


