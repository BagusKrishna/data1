import streamlit as st
import pandas as pd
import io

st.title("Aplikasi Konversi CSV/Excel")

uploaded_file = st.file_uploader("Upload file CSV atau Excel", type=["csv", "xlsx"])

def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def convert_df_to_excel(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
    return output.getvalue()

# Jika ada file yang diupload
if uploaded_file is not None:
    # Cek apakah file CSV atau Excel
    file_extension = uploaded_file.name.split('.')[-1]

    if file_extension == 'csv':
        df = pd.read_csv(uploaded_file, delimiter=',', encoding='utf-8')
        st.write("Data CSV yang diupload:")
        st.write(df)
        
        # Konversi ke Excel
        excel_data = convert_df_to_excel(df)
        st.download_button(
            label="Download file sebagai Excel",
            data=excel_data,
            file_name="converted_file.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        
    elif file_extension == 'xlsx':
        df = pd.read_excel(uploaded_file)
        st.write("Data Excel yang diupload:")
        st.write(df)
        
        # Konversi ke CSV
        csv_data = convert_df_to_csv(df)
        st.download_button(
            label="Download file sebagai CSV",
            data=csv_data,
            file_name="converted_file.csv",
            mime="text/csv"
        )

else:
    st.write("Silakan upload file CSV atau Excel.")
