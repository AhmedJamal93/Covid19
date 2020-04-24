import pandas as pd
import numpy as np
import io
import requests
import matplotlib.pyplot as plt

# ## DATA FOR CONFIRMED CASES GLOBAL
# url="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
# s=requests.get(url).content
# cases_glob=pd.read_csv(io.StringIO(s.decode('utf-8')))
# cases_glob.drop(columns =['Lat', 'Long'], inplace = True)
#
# ## DATA FOR DEATHS GLOBAL
# url="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
# s=requests.get(url).content
# deaths_glob=pd.read_csv(io.StringIO(s.decode('utf-8')))
# deaths_glob.drop(columns =['Lat', 'Long'], inplace = True)
#
# ## DATA FOR CONFIRMED CASES USA
# url="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
# s=requests.get(url).content
# cases_us=pd.read_csv(io.StringIO(s.decode('utf-8')))
# cases_us.drop(columns =['UID', 'iso2','iso3','code3','FIPS','Admin2','Lat','Long_','Combined_Key'], inplace = True)
# cases_us.rename(columns ={'Province_State':'Province/State','Country_Region':'Country/Region'}, inplace = True)
#
# ## DATA FOR DEATHS USA
# url="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"
# s=requests.get(url).content
# deaths_us=pd.read_csv(io.StringIO(s.decode('utf-8')))
# deaths_us.drop(columns =['UID', 'iso2','iso3','code3','FIPS','Admin2','Lat','Long_','Combined_Key','Population'], inplace = True)
# deaths_us.rename(columns ={'Province_State':'Province/State','Country_Region':'Country/Region'}, inplace = True)
#
# ## CONCATING DATAFRAMES
# cases = pd.concat([cases_glob,cases_us], ignore_index = True)
# deaths = pd.concat([deaths_glob,deaths_us], ignore_index = True)
#
# ## GROUPING BY COUNTRY REGION
# cases_group = cases.groupby('Country/Region').sum()
# deaths_group = deaths.groupby('Country/Region').sum()
#
# ## ADDING NEW ROW FOR WORLD
# cases_world = cases_group.sum(numeric_only=True)
# cases_group.loc['World'] = cases_world
# deaths_world = deaths_group.sum(numeric_only=True)
# deaths_group.loc['World'] = deaths_world
#
# ## SAVING FILE
# cases_group.to_csv('cases_all.csv')
# deaths_group.to_csv('deaths_all.csv')

## READING FILE
cases = pd.read_csv('cases_all.csv')
deaths = pd.read_csv('deaths_all.csv')

## PLOTTING GRAPH
period = len(deaths.columns)
dti = pd.date_range('2020-01-22', periods= (period-1), freq='D').date

deaths.set_index('Country/Region',inplace=True)
deaths = deaths.T

cases.set_index('Country/Region',inplace=True)
cases = cases.T


final_list = []
while 1:
    user_input = input("Enter Country, Enter Stop when completed: ")
    if user_input == "Stop":
        break
    final_list.append(user_input)
print(final_list)

plt.figure(figsize = (10,6))
plt.title('Deaths vs. Cases Over Time Due to Coronavirus')
plt.xlabel('Date')
plt.ylabel('Number of Deaths(-),Cases(--)')

for country in final_list:
    plt.plot(dti, deaths[country], label = country)
    plt.annotate('%0.0f' % deaths[country].max(), xy=(1, deaths[country].max()), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')

plt.gca().set_prop_cycle(None)

for country in final_list:
    plt.plot(dti, cases[country],'--')
    plt.annotate('%0.0f' % cases[country].max(), xy=(1, cases[country].max()), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')
    max = cases[country].max()
    if cases[country].max() > max:
        max = cases[country].max()
    else:
        continue

plt.xticks(dti[::3], rotation = 'vertical')
y1 = np.arange(0, max, step = (max/20))
plt.yticks(y1)
plt.margins(0)
plt.legend()
plt.grid()
plt.show()
