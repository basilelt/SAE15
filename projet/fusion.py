import pandas

def fusion(L, M):
    N = []

    while L != [] and M != []:
        if L[0] < M[0]:
            N.append(L[0])
            L.pop(0)
        else:
            N.append(M[0])
            M.pop(0)

    return N + L + M

def tri_fusion(L):
    n = len(L)
    n_2 = n // 2
    if n < 2:
        return L
    
    G = L[0:n_2]
    D = L[n_2:n]

    G = tri_fusion(G)
    D = tri_fusion(D)

    F = fusion (G, D)

    return F

def run_fusion(tirage):
    for i in range(tirage.shape[1]):
        to_list = tirage.iloc[:, i].tolist()
        to_list = tri_fusion(to_list)
        tirage.iloc[:,i] = pandas.Series(to_list)

    return tirage
    