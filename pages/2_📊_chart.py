import streamlit as st
import pandas as pd
import numpy as np
import subprocess
import plotly.express as px
import plotly.graph_objects as go       #cara 2 agar data terlihat saat mouse over
# import json
# from 1_🏡_home import results_dateRange

st.subheader('Dasboard Chart')      #at home 28Sept2024 when I'm feeling blue

# Baca nilai dari file JSON
# with open('date_info.json', 'r') as f:
#     date_info = json.load(f)

# min_date = date_info['min_date']
# max_date = date_info['max_date']

# st.write(f"Data Periode :{min_date} sampai {max_date}")
# st.error("Anda memilih data dari tanggal: "+ str(result_dateRange['Start Date']) + " sampai tanggal " + str(result_dateRange['End Date'])))

# ----------- Menjalankan pivot.py ------------------------
subprocess.run(["python", "pivot.py"])

#------------buka file output dr pivot.py -----------------

# if 'pivot_df_tanggal.csv' is not None:
#     pivot_df_bulan=pd.read_csv('pivot_df_tanggal.csv')

if 'pivot_df_bulan.csv' is not None:
    pivot_df_bulan=pd.read_csv('pivot_df_bulan.csv')

if 'pivot_df_line.csv' is not None:
    pivot_df_line=pd.read_csv('pivot_df_line.csv')

if 'pivot_df_line_multi.csv' is not None:
    pivot_df_line_multi=pd.read_csv('pivot_df_line_multi.csv')
    long_format = pivot_df_line_multi.melt(id_vars='Date', value_vars=['Barrel 4', 'Rack 1', 'Nickel'], var_name='Line', value_name='NG%')

if 'pivot_df_kategori.csv' is not None:
    pivot_df_kategori=pd.read_csv('pivot_df_kategori.csv')



#----------     CHART AREA ---------

# Membuat grafik combo dengan Plotly

##Grafik TotInsp & NG by Month
fig = go.Figure()

# Grafik batang untuk TotInsp(Lot)
fig.add_trace(go.Bar(
    x=pivot_df_bulan['Month'],
    y=pivot_df_bulan['TotInsp(Lot)'],
    name='TotInsp(Lot)',
    marker_color='yellow',
    yaxis='y1'
))

# Grafik garis untuk NG%
fig.add_trace(go.Scatter(
    x=pivot_df_bulan['Month'],
    y=pivot_df_bulan['NG%'],
    name='NG%',
    marker=dict(color='red', size=10),
    yaxis='y2'
))

# Menambahkan sumbu Y kedua
fig.update_layout(
    title='Total Inspected (Lot) dan NG ratio (%) by Month-Year',
    xaxis=dict(title='Month-Year'),
    yaxis=dict(title='TotInsp(Lot)', titlefont=dict(color='yellow'), tickfont=dict(color='yellow')),
    yaxis2=dict(title='NG%', titlefont=dict(color='red'), tickfont=dict(color='red'), overlaying='y', side='right'),

    paper_bgcolor='rgba(0,0,0,0)',      # Warna background keseluruhan
    plot_bgcolor='rgba(0,0,0,0)',       # Warna background area plot
    shapes=[  # Menambahkan border pada paper
        dict(
            type='rect',
            xref='paper', yref='paper',
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color='grey', width=1)
        )
    ],
    legend=dict(
        yanchor="top",
        y=-0.2,  # Posisi vertikal di bawah sumbu X
        xanchor="center",
        x=0.5   # Posisi horizontal di tengah
    )
)

# Tampilkan grafik di Streamlit
st.plotly_chart(fig)
#------------------------------------------------
kiri,kanan=st.columns(2)
with kiri:

    ##Grafik TotInsp & NG by Line
    fig = go.Figure()

    # Grafik batang untuk TotInsp(Lot)
    fig.add_trace(go.Bar(
        x=pivot_df_line['Line'],
        y=pivot_df_line['TotInsp(Lot)'],
        name='TotInsp(Lot)',
        marker_color='blue',
        yaxis='y1'
    ))

    # Grafik garis untuk NG%
    fig.add_trace(go.Scatter(
        x=pivot_df_line['Line'],
        y=pivot_df_line['NG%'],
        name='NG%',
        marker=dict(color='red', size=10),
        yaxis='y2'
    ))

    # Menambahkan sumbu Y kedua
    fig.update_layout(
        title='Total Inspected (Lot) dan NG ratio (%) by Line',
        xaxis=dict(title='Line'),
        yaxis=dict(title='TotInsp(Lot)', titlefont=dict(color='blue'), tickfont=dict(color='blue')),
        yaxis2=dict(title='NG%', titlefont=dict(color='red'), tickfont=dict(color='red'), overlaying='y', side='right'),

        paper_bgcolor='rgba(0,0,0,0)',      # Warna background keseluruhan
        plot_bgcolor='rgba(0,0,0,0)',       # Warna background area plot
        shapes=[  # Menambahkan border pada paper
            dict(
                type='rect',
                xref='paper', yref='paper',
                x0=0, y0=0, x1=1, y1=1,
                line=dict(color='grey', width=1)
            )
        ],
        legend=dict(
            yanchor="top",
            y=-0.2,  # Posisi vertikal di bawah sumbu X
            xanchor="center",
            x=0.5   # Posisi horizontal di tengah
        )
    )

    # Tampilkan grafik di Streamlit
    st.plotly_chart(fig)
#------------------------------------------------
with kanan:
    ##Grafik TotInsp & NG by Kategori
    fig = go.Figure()

    # Grafik batang untuk TotInsp(Lot)
    fig.add_trace(go.Bar(
        x=pivot_df_kategori['Kategori'],
        y=pivot_df_kategori['TotInsp(Lot)'],
        name='TotInsp(Lot)',
        marker_color='green',
        yaxis='y1'
    ))

    # Grafik garis untuk NG%
    fig.add_trace(go.Scatter(
        x=pivot_df_kategori['Kategori'],
        y=pivot_df_kategori['NG%'],
        name='NG%',
        marker=dict(color='red', size=10),
        yaxis='y2'
    ))

    # Menambahkan sumbu Y kedua
    fig.update_layout(
        title='Total Inspected (Lot) dan NG ratio (%) by Kategori',
        xaxis=dict(title='Kategori'),
        yaxis=dict(title='TotInsp(Lot)', titlefont=dict(color='green'), tickfont=dict(color='green')),
        yaxis2=dict(title='NG%', titlefont=dict(color='red'), tickfont=dict(color='red'), overlaying='y', side='right'),
        paper_bgcolor='rgba(0,0,0,0)',      # Warna background keseluruhan
        plot_bgcolor='rgba(0,0,0,0)',       # Warna background area plot
        shapes=[  # Menambahkan border pada paper
            dict(
                type='rect',
                xref='paper', yref='paper',
                x0=0, y0=0, x1=1, y1=1,
                line=dict(color='grey', width=1)
            )
        ],
        legend=dict(
            yanchor="top",
            y=-0.2,  # Posisi vertikal di bawah sumbu X
            xanchor="center",
            x=0.5   # Posisi horizontal di tengah
        )
    )

    # Tampilkan grafik di Streamlit
    st.plotly_chart(fig)

#PIE CHART KATEGORI ------------------------
## Membuat pie chart untuk LINE
label_line=pivot_df_line['Line']
ng_percent = pivot_df_line['NG%']
tot_inspected = pivot_df_line['TotInsp(Lot)']

fig_ng = go.Figure(data=[go.Pie(labels=label_line, values=ng_percent, hole=.3)])
fig_ng.update_layout(title_text="PIE CHART NG% by LINE")

# Membuat pie chart untuk TotInspected
fig_tot = go.Figure(data=[go.Pie(labels=label_line, values=tot_inspected, hole=.3)])
fig_tot.update_layout(title_text='PIE CHART QTY INSPECTED by LINE')

# Menampilkan pie chart di Streamlit
kolpie1,kolpie2=st.columns(2)
with kolpie1:
    st.plotly_chart(fig_ng)
with kolpie2:
    st.plotly_chart(fig_tot)

## Membuat pie chart untuk Kategori
label_kategori=pivot_df_kategori['Kategori']
ng_percent = pivot_df_kategori['NG%']
tot_inspected = pivot_df_kategori['TotInsp(Lot)']

fig_ng = go.Figure(data=[go.Pie(labels=label_kategori, values=ng_percent, hole=.3)])
fig_ng.update_layout(title_text='PIE CHART NG% by KATEGORI')

# Membuat pie chart untuk TotInspected
fig_tot = go.Figure(data=[go.Pie(labels=label_kategori, values=tot_inspected, hole=.3)])
fig_tot.update_layout(title_text='PIE CHART QTY INSPECTED by KATEGORI')

# Menampilkan pie chart di Streamlit
kolpie1,kolpie2=st.columns(2)
with kolpie1:
    st.plotly_chart(fig_ng)
with kolpie2:
    st.plotly_chart(fig_tot)

#----------------- LINE CHART by ST --------------
pivot_df_bulan.index = pd.to_datetime(pivot_df_bulan.index)

# Urutkan DataFrame berdasarkan kolom 'Month'
# pivot_df_bulan.sort_index(inplace=True)
# # Reset index untuk memudahkan plotting
# pivot_df_bulan.reset_index(inplace=True)

chart_data=pd.DataFrame(pivot_df_bulan,columns=['NG%','Line','Month'])
st.line_chart(chart_data, x="Month", y="NG%", color="#FF0000")

#------------- CHART MULTI LINE WITH PLOTLY --------------
# Membuat grafik garis interaktif dengan Plotly
fig = px.line(long_format, x='Date', y='NG%', color='Line', markers=True, title='Rata-rata NG% per Line')
fig.update_layout(xaxis_title='Bulan', yaxis_title='NG%', legend_title='Line',
                  legend=dict(
                        orientation="h",
                        yanchor="bottom",
                        y=-0.3,
                        xanchor="center",
                        x=0.5)
)
st.plotly_chart(fig)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)