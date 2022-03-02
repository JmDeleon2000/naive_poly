
#input parecido al de Horner
input = [0, 2, 0, 5]


def naive_poly(coef, x):
    total = 0
    for i, a in enumerate(coef):
        mul = a
        for j in range(i):
            mul *= x
        total += mul
    return total

print(naive_poly(input, 4))

print(naive_poly(input, 5))