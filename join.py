a = int(input())
d, d1 = [], []
def returner(x, y, z):
    m = x * y + z
    b = 0
    while m > 0:
        m = m/10
        n = round(m - int(m), 1)
        m = int(m)
        h = int(n*10)
        b = h + b      
    return b

for i in range(a):
    c = input()
    j = i
    d.append(c.split())
    d[j] = [int(d[j]) for d[j] in d[j]]
    g = returner(d[j][0], d[j][1], d[j][2])
    d1.append(str(g))
    
print(" ".join(d1))
