# Solar profits maximization
<p align="center">
<img src="https://www.letsgosolar.com/wp-content/themes/solar/images/consumer-education-guide/get-solar-panels/sun.png">
</p>

These days everyone is talking about renewable energy and how it should replace the conventional oil and gas. The reality is however that the transition to renewable energy will take time and we need a strategy to implement it.

My report provides an analysis of the curent electricity production by country and the respective CO2 emissions. It targets the countries with high polution and expensive electricity as the primary targets for transition to renewables.

In order to do that I will use the following data sources:

- Electricity production by source - Our World in Data https://ourworldindata.org/energy-mix

- CO2 emmissions by country - Our World in Data https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions

- Solar Photovoltaic potential by country - The World Bank https://datacatalog.worldbank.org/search/dataset/0038379

- Web scraped data from Wikipedia on the solar panel manufacturers

Main assumptions are:

- Find the most poluting countries (per capita)
- Find the countries with best solar potential relative to their polution
- Assess the cost of electricity in those countries and the $ potential of transitioning to solar

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

Below are the top poluters per capita sorted from highest to lowest:

<p align="center">
<img src="https://github.com/berserkus/Solar-Potential/blob/main/output/images/top_poluters.png">
</p>

The data is complemented by solar potential figures - calculated as the total practical potential per day per square meter across the long term

<p align="center">
<img src="https://github.com/berserkus/Solar-Potential/blob/main/output/images/top_cost.png">
</p>

Countries with high electricity costs and high solar potential are our targets.

**Profit potential**

<p align="center">
<img src="https://github.com/berserkus/Solar-Potential/blob/main/output/images/top_potential.png">
</p>

Maldives to Israel - all these countries provide an opportunity to produce revenue of at least $200 per square meter per year. The retail cost of solar panels is roughly $100 per square meter. If you consider the installation and maintenance cost, that might double the cost. But it still means that **your investment pays back in a year!**


### Solar money!
<p align="center">
<img src=https://github.com/berserkus/Solar-Potential/blob/main/output/images/sun_money.jpg">
</p>

**So who might be interested in this?**

## Let's do some Web scraping!

Now let's look at the companies that are producing the solar panels - they are the target recipients of our research! :)

In order to obtain a list of producers and their information, I have scraped the Wikipedia page

https://en.wikipedia.org/wiki/List_of_photovoltaics_companies

Every table containing producer information is scraped and the links collected.

<p align="center">
<img src="https://github.com/berserkus/Solar-Potential/blob/main/output/images/wiki_table1.jpg">
</p>

The code then goes through the list of producers and their links and collects the infromation from within their respective Wikipedia pages

Like the one below:

<p align="center">
<img src="https://github.com/berserkus/Solar-Potential/blob/main/output/images/wiki_table2.jpg">
</p>

After collecting the data on each company and cleaning the information, I export the table into excel.

<p align="center">
<img src="https://github.com/berserkus/Solar-Potential/blob/main/output/images/excel_export.jpg">
</p>

## Now let's make some calls!

<p align="center">
<img src="http://gif-free.com/uploads/posts/2017-04/1491130956_obama-making-call.gif">
</p>