def solution(n):
    n = bin(int(n))[2:]
    resto = 0
    cont = 0
    for i in range(len(n) - 1, 0, -1):
        if n[i] == '0' and resto == 0:
            cont = cont + 1
        elif n[i] == '0' and resto == 1:
            cont = cont + 2
            if i == 1 or n[i - 1] == '0':
                resto = 0
        elif n[i] == '1' and resto == 0:
            cont = cont + 2
            if i > 1 and n[i - 1] == '1':
                resto = 1
        else:
            cont += 1
    return cont + resto
