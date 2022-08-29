# Create a BMI calculator, BMI which stands for Body Mass Index can be
# calculated using the formula:
# BMI = (weight in Kg)/(Height in Meters)^2.
# Write python code which can accept the weight and height of a person and
# calculate his BMI.
# note: Make sure to use a function which accepts the height and weight
# values and returns the BMI value.


def bmi_calc(h, w):
    bmi = w / h ** 2
    return bmi


height = float(input('Enter the height in Meters: '))
weight = float(input('Enter the weight in KG: '))
res = bmi_calc(height, weight)
print('BMI = ', round(res, 1))
