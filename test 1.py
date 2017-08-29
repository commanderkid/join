def returner(x, y, z):
    m = x * y + z
    b = 0
    while m > 0:
        m = m/10
        n = round(m - int(m), 1)
        m = int(m)
        h = int(n*10)
        b = h + b
        print(m, n, h, b)
    return b

g = returner(120, 10, 232)

