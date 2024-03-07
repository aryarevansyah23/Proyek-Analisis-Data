import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

#Berkas data day.csv
day_df = pd.read_csv("C:/Users/Arya Revansyah/Documents/BANGKIT/MATERI/MATERI INTI/3. BELAJAR ANALISIS DATA DENGAN PYTHON/PROYEK ANALISIS DATA/Proyek_Analisis_Data/day.csv")

#Datetime untuk data
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

#function_weahter_data()

#Judul Dashboard
st.title("Dashboard Bike Sharing")

#Header Dashboard
st.header("Bike Sharing Demand")

#Visualisasi Kondisi Cuaca
st.subheader("Kondisi Cuaca Setiap Bulan")

weather_data = day_df.groupby(day_df['dteday'].dt.to_period('M')).agg({
    'temp' : 'sum',
    'hum' : 'sum',
    'windspeed' : 'sum'
}).reset_index()

weather_data['dteday'] = weather_data['dteday'].dt.to_timestamp()

fig = plt.figure(figsize=(10, 5))

plt.plot(weather_data['dteday'], weather_data['temp'], label = 'Temperature')
plt.plot(weather_data['dteday'], weather_data['hum'], label = 'Humidity')
plt.plot(weather_data['dteday'], weather_data['windspeed'], label = 'Wind Speed')

plt.title("Weather Condition in Month")
plt.xticks(weather_data['dteday'], labels = weather_data['dteday'].dt.strftime('%b %Y'), rotation = -90)
plt.legend()
st.pyplot(fig)

#Visualisasi Pengguna Bulan
st.subheader("Pengguna Sepeda Setiap Bulan")

month_data = day_df.groupby(day_df['dteday'].dt.to_period('M')).agg({
    'casual' : 'sum',
    'registered' : 'sum',
    'cnt' : 'sum'
}).reset_index()

month_data['dteday'] = month_data['dteday'].dt.to_timestamp()

fig = plt.figure(figsize=(10, 5))

plt.plot(month_data['dteday'], month_data['casual'], label = 'Casual')
plt.plot(month_data['dteday'], month_data['registered'], label = 'Registered')
plt.plot(month_data['dteday'], month_data['cnt'], label = 'Total')

plt.title("Bike Sharing per Month")
plt.xticks(month_data['dteday'], labels = month_data['dteday'].dt.strftime('%b %Y'), rotation = -90)
plt.ylabel('Jumlah Bike Sharing')
plt.legend()
st.pyplot(fig)

#Visualisasi Pengguna Minggu
st.subheader("Pengguna Sepeda Setiap Minggu")

week_data = day_df.groupby(day_df['weekday']).agg({
    'casual' : 'sum',
    'registered' : 'sum',
    'cnt' : 'sum'
}).reset_index()

fig = plt.figure(figsize=(10, 5))

plt.plot(week_data['weekday'], week_data['casual'], label='Casual')
plt.plot(week_data['weekday'], week_data['registered'], label='Registered')
plt.plot(week_data['weekday'], week_data['cnt'], label='Total')

weekday_names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

plt.title("Bike Sharing per Week")
plt.xticks(week_data['weekday'], labels=weekday_names)
plt.ylabel('Number of Bike Sharing')
plt.legend()
st.pyplot(fig)