# Lab 4

while True:
    try:
        triangle_height = int(input("Enter the height of the triangle: "))
        if triangle_height < 1:
            print("Less than 1. Try again.")
            continue
        else:
            break
    except ValueError:
        print("Not an integer.")
        

i = triangle_height

while i >= 1:
    print("*" * i)
    i -= 1