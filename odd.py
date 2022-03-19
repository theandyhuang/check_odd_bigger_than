def add_odd_3():
    number1 = int(input("please enter a number: "))
    sum2 = 0
    i = 1
    for i in range(number1+1):
        if (i % 2) != 0:
            sum2 += i
    print(f"Summation from 1 to {number1} is {sum2}")

add_odd_3()