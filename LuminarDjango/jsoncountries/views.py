import json
with open('countries.json', 'r', encoding='Utf-8') as file:
    data = json.load(file)

# # capital of a certain country
# capital_ind = [country.get('capital') for country in data if country.get('name') == 'India']
# print(capital_ind)

# # currency name of bhutan
# currencies = [country.get('currencies') for country in data if country.get('name') == 'Bhutan'].pop()
# currency_names = [currency.get('name') for currency in currencies]
# print(currency_names)


# currency_names = [cname.get('name') for cname in ([country.get('currencies') for country in data if country.get('name') == 'Bhutan'].pop())]
# print(currency_names)

# # population of china
# population_china = [country.get('population') for country in data if country.get('name') == 'China']
# print(population_china)

# # languages of india
# india_lang = [india.get('name') for india in [country.get('languages') for country in data if country.get('name') == 'India'].pop()]
# print(india_lang)


# # borders
# china_borders = [borders.get('borders') for borders in data if borders.get('name') == 'China'].pop()
# border_countries = [country.get('name') for country in data if country.get('alpha3Code') in china_borders]
# print(border_countries)


# # print most populated country
# most_populated = max(data, key=lambda c: c.get('population')).get('name')
# print(most_populated)


# # lowest populated country
# less_populated = min(data, key=lambda c: c.get('population')).get('name')
# print(less_populated)


# # names of countries that shares border with india
# india_borders = [country.get('borders') for country in data if country.get('name') == 'India'].pop()
# border_names = [border.get('name') for border in data if border.get('alpha3Code') in india_borders]
# print(border_names)


