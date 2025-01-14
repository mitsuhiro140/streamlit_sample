import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import pandas as pd

def scrape_amazon_books():
    url = "https://www.amazon.co.jp/s?k=データ分析"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    books = []
    for item in soup.find_all("div", {"data-component-type": "s-search-result"}):
        try:
            title = item.h2.text.strip()
            price = item.find("span", "a-price").find("span", "a-offscreen").text.strip()
            rating = item.find("span", "a-icon-alt").text.strip() if item.find("span", "a-icon-alt") else "No rating"
            books.append({"title": title, "price": price, "rating": rating})
        except AttributeError:
            continue

    # データフレームを作成して返す
    return pd.DataFrame(books)

# 実行してデータを取得
books_df = scrape_amazon_books()
print(books_df.head())

def save_to_postgresql(df, db_url="postgresql://myuser:mypassword@localhost:5432/amazon_books"):
    engine = create_engine(db_url)
    df['price'] = df['price'].str.replace('￥', '').str.replace(',', '').astype(float)
    df['rating'] = df['rating'].str.replace('5つ星のうち', '').astype(float)
    df.to_sql('books', engine, if_exists='replace', index=False)
    print("Data saved to PostgreSQL.")

# PostgreSQLに保存
save_to_postgresql(books_df)
