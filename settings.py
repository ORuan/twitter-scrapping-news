from selenium import webdriver
import threading
from controller import URL
import chromedriver_autoinstaller
from pathlib import Path
from time import sleep


BASE_DIR = Path(__file__).resolve(strict=True).parent


class TwitterScrappingBot():
    def initialization(self):
        try:
            _path = chromedriver_autoinstaller.install()
        except Exception as err:
            print("Error in instalation ", err)
        try:
            _web_driver = webdriver.ChromeOptions()
            # _web_driver.add_argument("--headless")
            _web_driver.add_argument(f"user-data-dir={BASE_DIR}/.seln_data/")
            _web_driver.add_argument("--no-sandbox")
            _web_driver.add_argument("--disable-gpu")
            _web_driver.add_argument("--ignore-certificate-errors")
            _web_driver.add_argument("--test-type")
            _web_driver.add_argument("--disable-dev-shm-usage")
            _web_driver.add_argument("--disable-extensions")
            _web_driver.add_argument("--start-maximized")
            _web_driver.add_argument("--disable-software-rasterizer")
            _web_driver.add_argument("disable-infobars")
            _web_driver.add_argument("lang=pt-br")
            return webdriver.Chrome(options=_web_driver, executable_path=_path)
        except Exception as err:
            print("Error in initialization ", err)

    def __init__(self):
        self.instance = self.initialization()

    def monitoring(self):
        content_trending = self.instance.execute_script("""function _get(){
                                                            document.body.style.zoom='25%'
                                                            content = document.querySelectorAll('.css-1dbjc4n.r-16y2uox.r-bnwqim')
                                                            return Array.prototype.slice.call(content)
                                                        };return _get();
                                                        """)
        while True:
            pass
        print(content_trending)
        #btn_news_path = "//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[4]/a"
        #content_news = self.instance.find_element_by_xpath(btn_news_path)
        #print(content_news)


    def open(self):
        self.instance.get(URL)
        sleep(3)
        self.monitoring()

TwitterScrappingBot().open()