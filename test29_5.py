import time
import requests
import urllib.request
import os, sys

from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QFrame, QToolTip
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve
from PyQt5 import uic
from matplotlib.backends._backend_tk import ToolTip

root = os.path.dirname(os.path.abspath(__file__))
MainUI = uic.loadUiType(os.path.join(root, 'steamTest03.ui'))[0]
SubUI = uic.loadUiType(os.path.join(root, 'test1.ui'))[0]

class Main_Page(QMainWindow, MainUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("메인화면")

        self.url = 'https://store.steampowered.com/'

        response = requests.get(self.url)

        html_text = response.text

        self.soup = bs(html_text, 'html.parser')

        self.thumbnail_name = []
        self.most_click_url = []
        self.new_click_url = []
        self.final_price = []

    def crawling_data(self):
        most_played_address = self.soup.select('#tab_topsellers_content .tab_content_items a')
        new_release_address = self.soup.select('#tab_newreleases_content .tab_content_items a')
        # 아이디가 tab_newrelease_content의 하위태그인 .tab_content_items의 하위태그인 a

        self.calculate_address(most_played_address, 'most')
        self.calculate_address(new_release_address, 'new')

        most_played_name = self.soup.select('#tab_topsellers_content .tab_content_items a .tab_item_cap_img')
        new_release_name = self.soup.select('#tab_newreleases_content .tab_content_items a .tab_item_cap_img')

        self.calculate_name(most_played_name, 'most')
        self.calculate_name(new_release_name, 'new')

        most_played_price = self.soup.select('#tab_topsellers_content .discount_final_price')
        new_release_price = self.soup.select('#tab_newreleases_content .discount_final_price')

        self.calculate_price(most_played_price, 'most')
        self.calculate_price(new_release_price, 'new')

        most_tag = self.soup.find_all('div', class_='tab_content', id='tab_topsellers_content')
        new_tag = self.soup.find_all('div', class_='tab_content', id='tab_newreleases_content')
        self.calculate_tag(new_tag, 'most')
        self.calculate_tag(most_tag, 'new')

    def calculate_address(self, data, category):
        i = 0

        for img in data:
            if img is not None:
                id = img.attrs['data-ds-appid']
                src_link = f'https://cdn.cloudflare.steamstatic.com/steam/apps/{id}/capsule_184x69.jpg?t='
                imageFromWeb = urllib.request.urlopen(src_link).read()
                # 웹에서 사진데이터를 가져오는 역할을 하는 함수이다.

                qPixmapVar = QPixmap()
                qPixmapVar.loadFromData(imageFromWeb)

                if category == 'most':
                    self.most_click_url.append(img.attrs['href'])
                elif category == 'new':
                    self.new_click_url.append(img.attrs['href'])

                image_label = f"{category}_image_label_{i}"
                set_image_label = getattr(self, image_label)
                set_image_label.setPixmap(qPixmapVar)

                container_name = f"{category}_frame_{i}"
                frame = self.findChild(QFrame, container_name)

                if frame:
                    frame.installEventFilter(self)

                i += 1

                if i >= 5:
                    break

    def calculate_name(self, data, category):

        i = 0

        for name in data:
            if name is not None:
                alt_name = name.attrs['alt']
                alt_name = alt_name.replace(':', " ")
                self.thumbnail_name.append(alt_name)

                name_label = f"{category}_name_label_{i}"
                set_name_label = getattr(self, name_label)
                set_name_label.setText(alt_name)

                i += 1

                if i >= 5:
                    break

    def calculate_price(self, data, category):

        i = 0

        for price in data:
            if price is not None:
                price_label = f"{category}_price_label_{i}"
                set_price_label = getattr(self, price_label)
                set_price_label.setText(price.text)

                i += 1

                if i >= 5:
                    break

    def calculate_tag(self, data, category):
        i = 0
        for a_tag in data:
            for b_tag in a_tag.find_all('div', class_='tab_item_content'):

                if b_tag:
                    # 탑 태그의 모든 <span> 태그 추출
                    tag_elements = b_tag.find_all('span', class_='top_tag')
                    # 각 태그의 텍스트 출력
                    if tag_elements:
                        tags_list = [tag.text.strip() for tag in tag_elements]
                        tags_str = str(tags_list).replace("', ', ","\n")
                        tags_str = tags_str.replace("']", "")
                        tags_str = tags_str.replace("['", "")
                        tags_str = f'Game Category:\n{tags_str}'
                        frame = f"{category}_frame_{i}"
                        set_frame_tip = getattr(self, frame)
                        set_frame_tip.setToolTip(tags_str)
                i = i + 1
                if i >= 5: break


    def eventFilter(self, obj, event):
        for i in range(0, len(self.most_click_url)):
            if obj.objectName() == f'most_frame_{i}' and event.type() == QEvent.MouseButtonPress:
                print(self.most_click_url[i])
                # gamePage = Game_Page(self.click_url[i])
                # gamePage.show()

            elif obj.objectName() == f'new_frame_{i}' and event.type() == QEvent.MouseButtonPress:
                print(self.newclick_url[i])

            if obj.objectName() == f'new_frame_{i}' and event.type() == QEvent.Enter:
                obj.setStyleSheet("background-color: rgb(130, 186, 255);")
                QToolTip.setFont(QFont("Arial", 20))  # 툴팁 폰트 설정
                return True

            if obj.objectName() == f'new_frame_{i}' and event.type() == QEvent.Leave:
                obj.setProperty("hovered", False)
                obj.setStyleSheet("")
                QToolTip.hideText()
                return True

            if obj.objectName() == f'most_frame_{i}' and event.type() == QEvent.Enter:
                obj.setStyleSheet("background-color: rgb(130, 186, 255);")
                QToolTip.setFont(QFont("Arial", 20))  # 툴팁 폰트 설정
                return True

            if obj.objectName() == f'most_frame_{i}' and event.type() == QEvent.Leave:
                obj.setProperty("hovered", False)
                obj.setStyleSheet("")
                QToolTip.hideText()
                return True

        return super().eventFilter(obj, event)


class Game_Page(QMainWindow, SubUI):
    def __init__(self, url):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("게임화면")

        self.url = url

        response = requests.get(self.url)

        html_text = response.text

        self.soup = bs(html_text, 'html.parser')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Main_Page()
    mainWindow.crawling_data()
    mainWindow.show()
    sys.exit(app.exec_())