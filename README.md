Amazon Books Data Project 📚
このプロジェクトは、Amazon.co.jpから「データ分析」に関する本の情報をスクレイピングし、それをPostgreSQLデータベースに保存し、Streamlitを使って可視化するものです。

📋 プロジェクト概要
データ抽出: BeautifulSoupを使用してAmazon.co.jpから本のタイトル、価格、評価を取得します。
データ変換: 価格を数値型に変換し、評価から余分な文字列を削除します。
データ保存: Postgresデータベースに保存して管理します。
データ可視化: Streamlitを使用してデータをグラフやテーブルで可視化します。
🚀 機能
Amazon.co.jpから「データ分析」関連の本の情報を収集
PostgreSQLにデータを保存
Streamlitで本のデータを以下の形式で可視化
データテーブル
平均価格と平均評価
価格と評価の分布
🛠️ 使用技術
Python ライブラリ:
requests: ウェブサイトへのHTTPリクエスト
beautifulsoup4: HTMLパースとデータ抽出
pandas: データフレーム操作
sqlalchemy: データベース接続と操作
streamlit: データ可視化とアプリ構築
データベース:
PostgreSQL
その他:
Docker（任意、環境構築用）
📂 ディレクトリ構成
bash
Copy code
amazon-books-data-project/
│
├── data_extraction.py         # データ抽出スクリプト
├── data_transform_and_save.py # データ変換と保存スクリプト
├── app.py                     # Streamlitアプリ
├── requirements.txt           # 必要なPythonライブラリ一覧
├── README.md                  # プロジェクトの概要
└── .gitignore                 # Gitで無視するファイル設定
🖥️ 実行方法
1. 依存パッケージのインストール
以下のコマンドを使用して必要なPythonライブラリをインストールしてください。

bash
Copy code
pip install -r requirements.txt
2. PostgreSQLデータベースのセットアップ
PostgreSQLを起動し、以下のコマンドでデータベースとユーザーを作成します。
sql
Copy code
CREATE DATABASE amazon_books;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE amazon_books TO myuser;
data_transform_and_save.py の db_url を編集してPostgreSQL接続情報を設定します。
python
Copy code
db_url = "postgresql://myuser:mypassword@localhost:5432/amazon_books"
3. データの抽出と保存
データ抽出:
bash
Copy code
python data_extraction.py
データ変換と保存:
bash
Copy code
python data_transform_and_save.py
4. データ可視化
Streamlitアプリを起動します。

bash
Copy code
streamlit run app.py
ブラウザで http://localhost:8501 を開き、アプリを確認してください。

⚠️ 注意事項
スクレイピングに関する規約: Amazonの利用規約を確認し、過度なリクエストを送信しないように注意してください。
リクエスト頻度の制御: サーバーへの負荷を避けるため、適宜 time.sleep を追加してください。
