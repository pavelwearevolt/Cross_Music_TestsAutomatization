__author__ = 'pavelkosicin'


class SearchHelper:

    def __init__(self, app):
        self.app = app

    def enter_query(self, query):
        wd = self.app.wd
        wd.find_element_by_css_selector("input._1gqlopWZDC5Z6kRHlB2qmr.form-control").click()
        wd.find_element_by_css_selector("input._1gqlopWZDC5Z6kRHlB2qmr.form-control").clear()
        wd.find_element_by_css_selector("input._1gqlopWZDC5Z6kRHlB2qmr.form-control").send_keys(query)
        wd.find_element_by_link_text("Songs(11)").click()
