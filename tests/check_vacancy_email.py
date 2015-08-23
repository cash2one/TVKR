# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time


def test_check_vacancy_email(app):
    wd = app.wd
    actions = ActionChains(wd)
    app.session.login_as(app.users["user1"])
    app.open_page("resume") # размещаем вакансию с известным нам e-mail для ответа
    title = "Тест создания вакансии %s" % int(time.time())
    wd.find_element_by_xpath("//span[.='Разместить вакансию']").click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//input[@id='Vacancy_name']"))
    wd.find_element_by_xpath("//input[@id='Vacancy_name']").send_keys(title)
    wd.find_element_by_xpath("//span[@class='select2-chosen' and .='Проф. область']").click()
    wd.find_element_by_xpath("//div[@class='select2-result-label' and .='Кино']").click()
    wd.find_element_by_xpath("//span[@class='select2-chosen' and .='Специальность']").click()
    wd.find_element_by_xpath("//div[@class='select2-result-label' and .='Агент']").click()
    wd.find_element_by_xpath("//span[@class='select2-chosen' and .='Город']").click()
    wd.find_element_by_xpath("//div[@class='select2-result-label' and .='Амстердам']").click()
    wd.find_element_by_xpath("//textarea[@id='Vacancy_smartDescription']").send_keys("Тест создания вакансии")
    wd.find_element_by_xpath("//input[@id='Vacancy_email']").send_keys("vacancy_testing@mail.com")
    wd.find_element_by_xpath("//input[@id='Vacancy_company_name']").send_keys("Sample Company")
    button = wd.find_element_by_xpath("//input[@class='btn btn_green btn_green_big']")
    actions.move_to_element(button).perform()
    wd.find_element_by_xpath("//input[@class='btn btn_green btn_green_big']").click()
    wait(wd, 10).until(lambda s: wd.find_element_by_css_selector("div.vacancy"))
    app.session.login_as(app.users["user2"])
    app.open_page("job")
    wd.find_element_by_xpath("//a[.='%s']" % title).click()
    wait(wd, 10).until(lambda s: wd.find_element_by_css_selector("a.create-vacancy-response")).click()
    wait(wd, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.vacancy-response-popup span.btn__inner"))).click()
    wait(wd, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.response-sent")))
    app.session.login_as(app.users["admin"])
    app.open_page("admin/emailQueue")
    assert "vacancy_testing@mail.com" == wd.find_element_by_xpath("//tbody/tr[1]/td[4]").text
