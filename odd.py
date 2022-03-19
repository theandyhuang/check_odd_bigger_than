def add_odd_1():
    number1 = int(input("please enter a number: "))
    sum2 = 0
    i = 1
    while i <= number1:
        if not (i % 2):
            i += 1
            continue
        sum2 += i
        i += 1
    print(f"Summation from 1 to {number1} is {sum2}")

add_odd_1()