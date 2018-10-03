long = ""
old = ""
old_long = ""

for char in "fhadsfhfjkabcdopsafhkfhgldsge":
    if char >= old:
        long += char
        old = char
    elif char < old:
        if len(old_long) < len(long):
            old_long = long
        long = ""
        old = char

print("Longest substring in alphabetical order is: " + old_long)