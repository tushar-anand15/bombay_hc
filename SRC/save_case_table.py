from bs4 import BeautifulSoup
import pandas as pd



def save_case_table(dr,start_date,end_date,ctype):
    page_source = dr.page_source
    soup = BeautifulSoup(page_source,'lxml')
    print('saving the temporary table.')
    try:
        table = soup.find('table',{'class':'table table-bordered'})
    except Exception as e:
        print('error. no table found. returning None.')
        return None
    else:
        df = pd.read_html(table.decode())[0]
        df.columns = df.iloc[0]
        df = df[1:]
        df[['start_date','end_date','case_type']] = start_date,end_date,ctype
        #tag = df['Case No'].iloc[0].split('/')[0]
        print('saving to temporary file.')
        df.to_csv(f'../DATA/temp/{start_date}_{end_date}_{ctype}.csv')
        return df




def main():
    pass

if __name__ == '__main__':
    pass