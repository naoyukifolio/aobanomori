import streamlit as st
import sqlite3
import pandas as pd

# データベース接続関数
def get_connection():
    conn = sqlite3.connect('equipment_management.db')
    return conn

# データをデータベースに保存する関数
def save_equipment(name, location, installation_date, maintenance_interval):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO equipment (name, location, installation_date, maintenance_interval)
        VALUES (?, ?, ?, ?)
    ''', (name, location, installation_date, maintenance_interval))
    conn.commit()
    conn.close()

# データを取得する関数
def get_all_equipment():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM equipment", conn)
    conn.close()
    return df

# StreamlitアプリのUI
st.title("マンション設備管理アプリ")

# 設備情報の登録
st.header("新しい設備の登録")
name = st.text_input("設備名")
location = st.text_input("設置場所")
installation_date = st.date_input("設置日")
maintenance_interval = st.number_input("メンテナンス周期（月）", min_value=1)

if st.button("登録"):
    save_equipment(name, location, installation_date, maintenance_interval)
    st.success("設備が登録されました！")

# 登録された設備を表示
st.header("登録された設備一覧")
equipment_df = get_all_equipment()
st.dataframe(equipment_df)
