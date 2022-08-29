import json
with open('users.json', 'r') as file:
    data = json.load(file)
names = [user.get('name') for user in data]
print(names)
persons = [user.get('name') for user in data if user.get('salary') > 50000]
print(persons)
hr_user = [user.get('name') for user in data if user.get('department') == 'hr']
print(hr_user)
# highest salaried employee
hi_sal_emp = max(data, key=lambda u: u.get('salary'))
print(hi_sal_emp)
low_payed = min(data, key=lambda u: u.get('salary'))
print(low_payed)
# sort employees based on salary order by desc
data.sort(key=lambda u: u.get('salary'), reverse=True)
print(data)

