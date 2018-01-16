__author__ = 'pavelkosicin'


class NavigateHelper:

    def __init__(self, app):
        self.app = app

    def open_cross_auth_page(self):
        wd = self.app.wd
        wd.get("https://cross-auth-staging.herokuapp.com/?redirect_uri=https%3A%2F%2Fcross-music-staging.herokuapp.com%2Fsearch")
