def primeFact (i, f):
    if i < f:
        return []
    if i % f == 0:
        return [f] + primeFact (i / f, 2)
    return primeFact (i, f + 1)


print(primeFact(int(input("Enter a number to decompose: ")),2))