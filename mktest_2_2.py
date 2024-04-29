import requests
import urllib.request
import os, sys
import pandas as pd

from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QFrame, QToolTip
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve
from PyQt5 import uic
import os, sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication



url = 'https://store.steampowered.com/app/1778820/TEKKEN_8/'

response = requests.get(url)

html_text = response.text
soup = bs(html_text, 'html.parser')

des_divs = soup.find('div', class_='game_description_snippet')

game_dev = soup.find('div', class_='summary column', id='developers_list')

game_pub = soup.find_all('div', class_='summary column')
print(game_dev)
print('========')

combined_content = []

for font in game_pub:
        content = font.text
        print(type(content))
        print(content)
        if content :  # 빈 문자열이 아닌 경우에만 추가

            combined_content.append(content)

combined_content = str(combined_content)
combined_content = combined_content.replace("\n\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t","")
combined_content = combined_content.replace("']", "")
combined_content = combined_content.replace("['", "")

#print(combined_content)