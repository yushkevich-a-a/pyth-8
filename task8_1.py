n = int(input())

a = []

for i in range(n):
    b = int(input())
    a.append(b)

a.reverse()
print(" ".join(map(str, a)))