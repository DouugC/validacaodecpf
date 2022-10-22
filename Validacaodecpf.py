CPF = input('Digite seu CPF com dígito: ')

CpfSemDigito = CPF[:-2]
ContagemDecrescente = 10
total = 0

for indice in range(19):
    if indice > 8:
        indice -= 9
    total += int(CpfSemDigito[indice]) * ContagemDecrescente

    ContagemDecrescente -= 1
    if ContagemDecrescente < 2:
        ContagemDecrescente = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        CpfSemDigito += str(d)

if CPF == CpfSemDigito:
    print('CPF Valido')
else:
    print('CPF Invalido')