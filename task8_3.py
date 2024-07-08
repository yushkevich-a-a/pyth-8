n = int(input("рыбаков: "))

w_b = int(input('грузоподъемность лодки: '))

cnt = 1

l1 = []

for i in range(n):
    r = int(input())
    l1.append(r)

l1.sort()

w = 0

for i in l1:
    w += i
    if w > w_b:
        cnt += 1
        w = i
        

print(cnt)


