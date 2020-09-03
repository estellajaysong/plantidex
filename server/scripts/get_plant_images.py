# Saved and modified from https://github.com/Msalmannasir/Google_image_scraper/blob/master/google_img.py

# BC_native_plants = [
#     'Aster',
#     'Aquilegia formosa',
#     # 'Sedum spathulifolium',
#     # 'Delphinium menziesii',
#     # 'Rosa nutkana',
#     # 'Physocarpus capitatus'
#     # 'Sambucus racemosa',
#     # 'Gaultheria shallon',
#     # 'Arbutus menziesii',
#     # 'Cornus Eddie\'s White Wonder',
#     # 'Sorbus aucuparia',
#     # 'Acer circinatum'
# ]
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import requests
import shutil
import os

user = os.getlogin()
driver = driver = webdriver.Chrome(ChromeDriverManager().install())
directory = '../images'
inp = input("Enter what you wanna search?")
url = (
    'https://www.google.com/search?q='
    + str(inp)
    + '&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947'
)
iterate = int(input("Enter how many pics?"))


def save_img(inp, img, i):
    try:
        filename = inp + str(i) + '.jpg'
        response = requests.get(img, stream=True)
        image_path = os.path.join(directory, filename)
        with open(image_path, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
    except Exception:
        pass


def find_urls(inp, url, driver, iterate):
    driver.get(url)
    time.sleep(3)
    for j in range(1, iterate + 1):
        imgurl = driver.find_element_by_xpath(
            '//div//div//div//div//div//div//div//div//div//div['
            + str(j)
            + ']//a[1]//div[1]//img[1]'
        )
        imgurl.click()
        time.sleep(15)
        img = driver.find_element_by_xpath(
            '//body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img'
        ).get_attribute("src")
        save_img(inp, img, j)


find_urls(inp, url, driver, iterate)
