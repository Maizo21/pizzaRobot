from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time, json

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


with open('data.json') as json_file:
    data = json.load(json_file)
    newData = []

    for i in data['data']:
        print("- " + i['name'] + " is loading...")
        newData.append( "---------- " + i['name'] + " ----------")

        if i['name'] == "papajohns.cl":
            driver.get(i['url'])

            time.sleep(4)
           
            pizza = driver.find_elements(By.CLASS_NAME,'ga-container-product')

            for j in pizza:
                   if 'pepperoni' in j.find_element(By.CLASS_NAME,'ga-menu-product-name-title').text.lower():
                    print(j.find_element(By.CLASS_NAME,'ga-menu-product-name-title').text + ": " + j.find_element(By.CLASS_NAME,'styles_price__ODKkX').text)
                    newData.append({'Pizza': j.find_element(By.CLASS_NAME,'ga-menu-product-name-title').text, 'price': j.find_element(By.CLASS_NAME,'styles_price__ODKkX').text})

        elif i['name'] == "meltpizzas.com":
            driver.get(i['url'])

            time.sleep(3)

            pizza = driver.find_elements(By.CLASS_NAME,'big-card')

            for j in pizza:
                if 'pepperoni' in j.find_element(By.CLASS_NAME,'title').text.lower():
                    print(j.find_element(By.CLASS_NAME,'title').text + ": " + j.find_element(By.CLASS_NAME,'product-price').text)
                    newData.append({'name': j.find_element(By.CLASS_NAME,'title').text, 'price': j.find_element(By.CLASS_NAME,'product-price').text})

        elif i['name'] == "underpizza.com":
            driver.get(i['url'])

            time.sleep(3)

            pizza = driver.find_elements(By.CLASS_NAME,'product')

            for j in pizza:
                if 'pepperoni' in j.find_element(By.CLASS_NAME,'title').text.lower():
                    print(j.find_element(By.CLASS_NAME,'title').text + ": " + j.find_element(By.CLASS_NAME,'product-price').text)
                    newData.append({'name': j.find_element(By.CLASS_NAME,'title').text, 'price': j.find_element(By.CLASS_NAME,'product-price').text})

        elif i['name'] == "littlecaesars.com":
            driver.get(i['url'])

            time.sleep(3)

            pizza = driver.find_elements(By.CLASS_NAME,'css-55thd1')

            for j in pizza:
                if 'pepperoni' in j.find_element(By.CLASS_NAME,'css-1o4lga5').text.lower():
                    print(j.find_element(By.CLASS_NAME,'css-1l246ro').text + ": " + j.find_element(By.CLASS_NAME,'css-15n7wyn').text)
                    newData.append({'name': j.find_element(By.CLASS_NAME,'css-1l246ro').text, 'price': j.find_element(By.CLASS_NAME,'css-15n7wyn').text})

driver.close()

"erase result.txt content"
open('result.txt', 'w').close()

"pass data to result.txt"
with open('result.txt', 'w') as f:
    json.dump(newData, f, sort_keys=True, indent=4)
    
print("- Script finished")




