side_length = int(input("Enter the side length of the square: "))

i = 1
while i <= side_length:
    if i == 1 or i == side_length:
        print("x" * side_length)
    else:
        print("x", end="")
        print(" " * (side_length - 2), end="")
        print("x")
    i += 1 