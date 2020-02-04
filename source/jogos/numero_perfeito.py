def nuemro_perfeito(n):
    soma=0
    for val in range(1,n):
        if n % val == 0:
            soma += val
            print(soma)

    if soma==n:
        return True
    else:
        return False

nuemro_perfeito(6)