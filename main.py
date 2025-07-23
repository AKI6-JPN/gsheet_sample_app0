import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()

st.write("DataFrame Columns:", df.columns.tolist())
st.write("First few rows of the DataFrame:")
st.dataframe(df.head())

for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
