lst = []
n = int(input("Enter number of elements: "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print(f"Your list is {lst}")
p = lst.copy()
p.sort()
lst.sort(reverse=True)
print(lst)
m = p[::-1]
print(m)
i = 0
j = n-1
while i < n/2:
    while j > n/2:
        temp = p[i]
        p[i] = p[j]
        p[j] = temp
        j -= 1
    i += 1
print(p)
