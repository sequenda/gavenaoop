def get_user_info(data, user_id):
    for dict in data:
        if dict.get("id") == user_id:
            return dict
    return {"error": "User not found"}

# users = [
#     {"id": 1, "name": "Alice", "age": 25},
#     {"id": 2, "name": "Bob", "age": 30},
#     {"id": 67, "name": "Brainrot", "age": 67}
# ]
# result_1 = get_user_info(users, 2)
# result_2 = get_user_info(users, 67)

# print(result_1)
# print(result_2)
