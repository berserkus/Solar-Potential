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