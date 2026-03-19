def calculate_stats(numbers):
    count_of_numbers = len(numbers)
    sum_of_numbers = sum(numbers)
    average = sum_of_numbers / count_of_numbers
    max_number = max(numbers)
    min_number = min(numbers)

    return {
        'count': count_of_numbers,
        'sum': sum_of_numbers,
        'average': average,
        'max': max_number,
        'min': min_number
    }

