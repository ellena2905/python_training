# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class cont(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_cont(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/addressbook/edit.php")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("123")
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("123")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("123")
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("123")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("123")
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("123")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("133")
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("123")
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("123")
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("123")
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("123")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys("\\9")
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("123")
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("123")
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("123")
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[1]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[14]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[14]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[14]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[14]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[14]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[14]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("2010")
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[14]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[14]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[14]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[14]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[14]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[14]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[1]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2020")
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("123")
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("123")
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("123")
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
