mobiles = [
    {"id": 1000, "name": "samsungA52", "band": "4g", "display": "AMOLED", "price": 27000, "brand": "samsung"},
    {"id": 1001, "name": "samsungA52s", "band": "5g", "display": "AMoLED", "price": 32000, "brand": "samsung"},
    {"id": 1002, "name": "redminote10", "band": "4g", "display": "led", "price": 17000, "brand": "redmi"},
    {"id": 1003, "name": "redminote11pro", "band": "5g", "display": "superAMOLED", "price": 20000, "brand": "redmi"},
    {"id": 1004, "name": "samsungA72", "band": "5g", "display": "AMOLED", "price": 27000, "brand": "samsung"},
    {"id": 1005, "name": "samsungA53", "band": "5g", "display": "AMOLED", "price": 27000, "brand": "samsung"},
    {"id": 1006, "name": "samsungm52", "band": "5g", "display": "AMOLED", "price": 27000, "brand": "samsung"},
    {"id": 1007, "name": "samsungm53", "band": "5g", "display": "AMOLED", "price": 27000, "brand": "samsung"},
    {"id": 1008, "name": "samsungA22", "band": "5g", "display": "AMOLED", "price": 27000, "brand": "samsung"},
    {"id": 1009, "name": "iphone13", "band": "5g", "display": "AMOLED", "price": 97000, "brand": "apple"},
    {"id": 1010, "name": "oneplusnordce2", "band": "5g", "display": "AMOLED", "price": 23000, "brand": "oneplus"}

]

# map, filter
# max, min
# sort

# # 1. print all mobile names
# mob_names = [mob.get('name') for mob in mobiles]
# print(mob_names)

# # 2. print all mobile names with 5g band
# five_g = [mob.get('name') for mob in mobiles if mob.get('band') == '5g']
# print(five_g)

# # 3. print the details of costly mobile
# costly_mobile = max(mobiles, key=lambda mob: mob.get('price'))
# print(costly_mobile)

# # 4. print the details of cheap mobile
# cheap_mobile = min(mobiles, key=lambda mob: mob.get('price'))
# print(cheap_mobile)

# # 5. sort the mobiles based on price in ascending order
# mobiles.sort(key=lambda mob: mob.get('price'))
# print(mobiles)

# # 6. sort the mobiles based on the price in descending order
# mobiles.sort(key=lambda mob: mob.get('price'), reverse=True)
# print(mobiles)

# # 7. filter the name mobiles have price between 25k to 32k
# mid_mobiles = [mob.get('name') for mob in mobiles if mob.get('price') in range(25000, 32001)]
# print(mid_mobiles)

# # 8. print the details of iphone13
# iphone_mob = [mob for mob in mobiles if mob.get('name') == 'iphone13']
# print(iphone_mob)

# # 9. name of phones between 15000 and 28000 other than samsung brand
# mob_list = [mob.get('name') for mob in mobiles if mob.get('price') in range(15000, 28001) and mob.get('brand') != 'samsung']
# print(mob_list)

# # 10. all 5g mobiles less than 100000 with brand iphone
# mob_list1 = [mob.get('name') for mob in mobiles if mob.get('band') == '5g' and mob.get('price') in range(100001) and mob.get('brand') == 'apple']
# print(mob_list1)


# # find the cheapest mobile from samsung brand
# samsung_mob = [mob for mob in mobiles if mob.get('brand') == 'samsung']
# min_samsung = min(samsung_mob, key=lambda mob: mob.get('price'))
# print(min_samsung)

# print all 5g mobiles name and price
details = [[mob.get('name'), mob.get('price')] for mob in mobiles if mob.get('band')=='5g']
print(details)