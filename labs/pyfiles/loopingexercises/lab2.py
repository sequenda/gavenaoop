# Lab 2

array_size = int(input("Enter the size of array: "))
elements = input(f"Enter {array_size} elements, separated with a space: ").split()

if len(elements) != array_size: # mismatch check
    print(f"Warning: {len(elements)} numbers were provided, {array_size} expected.")

arr_1 = []

for i in range(min(array_size, len(elements))): # select which is lower
    num = int(elements[i])
    arr_1.append(num)

print("Cubes:")
for j in arr_1:
    print(j ** 3)
