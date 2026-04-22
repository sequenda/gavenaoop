def write_line_to_file():
    with open("mylife.txt", "w") as f:
        while True:
            line = input("Enter line: ")
            f.write(f"{line}\n")

            choice = input("Are there more lines (y/n)? ")
            if choice.lower() == 'n':
                break

write_line_to_file()
