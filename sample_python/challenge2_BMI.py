def bmi_calc(w, h):
    bmi = w / (h ** 2)
    return bmi


weight = float(input('Enter the height in KG:'))
height = float(input('Enter the height in METER:'))
result = bmi_calc(weight, height)
print(result)
