# Solar Potential
<p align="center">
<img src="https://www.letsgosolar.com/wp-content/themes/solar/images/consumer-education-guide/get-solar-panels/sun.png">
</p>

These days everyone is talking about renewable energy and how it should replace the conventional oil and gas. The reality is however that the transition to renewable energy will take time and we need a strategy to implement it.

My report provides an analysis of the curent electricity production by country and the respective CO2 emissions. It targets the countries with high polution and expensive electricity as the primary targets for transition to renewables.

In order to do that I will use the following data sources:

- **Electricity production by source** - Our World in Data https://ourworldindata.org/energy-mix

- **CO2 emmissions by country** - Our World in Data https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions

- **Solar Photovoltaic potential by country** - The World Bank https://datacatalog.worldbank.org/search/dataset/0038379

- **Web scraped data from Wikipedia** on the solar panel manufacturers

Main goals and hypotheses are:

- **Find the most poluting countries (per capita)**
- **Find the countries with best solar potential relative to their polution**
- **Assess the cost of electricity in those countries and the $ potential of transitioning to solar**
- **Find companies that would be most interested in this analysis**

### Polution analysis

The database provides the timeseries of CO2 polution by country for a number of years. After cleaning and data analysis it seems that there is more complete data since 1985.

The chart below shows the development of CO2 emissions in some of the largest poluter economies:

<p align="center">
<img src="https://github.com/berserkus/Solar-Potential/blob/main/output/images/polute_series.png">
</p>

These same countries look very different when viewed as CO2 emissions per capita:

<p align="center">
<img src="https://github.com/berserkus/Solar-Potential/blob/main/output/images/polute_per_capita.png">
</p>

### Country analysis

Below we give the user to see the composition of electricity production and CO2 emissions for any country of his choosing.

**USA vs China**

<p align="center">
<img src="https://github.com/berserkus/Solar-Potential/blob/main/output/images/us_china_production.jpg">
</p>



<p align="center">
<img src="https://github.com/berserkus/Solar-Potential/blob/main/output/images/us_china_gdp.jpg">
</p>

### Poluters in 2019

Given the complete year end dataset ends in 2020 - which was a year with very low CO2 emissions, I prefer to use 2019 as the year for comparison.

Below are the top poluters per capita sorted from highest to lowest, complemented by solar potential figures - calculated as the total potential solar generation per day per square meter across the long term:

<p align="center">
<img src="https://github.com/berserkus/Solar-Potential/blob/main/output/images/top_poluters.png">
</p>

Considering that in most of the developped countries the industrial companies will have to buy CO2 credits - high polution might become expensive. But at the moment as it is not universally enforceable, the current incentive should be linked to the electricity costs.

Below I sort the countries by electricity cost by USD cents per kWh:

<p align="center">
<img src="https://github.com/berserkus/Solar-Potential/blob/main/output/images/top_cost.png">
</p>

Countries with high electricity costs and high solar potential are our targets.

Next I calculate the monetary potential in these countries by multiplying electricity costs by solar potential, by 365 days and by 20%. Here 20% is used as a coefficient for solar panel efficiency. New generation solar panels like the Meyer Burger Hetero Junction Type panels have efficiency of 22%.

**Profit potential**

<p align="center">
<img src="https://github.com/berserkus/Solar-Potential/blob/main/output/images/top_potential.png">
</p>

The profit potential differs quite a bit across the list where countries from Maldives to Dominican Republic present an interesting opportunity for solar power transition. The retail cost of solar panels is roughly $100 per square meter - for wholesale installations it might be even cheaper. If you consider the installation and initial maintenance cost, it might increase the cost to $150 per square meter. But it still means that in the selected countries **our investment in solar panels would pay back in less than three years! Yield > >40%!**


**So who might be interested in this?**



## Let's do some Web scraping!

<p align="center">
<img src="https://s3.amazonaws.com/businessinsider.mx/wp-content/uploads/2020/11/27172446/Wikipedia.jpg">
</p>

Now let's look at the companies that are producing the solar panels - they are the target recipients of our research!

In order to obtain a list of producers and their information, I perform a webscraping of the Wikipedia page:

https://en.wikipedia.org/wiki/List_of_photovoltaics_companies

Every table containing producer information is scraped and the corresponding information and links are collected.

<p align="center">
<img src="https://github.com/berserkus/Solar-Potential/blob/main/output/images/wiki_table1.jpg">
</p>

Once we have the list of names and links the code cycles through the links and collects the infromation from within their respective Wikipedia pages.

We are interested in the company specific information which will be contained in the table like the one below:

<p align="center">
<img src="https://github.com/berserkus/Solar-Potential/blob/main/output/images/wiki_table2.jpg">
</p>

From each page a dataframe is created and then merged with the main dataframe. After cleaning and sorting the data the resulting dataframe is stored in excel.

An extract of it is shown below:

<p align="center">
<img src="https://github.com/berserkus/Solar-Potential/blob/main/output/images/excel_export.jpg">
</p>


## Conclusions!

In this report I have looked at the electricity production and CO2 developlemnt across the countries, which provided some interesting insights. By merging this dataset with the solar potential across each country I could identify which countries present the greatest opportunity to install solar panels.

The main takeaways from this research are:

- **The CO2 emmissions are linked to GDP but only in emerging countries.**
- **The highest CO2 emmitters usually have quite cheap electricity.**
- **Countries with high electricity costs and solar potential present a perfect opportunity for solar transition.**