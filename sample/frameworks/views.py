# from frameworks.models import frameworks
# # print all framework names
# fw_names = [fw.get('fwname') for fw in frameworks]
# print(fw_names)
#
# # print all framework names whose rating > 4
# top_rated = [fw.get('fwname') for fw in frameworks if fw.get('rating') > 4]
# print(top_rated)
#
# # print all python framework name
# py_fw = [fw.get('fwname') for fw in frameworks if fw.get('language') == 'python']
# print(py_fw)
#
# # most rated
# most_rated = max(frameworks, key=lambda fw: fw.get('rating'))
# print(most_rated)
#
# # low rated
# low_rated = min(frameworks, key=lambda fw: fw.get('rating'))
# print(low_rated)


from frameworks.models import mobiles
# # 1 print all mobile names
# mob_names = [mob.get('name') for mob in mobiles]
# print(mob_names)


# # 2 print all mobile names with 5g band
# fiveg_mob = [mob.get('name') for mob in mobiles if mob.get('band') == '5g']
# print(fiveg_mob)


# # 3 print the details of costly mobile
# costly_mob = max(mobiles, key=lambda mob: mob.get('price'))
# print(costly_mob)


# # 4 print the details of cheap mobile
# cheap_mob = min(mobiles, key=lambda mob: mob.get('price'))
# print(cheap_mob)


# # 5 sort mobiles based on price in ascending order
# mobiles.sort(key=lambda mob: mob.get('price'), reverse= False)
# print(mobiles)


# # 6 sort mobiles based on price in descending order
# mobiles.sort(key=lambda mob: mob.get('price'), reverse=True)
# print(mobiles)


# # 7. filter the name mobiles have price between 25k to 32k
# mob_filter = [mob.get('name') for mob in mobiles if mob.get('price') in range(25000, 32001)]
# print(mob_filter)


# # 8. print the details of iphone13
# iphone = [mob for mob in mobiles if mob.get('name') == 'iphone13']
# print(iphone)


# # 9. name of phones between 15000 and 28000 other than samsung brand
# phones = [mob.get('name') for mob in mobiles if mob.get('price') in range(15000, 28001) and mob.get('brand') != 'samsung']
# print(phones)


# # 10. all 5g mobiles less than 100000 with brand iphone
# mobiles = [mob.get('name') for mob in mobiles if mob.get('band') == '5g' and mob.get('price') < 100000 and mob.get('brand') == 'apple']
# print(mobiles)


# # 11. find the cheapest mobile from samsung brand
# samsung_mobiles = [mob for mob in mobiles if mob.get('brand') == 'samsung']
# cheap_samsung = min(samsung_mobiles, key=lambda sm: sm.get('price'))
# print(cheap_samsung)

# 12. print all 5g mobiles name and price
mobiles_price = [[mob.get('name'), mob.get('price')] for mob in mobiles if mob.get('band') == '5g']
print(mobiles_price)



