def add_odd_2():
    number1 = int(input("please enter a number: "))
    sum2 = 0
    i = 1
    while i <= number1:
        if (i % 2) != 0:
            sum2 += i
        i += 1
    print(f"Summation from 1 to {number1} is {sum2}")

add_odd_2()