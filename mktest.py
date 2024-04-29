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

root = os.path.dirname(os.path.abspath(__file__))
MainUI = uic.loadUiType(os.path.join(root, 'test29.ui'))[0]


url = 'https://store.steampowered.com/app/730/CounterStrike_2/'

response = requests.get(url)

html_text = response.text
soup = bs(html_text, 'html.parser')

class MainDialog(QMainWindow, MainUI):
    front_num = []  # 앞쪽 숫자 저장공간
    figure = ""     # 사칙연산 기호 저장
    back_num = []   # 뒷쪽 숫자 저장
    display = []    # 디스플레이 저장
    result = 0      # 결과값 저장
    dot_flag = False    # 소숫점 입력 여부

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("메인화면")
        # btn을 누르면 click_func 함수에 연결
        game_pub = soup.find_all('div', class_='summary column')
        contents_list = []
        for font in game_pub:
            # strip() 메서드를 사용하여 좌우 공백 및 개행 문자 제거
            content = font.text.strip()


        print(str(content))
        self.label.setText(str(content))

    col_names = ['RECENT REVIEWS', 'ALL REVIEWS', 'RELEASE DATE', 'DEVELOPER', 'PUBLISHER','Popular user-defined tags for this product:']
    #df = pd.DataFrame(list3, columns=col_names)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainDialog()
    mainWindow.show()
    sys.exit(app.exec_())



#rightcol = soup.select('.rightcol div')


#print(rightcol)



