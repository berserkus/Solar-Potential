import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import re
import statsmodels.api as sm
from scipy import signal
import scipy as sp
import requests
from bs4 import BeautifulSoup as BS

# clean the electriciy production database
def cleanseries(el_prod,co2):

    # cut out the date before 1985 as it is not relevant
    el_prod=el_prod[el_prod['Year']>=1985]
    co2=co2[co2['year']>=1985]

    el_prod.rename(columns={'Entity':'Country'},inplace=True)
    el_prod.sort_values(['Country','Year'],ascending=True, inplace=True)
    sort_cols=['Country','Code','Year','Coal','Gas','Oil','Nuclear','Bioenergy','Hydro','Solar','Wind']
    columns=['Coal','Gas','Oil','Nuclear','Bioenergy','Hydro','Solar','Wind']
    el_prod=el_prod[sort_cols]
    el_prod['Total']=el_prod[columns].sum(axis=1)

    co2.rename(columns={'country':'Country', 'year':'Year'},inplace=True)
    co2.sort_values(['Country','Year'],ascending=True, inplace=True)
    co2.drop(['cement_co2_per_capita','coal_co2_per_capita','flaring_co2_per_capita','gas_co2_per_capita','oil_co2_per_capita','other_co2_per_capita'], inplace=True, axis=1)

    series=pd.merge(el_prod,co2,on=['Country','Year'], how='inner')
    series['gdp_per_capita']=series['gdp world bank']/series['population']


    return series

def getstatic(series,solar,year):

    static=series[series['Year']==year]
    static.drop(['iso_code','trade_co2','cement_co2','coal_co2','flaring_co2','gas_co2','oil_co2','other_industry_co2'],inplace=True, axis=1)
    static['Renewable %']=(static['Bioenergy']+static['Hydro']+static['Solar']+static['Wind'])/static['Total']
    static.sort_values('co2_per_capita',ascending=False, inplace=True)
    static=pd.merge(static,solar,on='Country', how='inner')
    # get 100 countries (excluding low income and tiny countries)
    static=static[(static['gdp_per_capita']>5000)&(static['population']>500000)][:100]

    return static

# Web scraping
def scrape(url):

    res=requests.get(url)
    html=res.content
    soup=BS(html, "html.parser")
    table1=pd.read_html(html)[2]
    table2=pd.read_html(html)[3]
    link=soup.find_all('td')
    #loop, check
    all_links=[]
    for i in link:
        try:
            all_links.append(i.find_all('a')[0].get('href'))
        except:
            all_links.append('')
    while '' in all_links:
        all_links.remove('')  
    clean_links=[]
    for i in all_links:
        if 'note-' in i or 'index.' in i:
            pass
        else:
            clean_links.append(i)
    
    df_companies=table1[['Solar modulecompany','Country']][:13]
    df_companies.rename(columns={'Solar modulecompany':'Company'}, inplace=True)
    df_temp=table2[['Company','Country']]
    list_col=df_companies.columns
    df_companies.columns=df_companies.columns.to_flat_index()
    df_companies.rename(columns={list_col[0]:'Company',list_col[1]:'Country'},inplace=True)
    df_temp.columns=df_temp.columns.to_flat_index()
    df_temp.rename(columns={list_col[0]:'Company',list_col[1]:'Country'},inplace=True)
    df_companies=pd.concat([df_companies, df_temp])


    dict_links={}
    for i in df_companies['Company']:
        for j in clean_links:
            if i.split(' ')[0] in j:
                dict_links[i]='https://wikipedia.org'+j

    df=pd.DataFrame([dict_links])
    df_links=df.T
    df_links.rename(columns={0:'Link'}, inplace=True)
    df_links.reset_index(inplace=True)
    df_links.rename(columns={'index':'Company'},inplace=True)
    df_links

    # create the first row of the dataframe scrape
    url_t='https://wikipedia.org/wiki/Jinko'
    res=requests.get(url_t)
    html=res.content
    soup=BS(html, "html.parser")
    table=pd.read_html(html)
    df_t=table[2]
    df_T=df_t.T
    df_T.columns=df_T.iloc[0]
    df_scrape=df_T[1:]
    df_scrape['Company']='Jinko'
    df_scrape

    # cycle through the links to get the required tables
    for key, value in dict_links.items():
        url=value
        res=requests.get(url)
        html=res.content
        soup=BS(html, "html.parser")
        table=pd.read_html(html)
        # check which table contains Website - this will be the table you are looking for
        for i in range(3):
            try:
                if 'Website' in str(table[i]):
                    num=i
            except:
                pass

        df_t=table[num]
        df_T=df_t.T
        df_T.columns=df_T.iloc[0]
        df_T=df_T[1:]
        df_T['Company']=key
        try:        
            df_scrape = pd.concat([df_T, df_scrape], join='outer')    
        except:
            pass

    com_columns=['Company','Type','Industry','Founded','Website','Headquarters','Number of employees','Products','Founder','Founders','Key people','Parent','Traded as','Subsidiaries','Operating income','Net income','Total assets','Total equity']
    df_comp_full=df_scrape[com_columns]
    df_comp_full=df_comp_full.dropna(subset=['Website'])

    pattern_year='\d{4}'
    patt_num='\d{2,}'

    df_c=df_comp_full

    df_c["Founded"]=df_c.apply(lambda row: str(re.findall(pattern_year,str(row["Founded"])))[2:-2], axis=1)
    df_c["Number of employees"]=df_c.apply(lambda row: str(row["Number of employees"]).replace(',',''), axis=1)
    df_c["Number of employees"]=df_c.apply(lambda row: re.findall(patt_num,str(row["Number of employees"])), axis=1)
    df_c['Number of employees']=df_c['Number of employees'].str[0]

    def clean_spec(element,list,remain): # remain is the value that is given if no match is found, 'same' leaves the same value
        sk=[i.capitalize() for i in list if i in str(element).lower()]
        if sk==[]:
            if remain=='same':
                sk=element
            else:
                sk=remain
        else:
            sk=str(sk[0]) 
        return sk
    
    type_list=['public', 'limited company', 'private']

    df_c['Type']=df_c['Type'].apply(clean_spec,args=(type_list,'same'))


    return df_c