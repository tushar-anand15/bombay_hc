import time
from selenium.webdriver.support.ui import Select



def set_case_params(dr,start_date,end_date,case_type,side):
    print("selecting the case type.")
    case_side_select = Select(dr.find_element_by_name("m_sideflg"))
    case_side_select.select_by_visible_text(side)
    time.sleep(1)
    case_type_select = Select(dr.find_element_by_name("m_skey"))
    case_type_select.select_by_visible_text(case_type)
    time.sleep(1)
    start_date_box = dr.find_element_by_xpath(r'//*[@id="demo1"]')
    end_date_box = dr.find_element_by_xpath(r'//*[@id="demo2"]')
    #dr.execute_script('document().getElementById("demo1").removeAttribute("onfocus")')
    #dr.execute_script('document.getElementById("demo2").removeAttribute("onfocus")')
    print("removed blur attributes.")
    time.sleep(1)
    start_date_box.send_keys(start_date)
    end_date_box.send_keys(end_date)

    print("sent dates")
    time.sleep(2)

    #click_button = dr.find_element_by_xpath(r'//*[@id="submit11"]')
    #click_button.click()
    print("sending the captcha")
    time.sleep(1)
    cp = dr.find_element_by_xpath(r'//*[@id="captchaimg2"]')
    captcha_text = cp.get_attribute('src').split('=')[-1]
    print(f"captcha text: {captcha_text}")

    captcha_text_box = dr.find_element_by_xpath(r'//*[@id="captcha_code2"]')
    captcha_text_box.send_keys(captcha_text)
    go_button = dr.find_element_by_xpath(r'//*[@id="submit11"]')
    time.sleep(2)
    go_button.click()
