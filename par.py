def par (lista):
    par =[]
    for valor in lista:
        if valor % 2 == 0:
            par.append(valor)
    return (par)

mi_lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,20,15,30,60,70]

print(par(mi_lista))
