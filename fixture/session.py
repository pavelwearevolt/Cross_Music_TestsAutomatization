__author__ = 'pavelkosicin'


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.navigation.open_cross_auth_page()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//div[@class='sign-in-control-box']//button[.='Log In']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("button.CYQcOAG72sePIKz5BZDTC").click()
        wd.find_element_by_css_selector("button._2WXT4B32gqEbBn72l2tJtW._3ZnfiGA-jAw_cmYoE7ln9d").click()
