#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pickle
import time

# Chromeオプションを設定
cService = webdriver.ChromeService(executable_path=ChromeDriverManager().install())
options = Options()
#options.add_argument('--no-sandbox')
#options.add_argument('--headless')




#options = webdriver.ChromeOptions()
#options.add_argument('--headless')  # ヘッドレスモードで実行
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')

# Chromeドライバーのパスを指定
#driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(service=cService, options=options)


# MyFitnessPalのログインページにアクセス
driver.get('https://www.myfitnesspal.com/account/login')
print(driver.page_source)

#driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div[4]/button[1]").click()
username = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="password"]')
username.send_keys('taisei12232000m@gmail.com')
password.send_keys('taisei1223')
password.send_keys(Keys.RETURN)

# クッキーを保存
cookies = driver.get_cookies()
with open('cookies.pkl', 'wb') as f:
    pickle.dump(cookies, f)

# ブラウザを閉じる
driver.quit()
#%%