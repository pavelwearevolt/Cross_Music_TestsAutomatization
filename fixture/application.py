__author__ = 'pavelkosicin'

from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.search import SearchHelper
from fixture.navigation import NavigationHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.search = SearchHelper(self)
        self.navigation = NavigationHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
