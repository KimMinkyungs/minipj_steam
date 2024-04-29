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



url = 'https://store.steampowered.com/app/2068280/Nordic_Ashes_Survivors_of_Ragnarok/'

response = requests.get(url)

html_text = response.text
soup = bs(html_text, 'html.parser')

des_divs = soup.find('div', class_='game_description_snippet')

game_info = soup.find('div', class_='summary column', id='developers_list')

game_pub = soup.find_all('div', class_='summary column')
combined_content = []
i = 0
for font in game_pub:
        i = i + 1
        print(font.text)
        print('===========================')

print(i)