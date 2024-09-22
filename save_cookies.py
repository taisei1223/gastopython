
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle

# Chromeオプションを設定
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # ヘッドレスモードで実行
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Chromeドライバーのパスを指定
driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)

# MyFitnessPalのログインページにアクセス
driver.get('https://www.myfitnesspal.com/account/login')

# ユーザー名とパスワードを入力
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
username.send_keys('taisei12232000m@gmail.com')
password.send_keys('taisei1223')
password.send_keys(Keys.RETURN)

# クッキーを保存
cookies = driver.get_cookies()
with open('cookies.pkl', 'wb') as f:
    pickle.dump(cookies, f)

# ブラウザを閉じる
driver.quit()
