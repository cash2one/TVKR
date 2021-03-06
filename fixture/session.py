# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait


class User:

    def __init__(self, username, password, real_name, role):
        self.username = username
        self.password = password
        self.real_name = real_name
        self.role = role


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_as(self, user):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(user):
                return
            else:
                self.logout()

        wd.get(self.app.base_url + "login")
        wait(wd, 10).until(lambda s: wd.find_element_by_id('UserForm_email'))
        wd.find_element_by_id('UserForm_email').send_keys(user.username)
        wd.find_element_by_id('UserForm_password').send_keys(user.password)
        wd.find_element_by_id('submit_link').click()
        wait(wd, 10).until(lambda s: self.is_logged_in())

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        return len(self.app.wd.find_elements_by_css_selector("div.account__info")) > 0\
            or len(self.app.wd.find_elements_by_css_selector("a[href='/admin/systemInfo/index']")) > 0

    def is_logged_in_as(self, user):
        wd = self.app.wd
        account_info = self.app.wd.find_elements_by_css_selector("div.account__info")
        return (len(account_info) > 0 and account_info[0].text == user.real_name)\
            or (user.role == "admin" and len(self.app.wd.find_elements_by_css_selector("a[href='/admin/systemInfo/index']")) > 0)

    def logout(self):
        wd = self.app.wd
        self.app.open_page("logout")
