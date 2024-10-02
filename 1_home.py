#Sunday 08Sept2024, create Dashboard wit lib streamlit
#Source: https://www.youtube.com/watch?v=2siBrMsqF44

import streamlit as st
import pandas as pd
import xlrd
from PIL import Image
import base64
from streamlit_extras.dataframe_explorer import dataframe_explorer
import numpy as np
import webbrowser
import subprocess   #untuk menjalankan cleaning.py tanpa menampilkan di web 24.09.2024
import locale

# Set locale to the user's default setting (for example, 'en_US' for US English)
locale.setlocale(locale.LC_ALL, '')

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Quality Dashboard", page_icon=":bar_chart:", layout="wide")

# horizontal Menu
# selected = option_menu(None, ["Home", "Upload", "Chart", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal")
# selected

# Fungsi untuk mengubah gambar menjadi base64
# def get_image_as_base64(image_path):
#     with open(image_path, "rb") as img_file:
#         return base64.b64encode(img_file.read()).decode()
    
# st.write("Bismillah")
# kolomJudul,kolomLogo=st.columns(2)
# with kolomJudul:
#     st.markdown(
#         """
#         <style>
#         .container {
#             width: 300px;
#             height: 30px;
#             display: flex;
#             align-contents:left;
#             justify-content: flex-start;

#         }
#         .judul {
#             color: yellow;
#             font-size: 27px;
#             margin-top:0px;
#             margin-bottom: 0px;
#             align-items:left;
#         }
#         .subjudul {
#             color: grey;
#             font-size: 10px;
#             margin-top: 30px;
#             margin-bottom:0px;
#         }
#         @media (max-width: 600px) {
#             .container {
#                 flex-direction: column;
#                 align-items: center;
#                 justify-content: flex-end;
#             }
#             .judul {
#                 font-size: 20px;
#             }
#             .subjudul {
#                 font-size: 2px;
#             }
#         }
#         </style>
#         <div class="container">
#             <div class="text">
#                 <h1 class='judul'>QUALITY REPORT</h1>
#                 <h2 class='subjudul'>by Imam W. ©️2024</h2>
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
#     # st.title(":bar_chart: QUALITY REPORT")
#     # st.subheader("by Imam W. ©️2024")

# with kolomLogo:
    # Memuat gambar
    # image = Image.open('logoKPD.PNG')
    # st.markdown(
        # Memuat gambar dan mengubahnya menjadi base64
    # logo_KPD='logoKPD.PNG'
    # image_base64 = get_image_as_base64(logo_KPD)

    # Menampilkan gambar dan teks di kolom kanan dengan posisi berdampingan
    # st.markdown(
    #     f"""
    #     <style>
    #     .container {{
    #         display: flex;
    #         align-items:center;
    #         justify-content: flex-end;
    #         flex-wrap: wrap;
    #     }}
    #     .container img {{
    #         width: 50px;
    #         margin-top: -20px;
    #     }}
    #     .container h2 {{
    #         color: grey;
    #         font-size: 20px;
    #         margin-top: -20px;
    #         margin-right: 10px;
    #         margin-bottom: 0px;
    #     }}
    #     @media (max-width: 600px) {{
    #         .container {{
    #             justify-content: center;
    #         }}
    #         .container img {{
    #             margin-top: 0;
    #         }}
    #         .container h2 {{
    #             margin-top: 0;
    #             text-align: center;
    #         }}
    #     }}
    #     </style>
    #     <div class="container">
    #         <h2>PT. KARYAPRATAMA DUNIA</h2>
    #         <img src='data:image/png;base64,{image_base64}'/>
    #     </div>
    #     """,
    #     unsafe_allow_html=True
    # )

    #--------akhir naroh Logo

# st.markdown("""---""")

# ---- SIDEBAR ----

st.sidebar.header(":bar_chart: QUALITY REPORT")
st.sidebar.markdown("""<h3 style="color:blue;">⚛ PT. KARYAPRATAMA DUNIA 📊</h3>""", unsafe_allow_html=True)
st.sidebar.markdown("---")

#Upload File Data

uploaded_file=st.sidebar.file_uploader("Pilih file Excel (.xls, .xlsx, csv):")

if uploaded_file is not None:

    # ---- READ FILE XLS, XLSX, CSV ----

    #flexible read data:
    def read_file(uploaded_file):
        # Mendapatkan nama file
        file_name = uploaded_file.name
        
        # Memeriksa ekstensi file
        if file_name.endswith('.xls'):
            # Menggunakan engine 'xlrd' untuk file .xls
            df2 = pd.read_excel(uploaded_file, engine='xlrd')
        elif file_name.endswith('.xlsx'):
            # Menggunakan engine 'openpyxl' untuk file .xlsx
            df2 = pd.read_excel(uploaded_file, engine='openpyxl')
        elif file_name.endswith('.csv'):
            # Menggunakan pandas untuk membaca file .csv
            df2 = pd.read_csv(uploaded_file)
        else:
            raise ValueError("File harus memiliki ekstensi .xls, .xlsx, atau .csv")

            # Nama file yang akan dihapus saat mulai
            files_to_delete = ["temp_uploaded.csv", "df_cleaned.csv"]
            # Loop melalui setiap file dan hapus jika ada
            for file in files_to_delete:
                if os.path.exists(file):
                    os.remove(file)
        
            # df2.to_csv('temp_uploaded.csv', index=False)  # Menyimpan dataframe ke file CSV sementara
      
        return df2
        
    # baca dataframe df2
    df2 = read_file(uploaded_file)

    #--------------------------------------------------------PR belum berhasil dg metode ini

    # if 'df_temp_upload' not in st.session_state:
    #     st.session_state['df_temp_upload']=df2

    df2.to_csv('temp_uploaded.csv',index=False)

    #dataframe - script ini untuk filtering model tree
    # with st.expander("Preview Original Data"):
    #     df3 = dataframe_explorer(df2, case=False)
    #     st.dataframe(df3, use_container_width=True)

    # st.write("File uploaded...and start Cleaning...")


    # Menjalankan cleaning.py
    subprocess.run(["python", "cleaning.py"])

    # Membaca dataframe dari file CSV hasil cleaning 'df_cleaned.csv'
    nama_file_bersih= 'df_cleaned.csv'
    if nama_file_bersih is not None:
        df = pd.read_csv(nama_file_bersih)
    else:
        st.error("File 'df_cleaned.csv' tidak ditemukan")

    #--------------------------------------------------------PR belum berhasil dg metode ini
    # if 'df_cleaned'in st.session_state:
    #     df = st.session_state['df_cleaned']
    # else:
    #     st.write("DataFrame tidak ditemukan di session_state. Pastikan Anda telah menyimpannya di cleaning.py.")
     
    #Filtering
    #sidebar Filter date picker

    # Konversi kolom 'Date' ke format datetime, mengabaikan kesalahan
    df['Date'] = pd.to_datetime(df['Date'],errors='coerce')

    # Menghapus baris dengan nilai NaT
    df = df.dropna(subset=['Date'])

    # Mendapatkan tanggal minimal dan maksimal

    min_date = df['Date'].min()
    max_date = df['Date'].max()

    # Menyimpan hasil ke file JSON untuk dapat dibaca di page lain
    # date_info = {
    # 'Start Date': min_date,
    # 'End Date': max_date
    # }
    # with open('date_info.json', 'w') as f:
    #     json.dump(date_info, f)

    # Tampilkan nilai min_date dan max_date untuk verifikasi
    # st.write(f"Min Date: {min_date}")
    # st.write(f"Max Date: {max_date}")


    with st.sidebar:
        st.title("Pilih rentang tanggal:")
        start_date=st.date_input('Start Date', min_date)

    with st.sidebar:
        end_date=st.date_input('End Date',max_date)

    if start_date is not None:
        st.sidebar.error("Anda memilih data dari tanggal: "+ str(start_date) + " sampai tanggal " + str(end_date))

        # Konversi input tanggal ke format datetime
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        # st.subheader("Data After Cleaning and Filteres by Date Range")
        # df_byDateRange=df[(df['Date']>=str(min_date))&(df['Date']<=str(max_date))]
        df_byDateRange = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
        # st.write("Data after Filter Date Range")
        # st.write(df_byDateRange)

    #Multi select Filter

    bulan=st.sidebar.multiselect(
        "Pilih Filter Month:",
        options=df_byDateRange["Month"].unique(),
        default=df_byDateRange["Month"].unique()

    )
    line = st.sidebar.multiselect(
        "Pilih Filter Line:",
        options=df_byDateRange["Line"].unique(),
        default=df_byDateRange["Line"].unique()
    )

    cust_ID = st.sidebar.multiselect(
        "Pilih Filter Customer:",
        options=df_byDateRange["Cust_ID"].unique(),
        default=df_byDateRange["Cust_ID"].unique(),
    )

    kategori = st.sidebar.multiselect(
        "Pilih Filter Kategori:",
        options=df_byDateRange["Kategori"].unique(),
        default=df_byDateRange["Kategori"].unique()
    )

    df_selection = df_byDateRange.query(
        "Month==@bulan & Line == @line & Cust_ID == @cust_ID & Kategori == @kategori"
    )

    # Check if the dataframe is not empty:
    if df_selection is not None:

        df_selection.to_csv('df_cleaned_multifiltered.csv',index=False)
        # st.subheader("Data Preview after Multiselect Filter")
        # st.write(df_selection)

        # Mengganti nilai non-numeric atau NaN dengan 0
        # df_selection['NG%'] = pd.to_numeric(df_selection['NG%'], errors='coerce').fillna(0)
        df_selection['NG%'] = df_selection['NG%'].fillna(0)
        total_NG = df_selection['NG%'].mean()
        total_Qty=df_selection['TotInsp(Lot)'].sum()

        # Format nilai
        average_ng_formatted = f"{total_NG:.2f}"  # 2 digit di belakang koma
        # total_inspected_formatted = "{:,.0f}".format(total_Qty).replace(",", ".") # 0 digit di belakang koma dan mengganti ribuan koma jadi titik
        total_Qty_formatted=locale.format_string("%d", int(total_Qty), grouping=True)

        # Summary move to Metric
        # st.write("Total rata2 NG % : ",average_ng_formatted)
        # st.write("Total Qty Inspected (lot) : ",total_inspected_formatted)

    else:
        st.warning("No data available based on the current filter settings!")
        # st.stop() # This will halt the app from further execution.

    #buat kolom Metric
    leftMenu,RightMenu=st.columns(2,gap='small')
    with RightMenu:
            st.info('Summary Quantity',icon="🍉")
            if total_Qty_formatted is not None:
                st.metric(label="Total Inspected (lot)",value=total_Qty_formatted)

    with leftMenu:
            st.info('Summary Quality',icon="🚨")
            if average_ng_formatted is not None:
                st.metric(label="Average NG (%)",value=average_ng_formatted)

    #akhir kolom Metric 

    st.sidebar.info('Link to Prefessional Summary Report',icon="📊")
    if st.sidebar.button('Summary Report'):
        webbrowser.open_new_tab('https://lookerstudio.google.com/reporting/e4a5c3f7-bf91-44e0-9ced-2b7a01eafa3d/page/FsgzD?s=qyZPms8Wytc')

        # st.sidebar.subheader("Data Filter")

        # kolom=df_byDateRange.columns.tolist()
        # selected_kolom=st.sidebar.selectbox("Pilih kolom untu mem-filter:",kolom)
        # nilai_unik=df_byDateRange[selected_kolom].unique()
        # selected_nilai=st.sidebar.selectbox("Pilih item :", nilai_unik)

        # filtered_df=df_byDateRange[df_byDateRange[selected_kolom]==selected_nilai]

        # st.subheader("Data filtered by date and Others ")
        # st.write(filtered_df)

        # st.subheader("PLot Data")
        # x_kolom=st.selectbox("Pilih X-Axis:",kolom)
        # y_kolom=st.selectbox("Pilih Y-Axis:",kolom)

        # if st.button("Generate plot"):
        #     st.bar_chart(filtered_df.set_index(x_kolom)[y_kolom])
        #     st.bar_chart(filtered_df,x=x_kolom,y=y_kolom,color="NG%")
   
else:
    st.write("Menunggu file di-upload...")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)