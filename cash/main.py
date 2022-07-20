from selenium import webdriver
from time import sleep
import datetime

url = 'https://www.escapefromtarkov.com/cash'

# while True:
#     now = datetime.datetime.now()
#     current_hour = now.strftime("%H")
#     current_minute = now.strftime("%M")
#     current_second = now.strftime("%S")
#     if(current_hour == "02"):
#         print("wrong hour")
#     else:
#         print('correct')
#         driver = webdriver.Firefox(executable_path=r'C:\Users\logan\Desktop\cash\geckodriver.exe')
#         driver.get(url)
#         # driver.get_screenshot_as_file("screenshot-" + current_hour + "-" + current_minute + "-" + current_second + ".png")
#         driver.quit()
#     print(now)
#     sleep(10)

while True:
    now = datetime.datetime.now()
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")
    if(current_hour=="06"):
        print("its 6am now")
        quit()
    else:
        driver = webdriver.Firefox(executable_path=r'C:\Users\logan\Desktop\cash\geckodriver.exe')
        driver.get(url)
        driver.get_screenshot_as_file("screenshot-" + current_hour + "-" + current_minute + "-" + current_second + ".png")
        driver.quit()
    sleep(60*5)
