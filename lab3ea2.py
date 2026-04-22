import random
from pathlib import Path


current_file = Path.cwd() / "integers.txt"
double_file = Path.cwd() / "double.txt"
triple_file = Path.cwd() / "triple.txt"

def doubles_and_triples():
    # just in case file doesn't exist or is empty
    # generates random 20 integers, from -1000 to 999
    if not current_file.exists() or current_file.stat().st_size == 0:
        with open(current_file, "w") as f:
            for _ in range(20):
                random_number = random.randint(-1000, 1000)
                f.write(f"{random_number}\n")

    with open(current_file, "r") as integers_file, \
        open(double_file, "w") as doubles_file, \
        open(triple_file, "w") as triples_file:

        for line in integers_file:
            number = int(line.strip())

            if number % 2 == 0:
                doubles_file.write(f"{number ** 2}\n")

            else:
                triples_file.write(f"{number ** 3}\n")

doubles_and_triples()
