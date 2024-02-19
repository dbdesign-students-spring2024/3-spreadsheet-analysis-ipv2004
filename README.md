Place your selected data files into this directory.
1. This data is from the *World Health Organization* and details the impact of COVID-19 as the pandemic has evolved over time. It is global excess deaths associated with COVID-19 since January of 2020.
[Here is the link to download that data](https://www.who.int/data/sets/global-excess-deaths-associated-with-covid-19-modelled-estimates)
2. The original file was a zip file containing a .xlsx file, which I converted to a plain text .txt file , reformatted, and converted back to a .xlsx file
3. **Example data:**
| country    | iso3 | year | sex    | age_group | type      | expected.mean | acm.mean | excess.mean |
|:----------:|:----:|:----:|:------:|:---------:|:---------:|:-------------:|:--------:|:-----------:|
| Afghanistan| AFG  | 2020 | Female | 0-24      | predicted | 49084         | 49103    | 0           |
| Afghanistan| AFG  | 2020 | Female | 25-34     | predicted | 6453          | 6691     | 237         |
| Afghanistan| AFG  | 2020 | Female | 35-44     | predicted | 6118          | 6977     | 860         |
| Afghanistan| AFG  | 2020 | Female | 45-54     | predicted | 7712          | 9330     | 1622        |
| Afghanistan| AFG  | 2020 | Female | 55-64     | predicted | 10062         | 12458    | 2401        |
| Afghanistan| AFG  | 2020 | Female | 65-74     | predicted | 13955         | 17144    | 3195        |
| Afghanistan| AFG  | 2020 | Female | 75-84     | predicted | 12752         | 14639    | 1889        |
| Afghanistan| AFG  | 2020 | Female | >85       | predicted | 3695          | 4614     | 922         |
| Afghanistan| AFG  | 2020 | Male   | 0-24      | predicted | 67686         | 67713    | 0           |
| Afghanistan| AFG  | 2020 | Male   | 25-34     | predicted | 15364         | 15619    | 249         |
| Afghanistan| AFG  | 2020 | Male   | 35-44     | predicted | 10605         | 11885    | 1280        |
| Afghanistan| AFG  | 2020 | Male   | 45-54     | predicted | 11164         | 13654    | 2495        |
| Afghanistan| AFG  | 2020 | Male   | 55-64     | predicted | 12852         | 16682    | 3840        |
| Afghanistan| AFG  | 2020 | Male   | 65-74     | predicted | 14370         | 18772    | 4413        |
| Afghanistan| AFG  | 2020 | Male   | 75-84     | predicted | 11140         | 13762    | 2627        |
| Afghanistan| AFG  | 2020 | Male   | >85       | predicted | 2541          | 3461     | 923         |
| Afghanistan| AFG  | 2021 | Female | 0-24      | predicted | 46857         | 46869    | 0           |
| Afghanistan| AFG  | 2021 | Female | 25-34     | predicted | 6413          | 7447     | 1034        |
| Afghanistan| AFG  | 2021 | Female | 35-44     | predicted | 6045          | 7811     | 1767        |
| Afghanistan| AFG  | 2021 | Female | 45-54     | predicted | 7706          | 10622    | 2919        |
4. There were many problems with munging and oragizing the data set. The first of which is that I had a problem with the spacing because a lot of the country names have a space in between them(ie United Arab Emirates), so differetiating them versus the space in between the columns was a challenge. I decided then since the next column consists of 3 letter values, I would parse through till it found 3 letter values then seperate that out as teh next column. However, there were countries with the words "and" or "the", which were also 3 letter words. This forced me to write in exceptions into the code for these specific 3 letter words.
5. **Links to Data Files:**
- [Raw data](data/WHO_COVID_Excess_Deaths_EstimatesByCountry.txt)
- [munged data](munge.py)
- [spreadsheet file](data/clean_dataEXCEL.xlsx)
***ANALYSIS***
1. The aggregate statistics I calculated provided insights in the maximum, minimum  for all the countries, as well as the average and median death. The maximum and minimum showed that a countries had a large amount of deaths, and minimium showed that there were places where there were no reported deaths. The average showed for across all the couuntries, the average death rate throughout the years. Additional analysis showed aggregate statistics with the conditions of gender, giving us the difference of gender in regards to covid deaths. I showed the average across amles, the max for females. the minimum for the reported statistics (without prediction), and the sum for all males.
2. Pivot table:
| Row Labels        | Sum of excess.mean* | Sum of acm.mean | Sum of expected.mean |
|-------------------|---------------------|-----------------|----------------------|
| **predicted**     | 7189147             | 76111839        | 68920523             |
| Afghanistan       | 65731               | 577311          | 511581               |
| Algeria           | 17039               | 227151          | 209932               |
| Angola            | 10995               | 469839          | 458846               |
| Bahrain           | 1699                | 12074           | 10370                |
| Bangladesh        | 160748              | 1794243         | 1633491              |
| Benin             | 3949                | 192327          | 188378               |
| Bhutan            | -341                | 9039            | 9372                 |
| Botswana          | 6472                | 48118           | 41645                |
| Burkina Faso      | 8940                | 312779          | 303842               |
| Burundi           | 2988                | 157906          | 154920               |
| Côte d'Ivoire     | 15989               | 400180          | 384193               |
| Cabo Verde        | 435                 | 3217            | 2780                 |
| Cambodia          | 9107                | 207174          | 198072               |
| Cameroon          | 20862               | 404885          | 384018               |
| Central African Republic | 6454         | 115673          | 109222               |
| Chad              | 9768                | 307605          | 297838               |
I seperated the data based on predicted vs reported, and each country was added up between the years. This gives insight on the imapct of COVID on each individual country. Theses results show that a lot of countries were disporportionally affected by covid, most likely due to their population size, density, access to modern medication, along with numerous other confounding variables.