def celsius_to_fahrenheit(celsius):
    fahrenheit_value = (celsius * 9 / 5) + 32
    # print(fahrenheit_value)
    return fahrenheit_value

def fahrenheit_to_celsius(fahrenheit):
    celsius_value = (fahrenheit - 32) * 5/9
    # print(celsius_value)
    return celsius_value

# celsius_to_fahrenheit(0)    # 32.0
# celsius_to_fahrenheit(100)  # 212.0
# fahrenheit_to_celsius(32)   # 0.0
# fahrenheit_to_celsius(212)  # 100.0
