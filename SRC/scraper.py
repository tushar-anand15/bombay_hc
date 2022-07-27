from selenium.webdriver.support.ui import Select
from selenium import webdriver
import pandas as pd
import time
import get_options
import set_case_params
import re
import os
from homepage import homepage_case_status, homepage_causelist
from save_case_table import save_case_table
from parse_case_details import parse_case_details, parse_each_case



if not os.path.exists('../DATA/total_case_types.csv'):
    print('options file not found. generating.')
    get_options.main()

my_options = pd.read_csv('../DATA/total_case_types.csv', sep='|')

selected_options = [{'side':'Original' , 'type': 'Commercial Suit'},{'side':'Original','type':'COMMERCIAL SUMMARY SUITS'},{'side':'Original','type':'SUMMARY SUITS.'},{'side':'Original','type':'COMMERCIAL SUMMARY SUITS'},{'side':'Original','type':'SUITS'}]

# to select options
# my_options.loc[my_options['Original'].str.contains('suits',regex=True,flags=re.I)]['Original']

start_date = '01-06-2021'
end_date = '01-07-2021'
filepath = os.path.abspath(r"/mnt/d/my_projects/bombay_high_court/DATA/orders/")
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('prefs', {
        "download.default_directory" : filepath,
        "download.prompt_for_download" : False,
            "download.directory_upgrade" : True,
            "plugins.always_open_pdf_externally": True,
            "download.extensions_to_open": ""
        })


for selected_option in selected_options:
        
    dr = webdriver.Chrome(options=chromeOptions)
    homepage_case_status(dr)

    set_case_params.set_case_params(dr,start_date,end_date,selected_option['type'],selected_option['side'])
    save_case_table(dr,start_date, end_date, selected_option['type'])
    a_tags = dr.find_elements_by_tag_name('a')
    a_tags = [i for i in a_tags if i]
    case_links = [i for i in a_tags if i.get_attribute('href') if 'bhcpar' in i.get_attribute('href')]
    for case_link in case_links:
        parse_each_case(dr,case_link, start_date, end_date,selected_option['type'],selected_option['side'])
    #print('closing this instance of the driver. moving on.')

    dr.close()

# case_links = dr.find_elements_by_xpath('//a[@href]')
# case_links = [i for i in case_links if 'bhcpar' in i.get_attribute('href')]

selected_option = selected_options[0]
dr = webdriver.Chrome(options=chromeOptions)
homepage_case_status(dr)
set_case_params.set_case_params(dr,start_date,end_date,selected_option['type'],selected_option['side'])
save_case_table(dr,start_date, end_date, selected_option['type'])
a_tags = dr.find_elements_by_tag_name('a')
a_tags = [i for i in a_tags if i]
case_links = [i for i in a_tags if i.get_attribute('href') if 'bhcpar' in i.get_attribute('href')]
for case_link in case_links:
    parse_each_case(dr,case_link, start_date, end_date,selected_option['type'],selected_option['side'])
    print('sleeping for 3 seconds.')
    time.sleep(3)
#print('closing this instance of the driver. moving on.')
dr.close()