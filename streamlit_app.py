import pandas as pd
import pygwalker as pyg
import streamlit as st

# ワイド表示
st.set_page_config(layout="wide")

# タイトル
st.title("Data Analysis with PyGWalker.")

# データフレームの用意
df = None

# ファイル選択
with st.sidebar:
    uploaded_files = st.file_uploader("Choose an Excel file", type="xlsx")
    if uploaded_files is not None:
        df = pd.read_excel(uploaded_files)

# Verificar si los datos se han cargado correctamente
if df is not None:
    # pygwalkerで表示
    pyg.walk(df, env='Streamlit')
else:
    st.warning("Por favor, carga un archivo Excel para continuar.")
