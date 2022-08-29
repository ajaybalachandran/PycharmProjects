import json
with open('countries.json', 'r', encoding='Utf-8') as file:
    data = json.load(file)
# capital

# population

# currency name

# languages

# borders

# print most populated country

# lowest populated country


# india=[country for country in data if country.get("name")=="India"]
# print(india)

# india_borders=[nation.get("borders") for nation in data if nation.get("name")=="India"]
# print("indian borders=",india_borders)

# china_capital=[china.get("capital") for china in data if china.get("name")=="China"]
# print("capital of china=",china_capital)

# australia_population=[aus.get("population") for aus in data if aus.get("name")=="Australia"]
# print("population of australia=",australia_population)

# nepal_currency=[nepal.get("currencies") for nepal in data if nepal.get("name")=="Nepal"]
# print("nepal currency=",nepal_currency)

# bhutan_languages=[bhutan.get("languages") for bhutan in data if bhutan.get("name")=="Bhutan"]
# print("bhutan languages=",bhutan_languages)

# most_populated=max(data,key=lambda pop:pop.get("population"))
# print("most populated country=",most_populated)

# low_populated=min(data,key=lambda pop:pop.get("population"))
# print("low populated country=",low_populated)


#03-08-22
# names of countries that shares border with india
india_borders = [country.get('borders') for country in data if country.get('name') == 'India'].pop()
# print(india_borders)
country_names = [country.get('name') for country in data if country.get('alpha3Code') in india_borders]
print(country_names)













