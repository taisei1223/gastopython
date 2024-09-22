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
    print(response.text)  # エラーメッセージを表示

    
#%%   

#myfittnesspal との接続

client = myfitnesspal.Client()
value=os.environ.get('DBUS_SESSION_BUS_ADDRESS')
print(value)

# 文字変換の関数
def translate_to_japanese(data):
    data_str=str(data)
    # 文字列から辞書の形式を削除
    data_str = data_str.replace("Breakfast ","").replace("Lunch ","").replace("Snacks ", "").replace("Dinner ","").replace("{", "").replace("}", "")
    
    # カンマで区切られたキーと値のペアを辞書に変換
    data_pairs = data_str.split(", ")
    data = {}
    for pair in data_pairs:
        key, value = pair.split(": ")
        data[key.strip("'")] = float(value)
    
    translation_dict = {
        'calories': 'カロリー',
        'carbohydrates': '炭水化物',
        'fat': '脂肪',
        'protein': 'タンパク質',
        'sodium': 'ナトリウム',
        'sugar': '砂糖'
    }
    
    translated_data = {translation_dict.get(key, key): value for key, value in data.items()}
    return translated_data

#　データなしの時のエラー回避関数
def check_data(meal):
    meal=str(meal)
    if meal == "Dinner {}" or meal == "Lunch {}" or meal == "Breakfast {}" or meal == "Snacks {}":
        nodata={'カロリー': 0.0,'炭水化物': 0.0,'脂肪': 0.0,'タンパク質': 0.0,'ナトリウム': 0.0,'砂糖': 0.0}
        return nodata 
    else:
        translated_meals = translate_to_japanese(meal)
        return translated_meals
    

def extract_values(mealdata):
    data_str=str(mealdata)
    data_str = data_str.replace('\xa0', '')
    
    # データ部分を抽出
    data_start = data_str.find("{")
    data_end = data_str.find("}") + 1
    data_substr = data_str[data_start:data_end]
    
    # データを辞書に変換
    data_dict = eval(data_substr)
    
    # 名前部分を抽出
    name_start = data_str.find("-") + 2
    name_end = data_str.find(",")
    name = data_str[name_start:name_end]
    
    # 量部分を抽出
    quantity_start = data_str.find(",") + 2
    quantity_end = data_str.find("{") - 1
    quantity = data_str[quantity_start:quantity_end]
    
    # 抜き出す値を指定
    result = {
        '食べ物': name,
        '数量': quantity,
        'カロリー': data_dict['calories'],
        '炭水化物': data_dict['carbohydrates'],
        '脂質': data_dict['fat'],
        'プロテイン': data_dict['protein']
    }
    
    return result

#　取得日付を専用の型に変換       
today = datetime.today()
year = today.year
month = today.month
day = today.day
day = client.get_date(year, month, day)


#一日の総摂取カロリー
today=translate_to_japanese(day.totals)
print("総摂取カロリー")
print(today)
print("============================")

#各食事のデータ
for meal_num in range(0,4):
    eachmeal=check_data(day.meals[meal_num])
    print(eachmeal)
    lens=len(day.meals[meal_num])
    for i in range(0,lens):
        value = extract_values(day.meals[meal_num].entries[i])
        print(value)
    print("============================")
#%%
