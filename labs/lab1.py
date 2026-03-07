# Lab 1

is_prime = True

while True:
    user_number = input("Number: ")

    if user_number.lower() == 'q':
        print("Bye!")
        exit()
    try:
        n = int(user_number)
        break
    except ValueError:
        print("Not an integer.")

if n <= 3:
    # Check if below 1, which includes 0 which is not a prime.
    is_prime = n > 1
elif n % 2 == 0 or n % 3 == 0:
    is_prime = False
else:
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            is_prime = False
            break
        else:
            i += 6

if is_prime:
    print("Prime.")
else:
    print("Not prime.")

