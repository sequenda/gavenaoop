def calculate_grade(scores):
    grade_sum = sum(scores)
    grade_len = len(scores)
    
    average = grade_sum / grade_len
    average_rounded = round(average)
    
    if average_rounded < 60:
        grade_letter = 'F'
    elif average_rounded >= 60 and average_rounded <= 69:
        grade_letter = 'D'
    elif average_rounded >= 70 and average_rounded <= 79:
        grade_letter = 'C'
    elif average_rounded >= 80 and average_rounded <= 89:
        grade_letter = 'B'
    elif average_rounded >= 90 and average_rounded <= 100:
        grade_letter = 'A'
    else:
        return None

    if average_rounded and grade_letter:
        return {'average': average, 'grade': grade_letter}
    else:
        return None
    



# grade_list = [95, 87, 92, 88]
# print(calculate_grade(grade_list))
