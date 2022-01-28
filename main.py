from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import random
import asyncio

# The link to a screenshot is 2 chars followed by 4 nums
async def getImage(chars, nums):

    options = Options()
    options.headless = True+

    urlCode = chars + nums

    print(urlCode)

    if(not os.path.exists('pictures/' + urlCode + '.png')):

        try:
            url = 'https://prnt.sc/' + urlCode
            driver = webdriver.Chrome(options=options, executable_path=str(os.getcwd() + "\\" + 'chromedriver.exe'))
            driver.get(url)

            with open('pictures/' + urlCode + '.png', 'wb') as file:
                file.write(driver.find_element_by_xpath('/html/body/div[3]/div/div/img').screenshot_as_png)

            driver.close()
        except:
            print('Uh oh')

    return True

async def main_def():

    chars = 'cc'
    nums = ''

    for i in range(4):

        nums += str(random.randint(0, 9))

    await getImage(chars, nums)

    return chars + nums

if __name__ == "__main__":
    print("Hello")
    asyncio.run(main_def())