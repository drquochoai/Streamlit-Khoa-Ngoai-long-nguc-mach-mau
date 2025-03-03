import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Trang chủ")

# add a file input

uploaded_file = st.file_uploader("Choose a file", type="xlsx")
if uploaded_file is not None:
    # Read the Excel file, all columns astype string
    df = pd.read_excel(uploaded_file, dtype=str)
    
    # Just keep these column HOTEN	MABN	PHAI	NAMSINH	NGAY	NGAYKT	PHANLOAIPT	MAPT	TENPT	TENPTDM	TENPTT	TEN	DACBIET	LOAI1	LOAI2	LOAI3	LOAIPT	TENLOAIPT	HOTEN1 HOTEN2	HOTEN22
    df = df[['MABN', 'HOTEN', 'PHAI', 'NAMSINH', 'NGAY', 'NGAYKT',
             'PHANLOAIPT', 'MAPT', 'TENPT', 'TENPTDM', 'TENPTT', 'TEN', 'DACBIET', 'LOAI1', 'LOAI2', 'LOAI3', 'LOAIPT', 'TENLOAIPT', 'HOTEN1', 'HOTEN2', 'HOTEN22']]

    # reraange the columns: MABN HOTEN PHAI NAMSINH HOTEN1...
    df = df[['MABN', 'HOTEN', 'PHAI', 'NAMSINH', 'HOTEN1', 'HOTEN2', 'HOTEN22', 'NGAY', 'NGAYKT',
             'PHANLOAIPT', 'MAPT', 'TENPT', 'TENPTDM', 'TENPTT', 'TEN', 'DACBIET', 'LOAI1', 'LOAI2', 'LOAI3', 'LOAIPT', 'TENLOAIPT']]
    
    # filter the data keep only the rows with HOTEN1 contain any of these words: "Nguyễn Anh Dũng", "Trần Công Quyền", "Lê Thị Ngọc Hằng", "Trần Quốc Hoài", "Lê Chí Hiếu", "Phan Vũ Hồng Hải", "Phạm Hưng", all in lowercase
    df = df[df['HOTEN1'].str.lower().str.contains("nguyễn anh dũng|trần công quyền|lê thị ngọc hằng|trần quốc hoài|lê chí hiếu|phan vũ hồng hải|phạm hưng")]

    # NGAY and NGAYKT current is text as "dd/mm/yyyy hh:mm", split the text and get dd mm yyyy hh mm, then convert that column to datetime display dd/mm/yyyy hh:mm; example: 06/02/2025 14:23 mean 6th February 2025 2:23 PM
    # """ 
    # NGAY and NGAYKT current is mix from text and datetime, and have some error data, so we need to convert it to datetime
    # - If datetime: reverse month and day, mean month is day and day is month. Example: 06/02/2025 14:23 mean 02th June 2025 2:23 PM
    # - If text: text will have format dd/mm/yyyy hh:m; split the text and get dd mm yyyy hh mm, then convert that column to datetime display dd/mm/yyyy hh:mm; example: 14/02/2025 14:23 mean 14th February 2025 2:23 PM
    # """
    def convert_date(date_str):
        # print type of date_str    
        try:
            # Try to parse as datetime object
            date_obj = pd.to_datetime(date_str, format='%d/%m/%Y %H:%M', errors='coerce')
            print(date_str, date_obj)
            print(date_str, date_obj)
            if pd.notnull(date_obj):
                return date_obj
            else:
                # If parsing fails, assume it's in the wrong format and swap day and month
                # date format is "NaT", but text is like 2025-06-02 13:50:00, mean you need to split the text and get dd mm yyyy hh mm
                date_obj = pd.to_datetime(date_str, format='%Y-%d-%m %H:%M:%S', errors='coerce')
            
                return date_obj
        except Exception as e:
            st.write(f"Error parsing date: {e}")
            return None

    df['NGAY'] = df['NGAY'].apply(convert_date)
    df['NGAYKT'] = df['NGAYKT'].apply(convert_date)

    # Show the data
    st.write(df)
    # show plot of the data follow NGAY, count total rows have same day
    # how many rows have same day in NGAY column, remove hour and minute to count
    
    df['NGAY2'] = df['NGAY'].dt.date
    
    st.write("Dữ liệu theo ngày")
    st.line_chart(df['NGAY2'].value_counts())

    # show total count of rows
    st.write(f"Tổng số PT/TT: {len(df)}")

    # show table groub by hoten1, count total rows
    st.write("Dữ liệu theo bác sĩ")
    st.write(df['HOTEN1'].value_counts())