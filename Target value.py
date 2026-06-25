lst = []

print("Enter 5 values:")
for i in range(6):
    lst.append(int(input()))

target = int(input("Enter target value: "))

if target in lst:
    print("Target found at index:", lst.index(target))
else:
    print("Target not found")
