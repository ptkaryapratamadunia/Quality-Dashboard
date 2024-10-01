import streamlit as st
import pandas as pd
import numpy as np

# Membaca dataframe dari file CSV sementara
df = pd.read_csv('temp_uploaded.csv')

#--------------------------------------------------------PR belum berhasil dg metode ini
# if 'df' not in st.session_state:
#     df2=st.session_state['df']


# df = pd.read_excel('StockProductionListingJAN_AUG2024.xls',engine='xlrd')
# st.subheader("Go to Clean....")
# st.write(df)

if df is not None:
# Cleaning Process

    # Membersihkan nama kolom dari spasi atau karakter tersembunyi
    df.columns = df.columns.str.strip()

    df['DocDate'] = pd.to_datetime(df['DocDate'],errors='coerce')             #konversi tanggal ke tanggal pandas
    df.rename(columns={'DocDate': 'Date'}, inplace=True)                        #'DocDate' menjadi 'Date'
    df.rename(columns={'Insp(B/H)': 'TotInsp(Lot)'}, inplace=True)              # Mengganti nama kolom 'Keterangan' menjadi 'Kategori'
    df.rename(columns={'NG(B/H)': 'NG(Lot)'}, inplace=True)     # Mengganti nama kolom 'Keterangan' menjadi 'Kategori'
    df.rename(columns={'OK(B/H)': 'OK(Lot)'}, inplace=True)     # Mengganti nama kolom 'Keterangan' menjadi 'Kategori'
    df.rename(columns={'Keterangan': 'Kategori'}, inplace=True)                 # Mengganti nama kolom 'Keterangan' menjadi 'Kategori'
    
    df["Month"] = pd.to_datetime(df["Date"]).dt.month               # menambah kolom 'Month' hasil ekstrasi dari kolom 'Date
    # df["Year"] = pd.to_datetime(df["Date"]).dt.year                 # menambah kolom 'Month' hasil ekstrasi dari kolom 'Date
    df['Month']=df['Date'].dt.strftime('%b-%Y')                        # Short month name, like 'Jan', 'Feb'
    df['Cust_ID'] = df['ItemCode'].str.split(' ').str[0]            # Membuat kolom baru 'Cust_ID' dengan mengambil karakter sebelum spasi pertama
    # menghapus kolom yg tidak akan digunakan'

    df.drop(columns=['Cheklist'], inplace=True)
    df.drop(columns=['DocNo'], inplace=True)
    df.drop(columns=['NoCard'], inplace=True)
    df.drop(columns=['NoBarrelHanger'],inplace=True)
    df.drop(columns=['NoBak'],inplace=True)
    df.drop(columns=['OK(pcs)'],inplace=True)
    df.drop(columns=['Qty(NG)'],inplace=True)
    df.drop(columns=['QInspec'],inplace=True)
    df.drop(columns=['% NG'],inplace=True)
    pd.set_option('display.max_columns', None)                      # Mengatur pandas untuk menampilkan semua kolom
    # memindahkan posisi kolom Y ke setelah kolom X
        # 1. Daftar kolom saat ini
    # columns = df.columns.tolist()
    #     # 2. Pindahkan kolom 'Y' setelah kolom 'X'
    # columns.insert(columns.index('X'), columns.pop(columns.index('Y')))
    #     # 3. Atur ulang dataframe dengan urutan kolom baru
    # df = df.reindex(columns=columns)
    
    # Mengganti nama kolom jenis NG ke nama Aslinya
    new_columns = {
                'A': 'Warna',
                'B': 'Buram',
                'C': 'Berbayang',
                'D': 'Kotor',
                'E': 'Tdk Terplating',
                'F': 'Rontok/ Blister',
                'G': 'Tipis/ EE No Plating',
                'H': 'Flek Kuning',
                'I': 'Terbakar',
                'J': 'Watermark',
                'K': 'Jig Mark/ Renggang',
                'L': 'Lecet/ Scratch',
                'M': 'Seret',
                'N': 'Flek Hitam',
                'O': 'Flek Tangan',
                'P': 'Belang/ Dempet',
                'Q': 'Bintik',
                'R': 'Kilap',
                'S': 'Tebal',
                'T': 'Flek Putih',
                'U': 'Spark',
                'V': 'Kotor H/ Oval',
                'W': 'Terkikis/ Crack',
                'X': 'Dimensi/ Penyok',
                'Y': 'MTL/ SLipMelintir'
            }

    df.rename(columns=new_columns, inplace=True)
    
    # mengkonversi isi kolom NG dari pcs ke Lot dgn membagi dgn Stdr Loading
    kolom_untuk_dibagi=['Warna',
                            'Buram',
                            'Berbayang',
                            'Kotor',
                            'Tdk Terplating',
                            'Rontok/ Blister',
                            'Tipis/ EE No Plating',
                            'Flek Kuning',
                            'Terbakar',
                            'Watermark',
                            'Jig Mark/ Renggang',
                            'Lecet/ Scratch',
                            'Seret',
                            'Flek Hitam',
                            'Flek Tangan',
                            'Belang/ Dempet',
                            'Bintik',
                            'Kilap',
                            'Tebal',
                            'Flek Putih',
                            'Spark',
                            'Kotor H/ Oval',
                            'Terkikis/ Crack',
                            'Dimensi/ Penyok',
                            'MTL/ SLipMelintir']

    for col in kolom_untuk_dibagi:
        df[col]=df[col]/df['Std Load']
   
        # Menjumlahkan kolom 'Wrn1', 'Brm1', 'Fhitam1', dan 'ktor1' pada setiap baris
        df['Tot_NG'] = df[['Warna',
                            'Buram',
                            'Berbayang',
                            'Kotor',
                            'Tdk Terplating',
                            'Rontok/ Blister',
                            'Tipis/ EE No Plating',
                            'Flek Kuning',
                            'Terbakar',
                            'Watermark',
                            'Jig Mark/ Renggang',
                            'Lecet/ Scratch',
                            'Seret',
                            'Flek Hitam',
                            'Flek Tangan',
                            'Belang/ Dempet',
                            'Bintik',
                            'Kilap',
                            'Tebal',
                            'Flek Putih',
                            'Spark',
                            'Kotor H/ Oval',
                            'Terkikis/ Crack',
                            'Dimensi/ Penyok',
                            # 'MTL/ SLipMelintir'
                        ]].sum(axis=1)

        # menghitung prosentase NG dengan syarat TotInsp(Lot) <>0, jika 0 maka 0
        df['NG%'] = np.where(df['TotInsp(Lot)'] == 0, 0, (df['Tot_NG'] / df['TotInsp(Lot)']) * 100)
        # df['NG%']=(df['Tot_NG']/df['TotInsp(Lot)'])*100

        # Mengganti nilai kosong dengan 0
        df['NG%'] = df['NG%'].fillna(0)
        # Mengganti nilai kosong (string kosong) dengan 0
        df['NG%'] = df['NG%'].replace('', 0)

        # st.write(df)

        ## Fungsi untuk menghapus nilai yang mengandung awalan 'CU', ' CU', dan 'CU '
        df['Kategori'] = df['Kategori'].astype(str)       # Mengonversi semua nilai dalam kolom NoJig menjadi string
        def remove_cu_prefix(kategori):
            if kategori.strip().startswith('CU'):
                return "RACK 1"  # atau "" jika ingin menggantinya dengan string kosong
            else:
                return kategori   
        df['Kategori'] = df['Kategori'].apply(remove_cu_prefix)         # Menggunakan apply untuk menerapkan fungsi pada kolom Kategori


        # Membersihkan nama kolom dari spasi atau karakter tersembunyi
        df.columns = df.columns.str.strip()

        # Daftar nilai yang diizinkan 26.09.2024
        allowed_values = ['BUSI','SMP','OTH', 'RACK 1', 'NICKEL', 'HDI']

        # Menghapus nilai yang tidak diizinkan
        df['Kategori'] = df['Kategori'].apply(lambda x: x if x in allowed_values else 'kosong') 
        #kosong pengganti '' yang tidak terdeteksi sebagai .isna() -- 28 Sept 2024 at home after short gowes

        #Mengonversi NaN Kembali ke String Kosong: Setelah melakukan operasi yang diperlukan, Anda bisa mengonversi NaN kembali ke string kosong untuk memastikan kolom tetap bertipe string.
        # df['Kategori'] = df['Kategori'].fillna('')

        # Mengisi kolom Kategori yang kosong berdasarkan kondisi
        df.loc[(df['Line'] == 'Barrel 4') & (df['Cust_ID'] == 'HDI') & (df['Kategori'].isna()), 'Kategori'] = 'HDI'
        df.loc[(df['Line'] == 'Barrel 4') & (df['Kategori']=='kosong'), 'Kategori'] = 'BUSI'
        df.loc[(df['Line'] == 'Rack 1') & (df['Kategori']=='kosong'), 'Kategori'] = 'RACK 1'
        df.loc[(df['Line'] == 'Nickel') & (df['Kategori']=='kosong'), 'Kategori'] = 'NICKEL'

        # st.subheader("preview isi Kategori")
        # st.write(df)
        # st.stop()

        # Fungsi untuk menentukan nilai kolom M/C No dari ekstraksi kolom NoJig
        
        df['NoJig'] = df['NoJig'].astype(str)       # Mengonversi semua nilai dalam kolom NoJig menjadi string
        def get_mc_no(nojig):
            if len(nojig) == 17:
                return nojig[9:11]
            else:
                return ""

        # Mengisi kolom M/C No. berdasarkan kondisi
        df['M/C No.'] = df['NoJig'].apply(get_mc_no)

        #--------------------------------------------------------PR belum berhasil dg metode ini
        # if 'df_cleaned' not in st.session_state:
        #     st.session_state['df_cleaned'] = df

        df.to_csv('df_cleaned.csv',index=False)

else:
    st.write("File tidak ditemukan")


# st.write(df)

# End of Cleaning Data
