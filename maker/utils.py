def aggregate(lista, key = lambda x:x[0]):
    resu = {}
    for ll in lista:
        k = key(ll)
        resu[k] = resu.get(k, []) + [ll]
    return resu

def join(listaA, listaB, keyA = lambda x: x[0], keyB = lambda x:x[0]):
    resu = []
    beta = aggregate(listaB, keyB)
    for ll in listaA:
        keyAlpha = keyA(ll)
        resu.append([ll, beta[keyAlpha]])
    return resu
