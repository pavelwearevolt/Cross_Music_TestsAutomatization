__author__ = 'pavelkosicin'

from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.search import SearchHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.search = SearchHelper(self)

    def open_cross_auth_page(self):
        wd = self.wd
        wd.get(
            "https://cross-auth-staging.herokuapp.com/?redirect_uri=https%3A%2F%2Fcross-music-staging.herokuapp.com%2Fsearch")

    def destroy(self):
        self.wd.quit()
