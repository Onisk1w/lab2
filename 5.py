print("введите числа")
a = list(map(int, input().split()))
b = []
print(a)
for item in a:
    if item not in b:
        b.append(item)
for item in b:
    print(item)

