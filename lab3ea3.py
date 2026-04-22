import random
from pathlib import Path

first_names = ["Ben", "Alice", "John", "Sarah", "Phil", "Emma", "Victor", "Luna", "Christian", "Angel", "Bella", "Angelica", "Marc", "Mark", "Allen", "Roger"]
last_names = ["Dover", "Smith", "Stone", "Light", "McChill", "Wick", "Vance", "Grayson", "Johnson", "Raven"]

file_path = Path.cwd() / "gpa.txt"

def generate_name():
    full_name = f"{random.choice(first_names)} {random.choice(last_names)}"

    gwa = round(random.uniform(75, 100), 2)

    return f"{full_name}, {gwa}"


def highest_gwa():
    winner_name = ""
    winner_gwa = 0.0

    # just in case file doesn't exist or is empty
    if not file_path.exists() or file_path.stat().st_size == 0:
        with open(file_path, "w") as f:
            for _ in range(20):
                f.write(f"{generate_name()}\n")
    
    with open(file_path, "r") as f:
        for line in f:
            name_and_gwa = line.strip().split(",")
            # error checking
            if len(name_and_gwa) < 2:
                continue

            name = name_and_gwa[0].strip()
            gwa = float(name_and_gwa[1].strip())

            if gwa > winner_gwa:
                winner_gwa = gwa
                winner_name = name

    print(f"Top student is {winner_name} with a GWA of {winner_gwa}.")

highest_gwa()
