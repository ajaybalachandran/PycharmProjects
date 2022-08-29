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

dis=[mob.get('name') for mob in mobiles if mob.get('display')=='led']
print(dis)

high=max(mobiles,key=lambda mob:mob.get('price'))
print(high)

rate=[mob for mob in mobiles if mob.get('price')<25000]
print(rate)

mini=min(mobiles,key=lambda mob:mob.get('price'))
print(mini)

mobiles.sort(key=lambda mob:mob.get('price'))
print(mobiles)