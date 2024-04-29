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
print(soup)
combined_content = []

tags_list = [tag.text.strip() for tag in game_pub]

tags_list = str(tags_list)
tags_list = tags_list.replace("\n\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t","")
#tags_list = combined_content.replace('\n\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t',' ')

print(tags_list)