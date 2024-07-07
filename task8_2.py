def modifyList(l: list):
    l.insert(0, l.pop())

n = int(input())

listNum = list(map(int, input().split()))


modifyList(listNum)

print(listNum)