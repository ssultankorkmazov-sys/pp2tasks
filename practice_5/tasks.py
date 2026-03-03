import re

with open("exmpl.txt", "r", encoding="utf-8") as f:
    exmp = f.read()

# Task 1
print("-"*10, "Task 1", "-"*10)
pattern = r"\bab*\b"
print(bool(re.search(pattern, exmp)))

# Task 2
print("-"*10, "Task 2", "-"*10)
pattern = r"\bab{2,3}\b"
print(bool(re.search(pattern, exmp)))

# Task 3
print("-"*10, "Task 3", "-"*10)
pattern = r"\b[a-zа-я]+(?:_[a-zа-я]+)+\b"
print(*re.findall(pattern, exmp), sep="\n")

# Task 4
print("-"*10, "Task 4", "-"*10)
pattern = r"\b[A-ZА-Я][a-zа-я]+\b"
print(*re.findall(pattern, exmp), sep="\n")

# Task 5
print("-"*10, "Task 5", "-"*10)
pattern = r"^a.*b$"
print(*re.findall(pattern, exmp, re.MULTILINE), sep="\n")

# Task 6
print("-"*10, "Task 6", "-"*10)
result = re.sub(r"[ ,\.]", ":", exmp)
print(result)

# Task 7
print("-"*10, "Task 7", "-"*10)
def to_camel(s):
    return re.sub(r"_([a-z])", lambda m: m.group(1).upper(), s)

print(to_camel(exmp))

# Task 8
print("-"*10, "Task 8", "-"*10)
pattern = r"(?=[A-ZА-Я])"
result = re.split(pattern, exmp)
print(*result, sep="\n")

# Task 9
print("-"*10, "Task 9", "-"*10)
result = re.sub(r"(?<!^)([A-ZА-Я])", r" \1", exmp)
print(result)

# Task 10
print("-"*10, "Task 10", "-"*10)
result = re.sub(r"(?<!^)([A-ZА-Я])", r"_\1", exmp).lower()
print(result)