from typing import List

def square_odd_only(list: List[int]):
    new_list = []

    for i in list:
        if i % 2 == 0:
            continue
        else:
            i_squared = i**2
            new_list.append(i_squared)

    return new_list

while True:
    try:
        user_input_number = int(input("How many numbers? "))
        list = []

        for i in range(user_input_number):
            user_input_to_list = int(input(f"Number {i + 1}: "))
            list.append(user_input_to_list)

        break
    
    except ValueError:
        print("Not an integer. Try again.")
    
squared_odd_only_list = square_odd_only(list)
print(squared_odd_only_list)

