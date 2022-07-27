#importing packages
import selenium
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import re
import itertools
import glob
import subprocess
import json
from bs4 import BeautifulSoup
import time
import pandas as pd
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from collections import ChainMap

def parse_case_details(dr):
    soup = BeautifulSoup(dr.page_source, 'lxml')
    rows = soup.findAll('tr')
    filtered_rows = [i for i in rows if re.search('\w|\d',i.text)]
    cells = [r.findAll('td') for r in filtered_rows]
    cells = [i for i in cells if i]
    my_dict=dict()
    for i in cells:
        if len(i)>1:
            key = i[0].text.strip()
            val = i[1].text.strip()
            my_dict.update({key:val})
        if len(i) == 1:
            try:
                key,val = i[0].text.strip().split(':-')
            except Exception as e:
                print(e)
                print(i)
            else:
                my_dict.update({key:val})
    fvs = list()
    final_dict = my_dict.copy()
    for key, value in my_dict.items():
        if ':-' in value:
            my_ind = value.rfind(':-')
            
            print(f"faulty value:         {value}")
            print(my_ind)
            print(value[my_ind])
            fvs.append(value)
            final_dict.pop(key)
        if (':-' in key):
            my_ind = key.rfind(':-')
            if my_ind !=len(key) - 2:            
                print(f"faulty key:         {key}")
                print(my_ind)
                print(key[my_ind])
                fvs.append(key)
        

    x = [i.split(':-') for i in fvs]
    update_dict = dict()

    for i in x:
        md = {i[0]:i[1]}
        update_dict.update(md)

    final_dict.update(update_dict)
    #_ = [my_dict.pop(i) for i in fvs if i in my_dict.items()]
    return final_dict

# office_info, misc_info, objections, paper_index, connected_matters, appl_cases, listing_dates_orders, lower_court_details


def get_listing_dates_orders(dr,case_name):
    listing_dates_button = dr.find_element_by_xpath(r'//*[@name="btnadjournlist1"]')
    print('Getting listing dates.')
    try:
        dr.execute_script("arguments[0].scrollIntoView();", listing_dates_button)
        print('Switching to a new tab.')
        action = ActionChains(dr)
        action.key_down(Keys.CONTROL).click(listing_dates_button).perform()
        dr.switch_to.window(dr.window_handles[-1])
        time.sleep(1)
    except Exception as e:
        print(e)
        return None
    else:
        soup = BeautifulSoup(dr.page_source, 'lxml')
        try:
            table = soup.find('table',{'class':'table table-border'})
        except Exception as e:
            print("table not found! error.")
            return None
        else:
            ldf = pd.read_html(table.decode())[0]
            try:
                clean_ldf = ldf[ldf.loc[ldf[ldf.columns[0]].str.contains('Date')].index[0]:]
            except Exception as e:
                print('date data not found.')
            else:
                clean_ldf.reset_index(inplace=True)
                clean_ldf.drop('index',inplace=True,axis=1)
                clean_ldf.columns = clean_ldf.iloc[0]
                clean_ldf_dict =clean_ldf.to_dict(orient='records')
                print('finished operations. saving the orders.')
                try:
                    get_orders(dr,case_name)
                except Exception as e:
                    print(e)
                    print('failed to get orders. returning data.')
                    return clean_ldf_dict
                else:
                    print('finished this menu. exiting.')    
                    dr.close()
                    dr.switch_to.window(dr.window_handles[-1])

                    return clean_ldf_dict


def get_orders(dr,case_name):
    links = dr.find_elements_by_xpath(r'//a[@href]')
    order_links = [i for i in links if 'bhcpar' in i.get_attribute('href')]
    for ix, order_link in enumerate(order_links):
        actions  = ActionChains(dr)
        # saving first order as test..
        #ix = 1
        actions.key_down(Keys.CONTROL).click(order_links[ix]).perform()
        time.sleep(3)
        list_of_files = glob.glob(r'../DATA/orders/*.pdf')
        time.sleep(2)
        try:
            latest_file = max(list_of_files, key=os.path.getctime)
        except Exception as e:
            print("file not downloaded yet. waiting for 5 more seconds.")
            print(e)
            time.sleep(5)
        else:
            os.rename(latest_file,f'../DATA/orders/{case_name}_{ix}.pdf')
            print('saved file.')

    #rename latest file to the case
    # move onto the next after renaming
    # exit this page here?


def get_office_info(dr):
    office_info_button = dr.find_element_by_xpath(r'//*[@name="btnordjud"]')
    print('Getting office_info')
    try:
        dr.execute_script("arguments[0].scrollIntoView();", office_info_button)
        action = ActionChains(dr)
        print('Switching to a new tab.')
        action.key_down(Keys.CONTROL).click(office_info_button).perform()
        dr.switch_to.window(dr.window_handles[-1])
        time.sleep(1)
    except Exception as e:
        print(e)
        return None
    else:
        soup = BeautifulSoup(dr.page_source, 'lxml')
        table = soup.find('table',{'class':'table table-bordered'})
        tds = [i.text for i in table.find_all('td') if i]
        for t in tds:
            if 'Not found' in t:
                office_info_dict = {'office_info':'None'}
        
        if not office_info_dict:
            info_df = pd.read_html(table.decode())[0]
            office_info_dict = {'office_info': info_df.to_dict(orient='records')}



        return office_info_dict

def get_misc_info():
    return None

def get_objections():
    return None

def get_paper_index():
    return None

def get_connected_matters():
    return None

def get_appl_cases():
    return None



def get_lower_court_details():
    return None





def parse_each_case(dr,case_link_element,start_date, end_date,case_type,case_side):
        case_name = case_link_element.text
        case_name = case_name.replace('/','-')
        print(f"sending requests for {case_name}")
        wait = WebDriverWait(dr, 30)
        actions = ActionChains(dr)
        try:
            
            #dr.execute_script("arguments[0].scrollIntoView();", home)
            #actions.move_to_element(home).perform()
            #actions.reset_actions()
            dr.execute_script("arguments[0].scrollIntoView();", case_link_element)
            #first_case = case_link_elements[1]
            actions.key_down(Keys.CONTROL).click(case_link_element).perform()
            actions.reset_actions()
            print("Switching to a new tab")
            dr.switch_to.window(dr.window_handles[-1])
            time.sleep(1)
        except Exception as e:
            print(e)
            #logger.error(f"Error sending request for case no. {case_name}. Date range {start_date}, {end_date}. Case type: {case_type}")
            input()
        else:
            print("request successful. parsing the data.")
            try:
                case_data = parse_case_details(dr)
            except Exception as e:
                print(e)
                print('error in parsing case page.')
            else:

                update_dict = {'start_date':start_date, 'end_date':end_date, 'case_type': case_type, 'side': case_side}
                case_data.update(update_dict)
                print('got the case details. parsing listing dates. ')
                try:
                    listing_dates = get_listing_dates_orders(dr,case_name)
                except Exception as e:
                    print(e)
                    print('error in parsing listing dates.')
                else:
                    update_dict = {'listing_dates':listing_dates}
                    case_data.update(update_dict)
            with open(f'../DATA/sample_data/{case_type}_{case_name}.json','w') as file:
                json.dump(case_data, file)
            print('file saved. closing the window.')
        while (len(dr.window_handles)>1):
                dr.switch_to_window(dr.window_handles[-1])
                dr.close()
        dr.switch_to_window(dr.window_handles[-1])



    
        return None



