import streamlit as st
import pandas as pd
import datetime

# 初期設定
if 'equipment_list' not in st.session_state:
    st.session_state.equipment_list = []

# タイトル
st.title("マンション設備管理アプリ")

# 設備情報の登録フォーム
st.header("新しい設備の登録")
equipment_name = st.text_input("設備名")
location = st.text_input("設置場所")
installation_date = st.date_input("設置日", datetime.date.today())
maintenance_interval = st.number_input("メンテナンス周期（ヶ月）", min_value=1)

if st.button("登録"):
    equipment = {
        "設備名": equipment_name,
        "設置場所": location,
        "設置日": installation_date,
        "メンテナンス周期": maintenance_interval,
        "次回メンテナンス": installation_date + pd.DateOffset(months=maintenance_interval)
    }
    st.session_state.equipment_list.append(equipment)
    st.success("設備が登録されました！")

# 設備リストの表示
st.header("登録された設備")
if st.session_state.equipment_list:
    df = pd.DataFrame(st.session_state.equipment_list)
    st.dataframe(df)
else:
    st.write("現在、登録されている設備はありません。")
