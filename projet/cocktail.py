def run_cocktail(tirage):
    for i in range(tirage.shape[0]):
        echange = True
        start = 1
        end = tirage.shape[1] - 2

        while echange:
            echange = False
            
            for j in range(start, end + 1):
                if tirage.iloc[i, j] > tirage.iloc[i, j + 1]:
                    (tirage.iloc[i, j], tirage.iloc[i, j + 1]) = (tirage.iloc[i, j + 1], tirage.iloc[i, j])
                    echange = True
            
            end -= 1 

            for j in range(end, start - 1, -1):
                if tirage.iloc[i, j] > tirage.iloc[i, j + 1]:
                    (tirage.iloc[i, j], tirage.iloc[i, j + 1]) = (tirage.iloc[i, j + 1], tirage.iloc[i, j])
                    echange = True
            
            start += 1
    
    return tirage