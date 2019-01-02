from math import *
import random
#import scipy # comment faire pour les importer sans que cela fasse une erreur ?
# from operator import itemgetter # fonction permettant de trier à partir d'une colonne au choix
# utiliser la commande :
# listTriée = sorted(listFrNum, key=itemgetter(1))

nbeFrTemp = ""
nbeNumTemp = 0
dicoFrNum = {} # dictionnaire Français vers Numérique
listFrNum = [] # liste à 2 dimensions
listFrNumTrans = []

fichierDico = open("Fichier_Dico_FrNum.txt","r") # lecture
listDico = fichierDico.readlines() # liste à 1 dimension


#---- Pour bricoler des chaînes pour voir
# testChaine = "\nBonjour\n"
# print(testChaine)
# print(testChaine.strip())

#---- Découpe le dictionnaire pour alimenter un tableau
#  qui sera ensuite rangé puis réenregistré(fonction à faire)
for i in range(0,len(listDico)):
    listDico[i] = listDico[i].strip() # retire les retours chariot
    listFrNum.append(listDico[i].split()) # découpe les lignes en mots et écrit toutes les entrées

listFrNum = sorted(listFrNum) # trie les entrées suivant la première colonne et remplace
listFrNumTrans = [[row[i] for row in listFrNum] for i in range(len(listFrNum[0]))] # transpose

#  fonction qui change un tableau [x][y] en [y][x]
#for raw in listDico[0]:


print(listFrNum)


#print(listDico)
#print(listFrNum)

# while True:
#     nbeFrTemp = input("Entrez un nombre en toutes lettres (\"S\" pour sortir) : ") # gérer les erreurs de saisie
#     if nbeFrTemp == "S":
#         print("--> Merci quand même. Au-revoir.")
#         break
#     else:
#         nbeNumTemp = int(input("Maintenant, entrez la traduction de \"" + nbeFrTemp + "\" en numérique : "))  # gérer les erreurs de saisie
#         dicoFrNum[nbeFrTemp] = nbeNumTemp
#         print("--> Merci pour la contribution")

fichierDico.close()