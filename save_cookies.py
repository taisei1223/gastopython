from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle

# Chromeドライバーのパスを指定
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

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
