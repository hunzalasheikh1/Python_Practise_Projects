import pandas as pd
countries = []
cities = []
text = pd.read_csv('data.csv')
#print(text)
for i in text["countries"]:
    countries.append(i)
for p in text["cities"]:
    cities.append(p)
    
print(countries)
print(cities)
print(type(countries))