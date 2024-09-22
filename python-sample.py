#%%
import myfitnesspal
import os 
from datetime import datetime
import requests

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
    # クッキーを取得
    cookies = session.cookies.get_dict()
    print(cookies)
    
    # MyFitnessPalクライアントの初期化
    client = myfitnesspal.Client('taisei12232000m@gmail.com', 'taisei1223')

    # DBUS_SESSION_BUS_ADDRESSの取得
    value = os.environ.get('DBUS_SESSION_BUS_ADDRESS')
    print(value)

    # 今日の日付を取得
    today = datetime.now().date()

    # 今日の食事データを取得
    try:
        day = client.get_date(today.year, today.month, today.day)
        print("食事データ取得成功")
        for meal in day.meals:
            print(meal)
    except Exception as e:
        print("食事データ取得失敗")
        print(e)
else:
    print("ログイン失敗")
    print(response.text)  # エラーメッセージを表示# ログインが成功したか確認
if response.ok:
    print("ログイン成功")
    # クッキーを取得
    cookies = session.cookies.get_dict()
    print(cookies)
    
    # MyFitnessPalクライアントの初期化
    client = myfitnesspal.Client('taisei12232000m@gmail.com', 'taisei1223')

    # DBUS_SESSION_BUS_ADDRESSの取得
    value = os.environ.get('DBUS_SESSION_BUS_ADDRESS')
    print(value)

    # 今日の日付を取得
    today = datetime.now().date()

    # 今日の食事データを取得
    try:
        day = client.get_date(today.year, today.month, today.day)
        print("食事データ取得成功")
        for meal in day.meals:
            print(meal)
    except Exception as e:
        print("食事データ取得失敗")
        print(e)
else:
    print("ログイン失敗")
    print(response.text)  # エラーメッセージを表示


    
#%%   
