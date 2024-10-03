# Bagian ini adalah kumpulan aksi untuk membuat pivot table sebelum dipakai untuk
# pembuatan chart atau table

import streamlit as st
import pandas as pd
# import subprocess

#buka file upload dr cleaning dan home.py
df=pd.read_csv('df_cleaned_multifiltered.csv')
df=pd.to_datetime(df)

# Membuat tabel pivot by DATE---------------
# pivot_df_tanggal= pd.pivot_table(df, values=['NG%'], index='Date', aggfunc={'NG%': 'mean'})

# pivot_df_tanggal.index = pd.to_datetime(pivot_df_tanggal.index, format='%d-%b')

# # Urutkan DataFrame berdasarkan kolom 'Date'
# pivot_df_tanggal.sort_index(inplace=True)

# # Reset index untuk memudahkan plotting
# pivot_df_tanggal.reset_index(inplace=True)

# pivot_df_tanggal.to_csv('pivot_df_tanggal.csv',index=False)

# Membuat tabel pivot by MONTH---------------
pivot_df_bulan= pd.pivot_table(df, values=['TotInsp(Lot)', 'NG%'], index='Month', aggfunc={'TotInsp(Lot)': 'sum', 'NG%': 'mean'})

# pivot_df_bulan.index = pd.to_datetime(pivot_df_bulan.index, format='%b-%Y')

# Urutkan DataFrame berdasarkan kolom 'Month'
pivot_df_bulan.sort_index(inplace=True)

# Reset index untuk memudahkan plotting
pivot_df_bulan.reset_index(inplace=True)

pivot_df_bulan['Month'] = pivot_df_bulan['Month'].dt.strftime('%b-%Y')

pivot_df_bulan.to_csv('pivot_df_bulan.csv',index=False)

# Membuat tabel pivot by MONTH and LINE---------------
pivot_df_bulan_line= pd.pivot_table(df, values=['NG%'], index=['Month','Line'], aggfunc={'NG%': 'mean'})

pivot_df_bulan_line.index = pd.to_datetime(pivot_df_bulan_line.index, format='%b-%Y')

# Urutkan DataFrame berdasarkan kolom 'Month'
pivot_df_bulan_line.sort_index(inplace=True)

# Reset index untuk memudahkan plotting
pivot_df_bulan_line.reset_index(inplace=True)

pivot_df_bulan_line['Month'] = pivot_df_bulan_line['Month'].dt.strftime('%b-%Y')

pivot_df_bulan_line.to_csv('pivot_df_bulan_line.csv',index=False)

# Membuat tabel pivot by SINGLE LINE---------------
pivot_df_line= pd.pivot_table(df, values=['TotInsp(Lot)', 'NG%'], index='Line', aggfunc={'TotInsp(Lot)': 'sum', 'NG%': 'mean'})
# Membuat tabel pivot by MULTI LINE---------------
pivot_df_line= pd.pivot_table(df, values=['TotInsp(Lot)', 'NG%'], index='Line', aggfunc={'TotInsp(Lot)': 'sum', 'NG%': 'mean'})
pivot_df_line_multi = pd.pivot_table(df, values='NG%', index='Date', columns='Line', aggfunc='mean')

# Reset index untuk memudahkan plotting
pivot_df_line.reset_index(inplace=True)
pivot_df_line_multi.reset_index(inplace=True)

pivot_df_line.to_csv('pivot_df_line.csv',index=False)
pivot_df_line_multi.to_csv('pivot_df_line_multi.csv',index=False)

# Membuat tabel pivot by KATEGORI---------------
pivot_df_kategori = pd.pivot_table(df, values=['TotInsp(Lot)', 'NG%'], index='Kategori', aggfunc={'TotInsp(Lot)': 'sum', 'NG%': 'mean'})

# Reset index untuk memudahkan plotting
pivot_df_kategori.reset_index(inplace=True)
pivot_df_kategori.to_csv('pivot_df_kategori.csv',index=False)