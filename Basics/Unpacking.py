lst = [1, 2, 3]
a, b, c = lst
print(f"a = {a}, b = {b}, c = {c}")

lst = [1, 2, 3, 4, 5]
a, b, *c = lst
print(f"a = {a}, b = {b}, c = {c}")

data = ("Name", ( 12, 18.9 ))
a, (b ,c) = data
print(f"a = {a}, b = {b}, c = {c}")