import allure
from locators import basicfirstfordemo_locators
from selenium.webdriver.support.select import Select

from locators.basicfirstfordemo_locators import BasicfirstfordemoLocators


class BasicFirstFormDemoPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('open https://www.seleniumeasy.com/test/basic-first-form-demo.html')
    def open_page_first_form_demopag(self):
        self.driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

    @allure.step('Close popup')
    def close_popup(self):
        self.driver.find_element(*BasicfirstfordemoLocators.close_popup).click()

    @allure.step('Select Single Input Field')
    def input_single_input_field(self, sif):
        self.driver.find_element_by_xpath('//input[@id="user-message"]').send_keys(sif)

    @allure.step('click on the Show Message button')
    def click_show_message_button(self):
        self.driver.find_element_by_xpath('//button[@onclick="showInput();"]').click()

    @allure.step('Two Input Fields - Enter a')
    def input_single_input_field1(self, tifa):
        self.driver.find_element_by_xpath('//input[@id="sum1"]').send_keys(tifa)

    @allure.step('Two Input Fields - Enter b')
    def input_single_input_field2(self, tifb):
        self.driver.find_element_by_xpath('//input[@id="sum2"]').send_keys(tifb)

    @allure.step('click on the Show Message button')
    def click_show_message_buttonn(self):
        self.driver.find_element_by_xpath('//button[@onclick="return total()"]').click()
