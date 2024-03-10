import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

#Berkas data day.csv
day_df = pd.read_csv("https://raw.githubusercontent.com/aryarevansyah23/Proyek-Analisis-Data/main/Data/day.csv")

#Datetime untuk data
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

#function_weahter_data()

with st.sidebar:
    #Keterangan
    st.header("File you should check:")
    st.subheader("Kondisi Cuaca Setiap Bulan")
    st.subheader("Pengguna Sepeda Setiap Bulan")
    st.subheader("Pengguna sepeda setiap Minggu")

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

plt.title("Kondisi Cuaca dalam Setiap Bulan")
plt.xlabel("Waktu dalam Setiap Bulan")
plt.ylabel("Jumlah Nilai")
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
plt.xlabel("Waktu dalam Setiap Bulan")
plt.ylabel("Jumlah Pengguna")
plt.xticks(month_data['dteday'], labels = month_data['dteday'].dt.strftime('%b %Y'), rotation = -90)
plt.legend()
st.pyplot(fig)

st.text(
    """
    Pada kedua grafik yang telah disajikan dapat terlihat bahwa kedua grafik tersebut 
    menunjukkan korelasi yang signifikan dengan perubahan kondisi cuaca selama periode 
    desember hingga februari. Grafik pertama menunjukkan kecepatan angin yang meningkat,
    serta temperatur dan humidity yang rendah secara mencolok. Grafik kedua menunjukkan 
    tren Recency, Frequency, dan Monetary (RFM) dengan peminjaman mengalami penurunan 
    sejak sebelum periode desember. Pada awal bulan november pengguna total sebanyak 4068 
    dan turun pada awal desember sebanyak 3727. Peminjaman pun mengalami penurunan hingga 
    titik terendah sekitar bulan desember hingga februari.

    Korelasi tersebut menunjukkan kondisi cuaca yang tidak menguntungkan dapat memberikan 
    pengaruh yang signifikan terhadap aktivitas peminjaman sepeda.
    """
)

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
plt.xlabel("Waktu dalam Seminggu")
plt.ylabel("Jumlah pengguna")
plt.xticks(week_data['weekday'], labels=weekday_names)
plt.legend()
st.pyplot(fig)

st.text(
    """
    Pada grafik pengguna sepeda setiap minggunya, menunjukkan tren yang menarik dari 
    pengguna registered dan pengguna kasual. Pada hari kerja (Senin-Jumat), pengguna 
    registered menunjukkan kecenderungan peningkatan dan pengguna kasual menunjukkan 
    penurunan. Sedangkan, pada hari libur (Sabtu-Minggu), pengguna registered 
    menunjukkan kecenderungan penurunan dan pengguna kasual menunjukkan peningkatan.

    Hal tersebut menunjukkan bahwa pengguna registered merupakan masyarakat sekitar 
    yang menggunakan sepeda untuk menunjang kegiatan sehari-hari mereka untuk bekerja. 
    Sedangkan, pengguna kasual merupakan masyarakat pendatang yang berjalan-jalan dengan 
    menggunakan sepeda. Melihat fenomena ini cukup penting untuk melakukan pendekatan 
    kepada peminjam berdasarkan pengguna sepeda setiap harinya.
    """
)