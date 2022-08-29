mark1 = int(input('Enter the mark of subject 1 out of 100:'))
mark2 = int(input('Enter the mark of subject 2 out of 100:'))
mark3 = int(input('Enter the mark of subject 3 out of 100:'))
if mark1 > 100 or mark2 > 100 or mark3 > 100:
    print('wrong')
else:
    per = ((mark1 + mark2 + mark3) / 300) * 100
    print(f'percentage is {per}')
    if per > 80:
        print('Distinction')
    elif per >= 60 and per < 80:
        print('First class')
    elif per >= 50 and per < 60:
        print('Second class')
    elif per >= 45:
        print('Passed')
    else:
        print('failed')