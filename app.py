 #Bismillah, niat insun nggawe ripot dokok nang langit - 17Sept2024

# @Email:  contact@pythonandvba.com
# @Website:  https://pythonandvba.com
# @YouTube:  https://youtube.com/c/CodingIsFun
# @Project:  Sales Dashboard w/ Streamlit



import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Quality Dashboard", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----
@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
        io="Aug24.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1",
        skiprows=0,
        usecols="C:AS",
        nrows=10000,
    )
    return df

df = get_data_from_excel()

df['DocDate'] = pd.to_datetime(df['DocDate'])

    # Add 'Month' column to dataframe
df["Month"] = pd.to_datetime(df["DocDate"]).dt.month

df['Month']=df['DocDate'].dt.strftime('%b') # Short month name, like 'Jan', 'Feb'

# Mengganti nama kolom 'Keterangan' menjadi 'Kategori'
df.rename(columns={'Keterangan': 'Kategori'}, inplace=True)

# Membuat kolom baru 'Cust.ID' dengan mengambil karakter sebelum spasi pertama
df['Cust'] = df['ItemCode'].str.split(' ').str[0]





# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")

line = st.sidebar.multiselect(
    "Select the Prodution Line:",
    options=df["Line"].unique(),
    default=df["Line"].unique()
)

cust_ID = st.sidebar.multiselect(
    "Select the Customer:",
    options=df["Cust"].unique(),
    default=df["Cust"].unique(),
)

kategori = st.sidebar.multiselect(
    "Select the Category:",
    options=df["Kategori"].unique(),
    default=df["Kategori"].unique()
)

df_selection = df.query(
    "Line == @line & Cust == @cust_ID & Kategori == @kategori"
)

# Check if the dataframe is empty:
if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop() # This will halt the app from further execution.

# ---- MAINPAGE ----
st.title(":bar_chart: QUALITY REPORT")
st.markdown("##")

# TOP KPI's
# total_sales = int(df_selection["Total"].sum())
# average_rating = round(df_selection["Rating"].mean(), 1)
# star_rating = ":star:" * int(round(average_rating, 0))
# average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

# left_column, middle_column, right_column = st.columns(3)
# with left_column:
#     st.subheader("Total Sales:")
#     st.subheader(f"US $ {total_sales:,}")
# with middle_column:
#     st.subheader("Average Rating:")
#     st.subheader(f"{average_rating} {star_rating}")
# with right_column:
#     st.subheader("Average Sales Per Transaction:")
#     st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("""---""")

# SALES BY PRODUCT LINE [BAR CHART]
# sales_by_product_line = df_selection.groupby(by=["Product line"])[["Total"]].sum().sort_values(by="Total")
# fig_product_sales = px.bar(
#     sales_by_product_line,
#     x="Total",
#     y=sales_by_product_line.index,
#     orientation="h",
#     title="<b>Sales by Product Line</b>",
#     color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
#     template="plotly_white",
# )
# fig_product_sales.update_layout(
#     plot_bgcolor="rgba(0,0,0,0)",
#     xaxis=(dict(showgrid=False))
# )

# # SALES BY HOUR [BAR CHART]
# sales_by_hour = df_selection.groupby(by=["hour"])[["Total"]].sum()
# fig_hourly_sales = px.bar(
#     sales_by_hour,
#     x=sales_by_hour.index,
#     y="Total",
#     title="<b>Sales by hour</b>",
#     color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
#     template="plotly_white",
# )
# fig_hourly_sales.update_layout(
#     xaxis=dict(tickmode="linear"),
#     plot_bgcolor="rgba(0,0,0,0)",
#     yaxis=(dict(showgrid=False)),
# )


# left_column, right_column = st.columns(2)
# left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
# right_column.plotly_chart(fig_product_sales, use_container_width=True)


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)