# prime numbers within range
l = int(input('Enter lower limit: '))
u = int(input('Enter upper limit'))
for i in range(l, u):  # 2 - 100
    for j in range(2, i):
        if i % j == 0:
            break
    else:  # if the if statement in above loop not execute then this else is executed
        print(i)
