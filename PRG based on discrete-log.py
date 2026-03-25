def prg_dlog(seed, g, p, length):
    x = seed
    output = []
    for _ in range(length):
        x = pow(g, x, p)
        output.append(x % 2)
    return output

print(prg_dlog(3, 5, 23, 10))