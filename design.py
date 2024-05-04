import streamlit as st

airline_name = st.selectbox('AirLines',("Air_India","GoAir","Indigo","Spicejet","Trujet","Vistara","Vistara_premium_economy"),str = 'Choose an option')
num_of_stops = st.selectbox("Number of Stops",("0","1","2","3"))
dep_date = st.date_input("Departure Date")
arr_date = st.date_input
source = st.text_input('Source')