import requests
import pickle

# MyFitnessPalのURL
url = 'https://www.myfitnesspal.com/'

# ヘッダーの設定
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

# セッションを開始
session = requests.Session()

# 保存したクッキーを読み込む
with open('cookies.pkl', 'rb') as f:
    session.cookies.update(pickle.load(f))

# クッキーを利用してリクエストを送信
response = session.get(url, headers=headers)

# ログインが成功したか確認
if response.ok:
    print("ログイン成功")
    # 必要なデータを取得
    # 例: 今日の食事データを取得
    # ...
else:
    print("ログイン失敗")
    print(response.text)  # エラーメッセージを表示
