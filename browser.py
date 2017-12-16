from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import os,sys


def resource_path(relative_path):
#""" Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# path to selenium server standalone jar, downloaded here:

# http://docs.seleniumhq.org/download/
# or a direct url:
# http://selenium-release.storage.googleapis.com/2.41/selenium-server-standalone-2.41.0.jar
os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.41.0.jar"
# note: I've put this jar file in the same folder as this python file

#browser = webdriver.Chrome("/Users/carneiro/Downloads/UAD/chromedriver")

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)


browser = webdriver.Chrome(executable_path=(resource_path("chromedriver")),chrome_options=chrome_options)

#browser = webdriver.Chrome(resource_path("chromedriver"))



# makes the browser wait if it can't find an element
#browser.implicitly_wait(10)
browser.get("https://www.uaudio.com/my/systems/")

search_input = browser.find_element_by_css_selector("#email")
search_input.send_keys("dcarneiro@hotmail.com")
search_input = browser.find_element_by_css_selector("#pass")
search_input.send_keys("straits")
search_input.send_keys(Keys.RETURN)


time.sleep(7)

html_source = browser.page_source
soup = BeautifulSoup(html_source,"html.parser")
#print(soup)
array=""

for td in soup.findAll("table", class_="data-table"):
    for a in td.findAll("td"):
        if "Manual" not in a.text and "Demo" not in a.text and "demo" not in a.text:
            #print(a.text)
            array = array + a.text

array = array.replace('\n\n','\n').replace('\n\n','\n')
array = array.replace('\n\n','\n').replace('\n\n','\n')
array = array.replace('\n\n','\n').replace('\n\n','\n')
array = array.replace('  ','').replace('  ','')
print(array)


#<td>
#<a href="/uad-plugins/compressors-limiters/uad-1176ln.html">1176LN Legacy Classic Limiting Amplifier </a>
#</td>

#raw_input("Press Enter to close...")


browser.quit()

