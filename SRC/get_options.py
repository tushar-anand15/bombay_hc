import pandas as pd
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from homepage import homepage_case_status

def get_options_text(dr):
    side_dropdown = Select(dr.find_element_by_name('m_sideflg'))
    side_options = [i.text for i in side_dropdown.options]
    options_text = list()
    for side_option in side_options:
        side_dropdown = Select(dr.find_element_by_name('m_sideflg'))
        side_dropdown.select_by_visible_text(side_option)
        time.sleep(3)
        opts = Select(dr.find_element_by_name('m_skey'))
        opts_text = [i.text for i in opts.options]
        options_text.append(opts_text)
    
    my_dict = dict(zip(side_options,options_text))
    df = pd.DataFrame.from_dict(my_dict,orient='index')
    df = df.T
    df.columns = df.iloc[0]
    df.drop(df.iloc[0],axis=1,inplace=True)
    df.to_csv(f'../DATA/total_case_types.csv',sep='|')
    return my_dict

def main():
    
    print(f'generating options for case types')
    dr = webdriver.Chrome()
    homepage_case_status(dr)
    get_options_text(dr)
    print(f'saved file.')
    dr.close()
    pass

if __name__ == '__main__':
    main()




