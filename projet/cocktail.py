def run_cocktail(tirage):
    for i in range(tirage.shape[1]):
        echange = True
        start = 0
        end = tirage.shape[0] - 2

        while echange:
            echange = False
            
            for j in range(start, end + 1):
                if tirage.iloc[j, i] > tirage.iloc[j + 1, i]:
                    tirage.iloc[j, i], tirage.iloc[j + 1, i] = tirage.iloc[j + 1, i], tirage.iloc[j, i]
                    echange = True
            
            end -= 1 
            
            for j in range(end, start - 1, -1):
                if tirage.iloc[j, i] > tirage.iloc[j + 1, i]:
                    tirage.iloc[j, i], tirage.iloc[j + 1, i] = tirage.iloc[j + 1, i], tirage.iloc[j, i]
                    echange = True
            
            start += 1
    
    return tirage