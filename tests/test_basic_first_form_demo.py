import allure
from pages.basicfirstformdemo_page import BasicFirstFormDemoPage


class TestSimpleForDemo:
    @allure.title('Open basic-first-form-demo')
    def test_user_can_open_basic_first_form_demo_page(self, driver):
        sif = "test"
        tifa = 2
        tifb = 4

        basic_first_form_demo_page = BasicFirstFormDemoPage(driver)
        basic_first_form_demo_page.open_page_first_form_demopag()
        basic_first_form_demo_page.close_popup()
        basic_first_form_demo_page.input_single_input_field(sif)
        basic_first_form_demo_page.click_show_message_button()
        basic_first_form_demo_page.input_single_input_field1(tifa)
        basic_first_form_demo_page.input_single_input_field2(tifb)
        basic_first_form_demo_page.click_show_message_buttonn()
