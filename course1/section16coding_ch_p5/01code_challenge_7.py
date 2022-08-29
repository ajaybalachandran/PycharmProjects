# Assume you want to build two functions for discounting products on a
# website.
# Function number 1 is for student discount which discounts the current price
# to 10%.
# Function number 2 is for additional discount for regular buyers which
# discounts an additional 5% on the current student discounted price.
# Depending on the situation, we want to be able to apply both the discounts
# on the products.
# Design the above two mentioned functions and apply them both
# simultaneously on the price

def stud_dis(p):
    f_price = p - (p * (10 / 100))
    return f_price


def reg_dis(p2):
    f_price = p2 - (p2 * (5 / 100))
    return f_price


current_p = int(input('Enter the current price of the product: '))
res = reg_dis(stud_dis(current_p))
print(f'Final price after student discount and regular buyers is: {res}')
