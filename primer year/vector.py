n = int(input("n:"))
v = [None]*n
for i in range (n):
    v[i] = int(input("v:"))
v[1] = v[::-1]
print(v)