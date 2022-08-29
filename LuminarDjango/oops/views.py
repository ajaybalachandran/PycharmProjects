from oops.models import mobiles
class ViewMobiles:
    def get(self):
        return mobiles
    def post(self, *args, **kwargs):
        new_data = kwargs.get('data')
        mobiles.append(new_data)
        return mobiles


all_mobiles = ViewMobiles()
print(all_mobiles.get())
data = {"id": 1011, "name": "iphone11", "band": "5g", "display": "OLED", "price": 47000, "brand": "apple"}
print(all_mobiles.post(data=data))
