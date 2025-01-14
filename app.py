import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

def load_data(db_url="postgresql://mitsuhiro.ogawa:Misonikomi23@localhost:5432/amazon_books"):
    engine = create_engine(db_url)
    query = "SELECT * FROM books"
    df = pd.read_sql(query, engine)
    return df

# Streamlitアプリ
st.title("Amazon データ分析の本情報")

# データをロード
df = load_data()

# データテーブル表示
st.subheader("本のデータ")
st.dataframe(df)

# レーティング分布の表示
st.subheader("レーティングの分布")
st.bar_chart(df['rating'])

# 平均レーティングの表示
avg_rating = df['rating'].mean()
st.metric("平均レーティング", f"{avg_rating:.2f}")