import pandas as pd
country = []
text = pd.read_csv('hello.csv')
print(text)
for i in text["countries"]:
    country.append(i)
print(country)
print(type(country))