def print_diamond(n):
    center = n // 2
    
    for i in range(0, center + 1):
        print("   " * (center - i) + " * " * ((2 * i) + 1) + "   " * (center - i))

    for j in range(center - 1, -1, -1):
        print("   " * (center - j) + " * " * ((2 * j) + 1) + "   " * (center - j))


while True:
    try:
        user_n = int(input("Odd integer only: "))

        if user_n % 2 == 0:
            print("Please provide an odd integer.")
        else:
            break
    except ValueError:
        print("Please provide an odd integer")
    
print_diamond(user_n)