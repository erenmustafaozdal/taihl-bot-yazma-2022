from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Tarayici:

    def __init__(self):
        self.tarayici = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.tarayici.maximize_window()

    def al(self):
        return self.tarayici
