s = int(input("Enter the number of stars: "))
l = int(input("Enter the number of lines: "))
b = int(input("Enter the number of blocks: "))
total = 0
for i in range (b):
    c=0
    for j in  range (l):
        for k in range (s):
            print("*", end= " ")
            c += 1
            total += 1
        print()
    print(c)
    print()
    l = l-1
print(f"total {total}")