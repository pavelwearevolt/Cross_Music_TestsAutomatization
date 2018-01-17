__author__ = 'pavelkosicin'


class SearchHelper:

    def __init__(self, app):
        self.app = app

    def enter_query(self, query):
        wd = self.app.wd
        wd.find_element_by_css_selector("input._1gqlopWZDC5Z6kRHlB2qmr.form-control").click()
        wd.find_element_by_css_selector("input._1gqlopWZDC5Z6kRHlB2qmr.form-control").clear()
        wd.find_element_by_css_selector("input._1gqlopWZDC5Z6kRHlB2qmr.form-control").send_keys(query)

    def check_search_result(self, expected_result):
        wd = self.app.wd
        check_list = []
        # find all query results, all elements
        search_output = wd.find_elements_by_tag_name("h3")
        for element in search_output:
            if element.text == expected_result:
                check_list.append(element)
        assert len(check_list) > 0, "Nothing found"

