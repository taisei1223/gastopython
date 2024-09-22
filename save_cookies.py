import requests
import pickle

# MyFitnessPalのログインURL
login_url = 'https://www.myfitnesspal.com/account/login'

# ログイン情報
payload = {
    'username': 'taisei12232000m@gmail.com',
    'password': 'taisei1223'
}

# ヘッダーの設定
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

# セッションを開始
session = requests.Session()

# ログインリクエストを送信
response = session.post(login_url, data=payload, headers=headers)

# ログインが成功したか確認
if response.ok:
    print("ログイン成功")
    # クッキーを保存
    with open('cookies.pkl', 'wb') as f:
        pickle.dump(session.cookies, f)
else:
    print("ログイン失敗")
    print(response.text)  # エラーメッセージを表示
