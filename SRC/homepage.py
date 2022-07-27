import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


## 6 months code

def homepage_case_status(dr):

    base = "https://bombayhighcourt.nic.in/"
    dr.get(base)
    print('On the homepage. Waiting 4 seconds.')
    time.sleep(4)
    #first = dr.find_element_by_link_text("Case Status")
    wait = WebDriverWait(dr, 30)
    action = ActionChains(dr)
    # app = wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Appointment')))
    # dr.execute_script("arguments[0].scrollIntoView();", app)
    # action.move_to_element(app).perform()
    # action.reset_actions()
    first = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Case Status')))
    dr.execute_script("arguments[0].scrollIntoView();", first)
    action.move_to_element(first).perform()
    time.sleep(0.3)
    print('Clicked on case status.')
    action.reset_actions()
    sec = dr.find_element_by_link_text("Case Number Wise")
    sec.click()
    time.sleep(2)
    print("Got to case number status page. Starting inputs.")


def homepage_causelist(dr):
    base = "https://bombayhighcourt.nic.in/"
    dr.get(base)
    print('On the homepage. Waiting 4 seconds.')
    time.sleep(4)
    #first = dr.find_element_by_link_text("Case Status")
    wait = WebDriverWait(dr, 30)
    action = ActionChains(dr)
    # app = wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Appointment')))
    # dr.execute_script("arguments[0].scrollIntoView();", app)
    # action.move_to_element(app).perform()
    # action.reset_actions()
    first = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Causelist')))
    dr.execute_script("arguments[0].scrollIntoView();", first)
    action.move_to_element(first).perform()
    time.sleep(0.3)
    print('Clicked on case status.')
    action.reset_actions()
    sec = dr.find_element_by_link_text("Regular Causelist")
    sec.click()
    time.sleep(2)
    print("Got to causelist page. Getting to archived causelists.")
    arch_button = dr.find_element_by_xpath(r'//*[@href="netbdarchieve.php"]')
    arch_button.click()
    print('Archived causelists. Starting inputs.')
    return 0


def main():
    pass

if __name__ == "__main__":
    main()
