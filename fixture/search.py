__author__ = 'pavelkosicin'
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class SearchHelper:

    def __init__(self, app):
        self.app = app

    def enter_query(self, query):
        wd = self.app.wd
        wd.find_element_by_css_selector('input._1gqlopWZDC5Z6kRHlB2qmr.form-control').click()
        wd.find_element_by_css_selector('input._1gqlopWZDC5Z6kRHlB2qmr.form-control').clear()
        wd.find_element_by_css_selector('input._1gqlopWZDC5Z6kRHlB2qmr.form-control').send_keys(query)
        time.sleep(3)

    def check_response_title(self, expected_result_title, error_message):
        wd = self.app.wd
        check_list_title = []
        # find all query results, all elements
        response_title = wd.find_elements_by_tag_name('h3')
        for element in response_title:
            if element.text == expected_result_title:
                check_list_title.append(element)
        assert len(check_list_title) > 0, error_message

    def check_response_person(self, expected_result_person, error_message):
        wd = self.app.wd
        check_list_person = []
        # find all query results, all elements
        response_person = wd.find_elements_by_class_name('_2IqTsnyvwST0XvZ5OkddE7')
        for element in response_person:
            if element.text == expected_result_person:
                check_list_person.append(element)
        assert len(check_list_person) > 0, error_message
