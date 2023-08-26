from selenium import webdriver
from bs4 import BeautifulSoup

nickname = input("write your nickname\n>>> ")
url = f"https://www.op.gg/summoners/kr/{nickname}"
tag = ["div.game > div.type", "div.game > div.result", "div.info > div > div.kda > div.k-d-a"]

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(options=options)

driver.get(url)
src_html = driver.page_source

driver.close()

soup = BeautifulSoup(src_html, "html.parser")

for i in tag:
    print(soup.select_one(i).text)
print(soup.select_one("div.info > div > div.champion > div.icon > a > img")["alt"])
