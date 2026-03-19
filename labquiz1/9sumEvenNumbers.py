def sum_even_numbers(numbers):
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return sum(even_numbers)
    


# list_1 = [1,3,4,5,6,7,8,9,12]
# list_2 = [3,4,56,78,14,56]

# print(sum_even_numbers(list_1))
# print(sum_even_numbers(list_2))
