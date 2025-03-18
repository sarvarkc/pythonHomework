import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument("--window-position=100,100")


driver = webdriver.Chrome(chrome_options)


driver.get("https://www.demoblaze.com/")

#click laptops
categories = driver.find_elements(By.CLASS_NAME,"list-group-item")
for categorie in categories:
    if categorie.text == "Laptops":
        categorie.click()
        time.sleep(5)

#click next button
button = driver.find_element(By.ID,"next2")
button.click()
time.sleep(5)

#create dict and json
data = {
    "laptops" : [

    ]
}

list

card_block = driver.find_elements(By.CLASS_NAME,"card-block")
for x in card_block:
    one_data={}
    one_data["Laptop Name"] = x.find_element(By.TAG_NAME,"h4").text
    one_data["Price"] = x.find_element(By.TAG_NAME,"h5").text
    one_data["Description"] = x.find_element(By.TAG_NAME,"p").text
    data["laptops"].append(one_data)
print(data)

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

time.sleep(5)

driver.quit()