import numpy
from loto import run_loto
from stats import run_stats
from functions import test_trichoix, test_bool
from cocktail import run_cocktail
from insertion import run_insertion
from fusion import run_fusion
from dicho import run_dicho
from binary import run_save_b, run_read_b
from humain import run_save_h, run_read_h
from histogram import run_hist

lst = numpy.array(list(i for i in range(1, 46)))

saved = test_bool(input("Voulez-vous charger des données précedemment générées ? (0 : non, 1 : oui) : "))
if saved:
    type_save = test_bool(input("\nDe quel type de sauvegarde s'agit-il ? (0 : humaine, 1 : binaire) : "))
    if type_save:
        tirage = run_read_b()
        
    else:
        tirage = run_read_h()
   
    saved_tri = test_bool(input("Ces données sont-elles triées ? (0 : non, 1 : oui) : "))
    if saved_tri:
        search = test_bool(input("\nVoulez-vous chercher si une valeur est présente dans le(s) tirage(s) ? (0 : non, 1 : oui) : "))
        if search:
            tirage_search = run_dicho(tirage, search, lst)
            print("\nLe(s) tirage(s) comportant le nombre choisi sont :\n", tirage_search)
        
        search = False
        lst_occurence = run_dicho(tirage, search, lst)
        run_hist(lst_occurence)

    else:
        tri = test_bool(input("\nVoulez-vous trier ce(s) tirage(s) ? (0 : non, 1 : oui) : "))
        if tri:
            tri_choix = test_trichoix(input("Quel tri voulez-vous utiliser ? (cocktail : 1, insertion : 2, fusion : 3) : "))
            if tri_choix == 1:
                tirage = run_cocktail(tirage)

            elif tri_choix == 2:
                tirage = run_insertion(tirage)

            else:
                tirage = run_fusion(tirage)

            print("\nVoici le(s) tirage(s) trié(s) : \n", tirage)

            save = test_bool(input("\nVoulez-vous sauvegarder ce(s) tirage(s) ? (0 : non, 1 : oui) : "))
            if save:
                type_save = test_bool(input("\nDe quel type de sauvegarde s'agit-il ? (0 : humaine, 1 : binaire) : "))
                if type_save:
                    run_save_b(tirage, True)
                    
                else:
                    run_save_h(tirage, True)

            search = test_bool(input("\nVoulez-vous chercher si une valeur est présente dans le(s) tirage(s) ? (0 : non, 1 : oui) : "))
            if search:
                tirage_search = run_dicho(tirage, search, lst)
                print("\nLe(s) tirage(s) comportant le nombre choisi sont :\n", tirage_search)
            
            search = False
            occurence = run_dicho(tirage, search, lst)
            run_hist(lst_occurence)
    
else:
    tirage = run_loto(lst)

    run_stats(lst)

    tri = test_bool(input("\nVoulez-vous trier ce(s) tirage(s) ? (0 : non, 1 : oui) : "))
    if tri:
        tri_choix = test_trichoix(input("Quel tri voulez-vous utiliser ? (cocktail : 1, insertion : 2, fusion : 3) : "))
        if tri_choix == 1:
            tirage = run_cocktail(tirage)

        elif tri_choix == 2:
            tirage = run_insertion(tirage)

        else:
            tirage = run_fusion(tirage)

        print("\nVoici le(s) tirage(s) trié(s) : \n", tirage)

        save = test_bool(input("\nVoulez-vous sauvegarder ce(s) tirage(s) ? (0 : non, 1 : oui) : "))
        if save:
            type_save = test_bool(input("\nDe quel type de sauvegarde s'agit-il ? (0 : humaine, 1 : binaire) : "))
            if type_save:
                run_save_b(tirage, True)
                
            else:
                run_save_h(tirage, True)

        search = test_bool(input("\nVoulez-vous chercher si une valeur est présente dans le(s) tirage(s) ? (0 : non, 1 : oui) : "))
        if search:
            tirage_search = run_dicho(tirage, search, lst)
            print("\nLe(s) tirage(s) comportant le nombre choisi sont :\n", tirage_search)
        
        search = False
        lst_occurence = run_dicho(tirage, search, lst)
        run_hist(lst_occurence)
        
    else:
        save = test_bool(input("\nVoulez-vous sauvegarder ce(s) tirage(s) ? (0 : non, 1 : oui) : "))
        if save:
            type_save = test_bool(input("\nDe quel type de sauvegarde s'agit-il ? (0 : humaine, 1 : binaire) : "))
            if type_save:
                run_save_b(tirage, False)
                
            else:
                run_save_h(tirage, False)
