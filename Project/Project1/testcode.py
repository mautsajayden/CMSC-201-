def value(x):
    n = 0
    val = 0
    for i in x.split():
        n += 1
        if n == 2:
            val = int(i)
    return val

print("hello")
print(value("mul 65"))


