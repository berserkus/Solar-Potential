import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import re
import statsmodels.api as sm
from scipy import signal
import scipy as sp

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

