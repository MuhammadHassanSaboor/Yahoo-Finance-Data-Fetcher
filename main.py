import pandas as pd
import streamlit as st
import yfinance as yf
from datetime import date
from io import StringIO


st.title("Yahoo Finance Data Fetcher")
st.sidebar.header("Stock Ticker Input")
ticker = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, MSFT):", "")

default_start_date = date(1900,1,1)
default_end_date = date.today()

start_date = st.sidebar.date_input("Start Date" , default_start_date)
end_date = st.sidebar.date_input("End Date", default_end_date)

if st.sidebar.button("Fetch Data"):
    if ticker.strip():
        try:
            df = yf.download(
                ticker,
                start=start_date,
                end = end_date,
                auto_adjust = False
            )
            
            if not df.empty:
                st.success(f"Data for {ticker.upper()} fetched successfully")
                
                df.columns = df.columns.get_level_values(0)
                
                df.reset_index(inplace = True)
                
                df['Date'] = pd.to_datetime(df['Date'])
                
                df['Year'] = df['Date'].dt.year 
                df['Month'] = df['Date'].dt.month
                df['Day'] = df['Date'].dt.day 
                
                st.title("Top 5 Rows")
                st.dataframe(df.head())
                st.title("Last 5 Rows")
                st.dataframe(df.tail())
                st.title("Sample of Data")
                st.dataframe(df.sample(5))
                
                col1 , col2 , col3 = st.columns(3)
                
                with col1:
                    st.markdown("<h3 style = 'fontsize: 30px;'> Columns</h3>",unsafe_allow_html=True)
                    st.write(df.columns)
                    
                with col2:
                    st.markdown("<h3 style = 'fontsize: 30px;'> Null Values</h3>",unsafe_allow_html=True)
                    st.write(df.isnull().sum())
                    
                with col3:
                    st.markdown("<h3 style = 'fontsize: 30px;'> Data Types</h3>",unsafe_allow_html=True)
                    st.write(df.dtypes)
                
                st.title("Duplicate Instances")
                st.dataframe(df[df.duplicated()])
                
                st.title("Download the Dataset")
                
                csv = df.to_csv(index = False)
                st.download_button(
                    label = "Download CSV",
                    data = csv,
                    file_name = f"{ticker}_data.csv",
                    mime = "text/csv",
                    
                )
            
            else:
                st.error("No data found for the entered ticker. Please check the ticker and date range.")
                
        except Exception as e:
            st.error(f"An error occured: {e}")
    
    else:
        st.warning("Please enter a valid stock ticker.")
            