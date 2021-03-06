# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from baseurl import Baseurl

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class photo_album_create_edit_delete(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_photo_album_create_edit_delete(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl))
        wd.find_element_by_link_text("Войти").click()
        time.sleep(5)
        wd.find_element_by_id("UserForm_email").send_keys("123@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").send_keys("1111")
        wd.find_element_by_id("submit_link").click()
        time.sleep(5)
        wd.find_element_by_xpath("//ul[@id='yw1']//strong[.=' Фотографии']").click()
        time.sleep(5)
        wd.find_element_by_xpath("//div[@class='btn__holder']//span[.='Добавить альбом']").click()
        time.sleep(5)
        wd.find_element_by_id("Album_name").send_keys("New album")
        wd.find_element_by_id("Album_body").send_keys("Sample description")
        wd.find_element_by_name("yt0").click()
        time.sleep(5)
        wd.find_element_by_xpath("//div[@class='company-box__section']//a[.='Редактировать альбом']").click()
        time.sleep(5)
        wd.find_element_by_id("AlbumUser_name").click()
        wd.find_element_by_id("AlbumUser_name").clear()
        wd.find_element_by_id("AlbumUser_name").send_keys("New New album")
        wd.find_element_by_id("AlbumUser_body").click()
        wd.find_element_by_id("AlbumUser_body").clear()
        wd.find_element_by_id("AlbumUser_body").send_keys("Новое описание")
        wd.find_element_by_name("yt0").click()
        time.sleep(5)
        wd.find_element_by_xpath("//div[@class='company-box__section']//a[.='Редактировать альбом']").click()
        time.sleep(5)
        if wd.find_element_by_id("AlbumUser_body").text != "Новое описание":
            success = False
            print("verifyText failed")
        wd.find_element_by_css_selector("div.clearfix.delete-album > label").click()
        wd.find_element_by_name("yt0").click()
        time.sleep(5)
        if not ("Пока нет загруженных фотографий" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
