print("введите числа")
a = input().split(' ')
for i in range(len(a)):
    a[i] = int(a[i]) ** 2
print(a)