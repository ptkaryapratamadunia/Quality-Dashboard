
import streamlit as st
import pandas as pd
import subprocess
from streamlit_extras.dataframe_explorer import dataframe_explorer
import locale

# Set locale to the user's default setting (for example, 'en_US' for US English)
locale.setlocale(locale.LC_ALL, '')

st.header("TABLE DATA")

#buka file upload dr home

df=pd.read_csv('temp_uploaded.csv')

#--------------------------------------------------------PR belum berhasil dg metode ini
# if 'df_cleaned' in st.session_state:
#     df=st.session_state['df_cleaned']
# else:
#     st.write("DataFrame tidak ditemukan di session_state. Pastikan Anda telah menyimpannya di cleaning.py.")

#dataframe - script ini untuk filtering model tree
with st.expander("Preview Original Data"):
    df2 = dataframe_explorer(df, case=False)
    st.dataframe(df2, use_container_width=True)


#buka file upload dr home after cleaning
df_bersih=pd.read_csv('df_cleaned_multifiltered.csv')
#--------------------------------------------------------PR belum berhasil dg metode ini
# st.session_state['df_cleaned']
# if 'df_cleaned' not in st.session_state:
#     df_bersih=st.session_state['df_cleaned']
#--------------------------------------------------------PR belum berhasil dg metode ini

#dataframe - script ini untuk filtering model tree
with st.expander("Preview Data after Cleaning"):
    df_bersih2 = dataframe_explorer(df_bersih, case=False)
    st.dataframe(df_bersih2, use_container_width=True)
#--------------------------------------------------

#-------------PIVOT TABLE VIEW --------------------

subprocess.run(["python", "pivot.py"])

st.markdown("""---""")
kol1,kol2=st.columns(2)

with kol1:
    #buka file upload dr chart pivot Month
    if 'pivot_df_bulan.csv' is not None:
        df_pivot_bulan=pd.read_csv('pivot_df_bulan.csv')
    
        df_pivot_bulan.sort_index(inplace=True) 
            ## Menghilangkan kolom index
        df_pivot_bulan.reset_index(drop=True, inplace=True)
        
        # Menghitung mean of mean untuk NG% dan SUM of SUM untuk TotInsp(Lot)
        mean_of_mean_ng = df_pivot_bulan['NG%'].mean()
        sum_of_sum_totinsp = df_pivot_bulan['TotInsp(Lot)'].sum()

        formatted_SUM=locale.format_string("%d", int(sum_of_sum_totinsp), grouping=True)

        st.write("Tabel Total Inspected (Lot) & NG (%) by Month:")
        st.write(df_pivot_bulan)
        st.write(f"Total rata2 NG%: {mean_of_mean_ng:0.2f}")
        st.write(f"Total Inspected (lot): {formatted_SUM}")
    else:
        st.write("File tidak ditemukan !")
#--------------------------------------------------
with kol2:
    if 'pivot_df_line.csv' is not None:
        #buka file upload dr chart pivot line
        df_pivot_line=pd.read_csv('pivot_df_line.csv')
            ## Menghilangkan kolom index
        df_pivot_line.reset_index(drop=True, inplace=True)

            # Menghitung mean of mean untuk NG% dan SUM of SUM untuk TotInsp(Lot)
        mean_of_mean_ng_line = df_pivot_line['NG%'].mean()
        sum_of_sum_totinsp_line= df_pivot_line['TotInsp(Lot)'].sum()

        formatted_SUM2=locale.format_string("%d", int(sum_of_sum_totinsp_line), grouping=True)
        
        st.write("Tabel Total Inspected (Lot) & NG (%) by Line:")
        st.write(df_pivot_line)
        st.write(f"Total rata2 NG%: {mean_of_mean_ng_line:0.2f}")
        st.write(f"Total Inspected: {formatted_SUM2}")
    else:
        st.write("File tidak ditemukan !")
#--------------------------------------------------
st.markdown("""---""")
b2kol1,b2kol2=st.columns(2)

with b2kol1:
    #buka file upload dr chart pivot kategori
    if 'pivot_df_kategori.csv' is not None:
        df_pivot_kategori=pd.read_csv('pivot_df_kategori.csv')
            ## Menghilangkan kolom index
        df_pivot_kategori.reset_index(drop=True, inplace=True)
        # Memeriksa dan menghapus kolom index yang mungkin tersimpan dalam file CSV ('Unnamed: 0').
        if 'Unnamed: 0' in df_pivot_kategori.columns:
            df_pivot_kategori.drop(columns=['Unnamed: 0'], inplace=True)

        # Menghitung mean of mean untuk NG% dan SUM of SUM untuk TotInsp(Lot)
        mean_of_mean_ng_kategori = df_pivot_kategori['NG%'].mean()
        sum_of_sum_totinsp_kategori = df_pivot_kategori['TotInsp(Lot)'].sum()

        # Menambahkan baris Summary
        summary_row = pd.DataFrame({
            'Kategori': ['Summary'],
            'NG%': [mean_of_mean_ng],
            'TotInsp(Lot)': [sum_of_sum_totinsp]
        })

        # Menambahkan baris Summary
        summary_row = pd.DataFrame({
            'Kategori': ['Summary'],
            'NG%': [mean_of_mean_ng_kategori],
            'TotInsp(Lot)': [sum_of_sum_totinsp_kategori]
        })

        # Membuat DataFrame baru untuk baris Summary dan menggabungkannya dengan DataFrame asli menggunakan pd.concat().
        df_mixed2= pd.concat([df_pivot_kategori, summary_row], ignore_index=True)

        st.write("Tabel Total Inspected (Lot) & NG (%) by Kategori:")
        st.write(df_mixed2.to_html(index=False), unsafe_allow_html=True)
    else:
        st.write("File tidak ditemukan !")

with b2kol2:
    if 'pivot_df_bulan_line.csv' is not None:
        df_pivot_bulan_line=pd.read_csv('pivot_df_bulan_line.csv')

        st.write("Tabel NG (%) & Line by Month:")
        st.write(df_pivot_bulan_line)



# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)