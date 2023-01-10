def run_insertion(tirage):
    for i in range(tirage.shape[0]):
        for j in range(2, tirage.shape[1]):
            x = tirage.iloc[i, j]
            k = j - 1

            while k > 0 and tirage.iloc[i, k] > x:
                tirage.iloc[i, k + 1] = tirage.iloc[i, k]
                k -= 1
            
            tirage.iloc[i, k + 1] = x

    return tirage
    