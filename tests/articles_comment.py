# -*- coding: utf-8 -*-
from time import gmtime, strftime
from selenium.webdriver.support.wait import WebDriverWait as wait
import time


def test_articles_comment(app):
    wd = app.wd
    app.open_page("article/article4029-pravila-hudozhnika-po-grimu-marii-morzunovoj")
    wait(wd, 60).until(lambda s: wd.find_element_by_xpath("//li[@class='comment-welcome']/a[.='Войдите']")).click()
    app.login(username="123@guerrillamail.com", password="1111")
    unique_comment = "comment" + strftime("%H:%M:%S", gmtime())  # генерируем уникальный коммент
    wait(wd, 60).until(lambda s: wd.find_element_by_id("Comment_comment_text")).send_keys(unique_comment)
    wait(wd, 60).until(lambda s: wd.find_element_by_link_text("Отправить")).click()
    time.sleep(3)
    assert unique_comment in wd.find_element_by_tag_name("body").text