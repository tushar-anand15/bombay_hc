from selenium.webdriver.support.ui import Select


def parse_causelist(dr,side,date):
    month_select = Select(dr.find_element_by_name('mmonth'))
    month_select.select_by_index(1)
    year_select = Select(dr.find_element_by_name('myear'))
    year_select.select_by_index(1)
    date_select = Select(dr.find_element_by_name('m_causedt'))
    date_select.select_by_index(1)
    cp = dr.find_element_by_xpath(r'//*[@id="captchaimg"]')
    cp_code = cp.get_attribute('src').split('=')[1]
    captcha_input_box = dr.find_element_by_name('captcha_code')
    captcha_input_box.send_keys(cp_code)
    go_button = dr.find_element_by_xpath(r"//*[@value='GO']")
    go_button.click()
    return None