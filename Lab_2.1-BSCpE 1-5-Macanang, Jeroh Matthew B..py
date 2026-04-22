from pathlib import Path


python_dir = Path.cwd()
numbers_path = python_dir / "numbers.txt"
evens_path = python_dir / "even_numbers.txt"
odds_path = python_dir / "odd_numbers.txt"

try:
    with open(numbers_path, "w+", encoding="utf-8") as numf, \
         open(odds_path, "w", encoding="utf-8") as oddf, \
         open(evens_path, "w", encoding="utf-8") as evenf:
        
        for i in range(1, 21):
            numf.write(f"{i}\n")

        numf.seek(0)
        

        for line in numf:
            clean_line = line.strip()
            if not clean_line:
                continue

            try:
                num = int(clean_line)
                if num % 2 == 0:
                    evenf.write(f"{num}\n")
                else:
                    oddf.write(f"{num}\n")
            except ValueError:
                continue
                
    print(f"Success. Files created in: {python_dir}")
        
except PermissionError:
    print("Error: Permission denied. Check your directory write access.")
except Exception as e:
    print(f"Err: {e}")