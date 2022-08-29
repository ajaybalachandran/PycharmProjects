import re
zipcode = '2121-1313-3424'
result = re.sub(r'\D', '@', zipcode)  # \D non-digits
print(result)
result2 = re.sub(r'\d', '@', zipcode)  # \d digits
print(result2)