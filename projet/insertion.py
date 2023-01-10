def run_insertion(tirage):
    for i in range(tirage.shape[1]):
        for j in range(1, tirage.shape[0]):
            x = tirage.iloc[j, i]
            k = j - 1

            while k > -1 and tirage.iloc[k, i] > x:
                tirage.iloc[k + 1, i] = tirage.iloc[k, i]
                k -= 1
            
            tirage.iloc[k + 1, i] = x

    return tirage
    