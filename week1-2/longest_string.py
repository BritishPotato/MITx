long = ""
old = ""
old_long = ""

for char in "ltqaxwhruu":
    if char >= old:
        long += char
        old = char
    elif char < old:
        if len(old_long) < len(long):
            old_long = long
        long = char
        old = char

if len(long) > len(old_long):
    old_long = long

print("Longest substring in alphabetical order is: " + old_long)