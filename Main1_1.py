from math import *
import random
# import scipy # comment faire pour les importer sans que cela fasse une erreur ?
# from operator import itemgetter # fonction permettant de trier à partir d'une colonne au choix
# utiliser la commande :
# listTriée = sorted(listFrNum, key=itemgetter(1))

nbeFrTemp = "bonjour"
nbeNumTemp = 30
dicoFrNum = {} # dictionnaire Français vers Numérique
listFrNum = [] # liste à 2 dimensions
listFrNumTrans = []

fichierDico = open("Fichier_Dico_FrNum.txt","r+") # lecture
listDico = fichierDico.readlines() # liste à 1 dimension
listDico.extend([nbeFrTemp + " " + str(nbeNumTemp) + "\n"])

print(listDico)

#fichierDico.write("bonjour à tous")


fichierDico = open("Fichier_Dico_FrNum.txt","a") # lecture
fichierDico.write(nbeFrTemp + " " + str(nbeNumTemp) + "\n")
listDico = fichierDico.readlines() # liste à 1 dimension

print(listDico)

# #---- Découpe le dictionnaire pour alimenter un tableau
# #  qui sera ensuite rangé puis réenregistré(fonction à faire)
# for i in range(0,len(listDico)):
#     listDico[i] = listDico[i].strip() # retire les retours chariot
#     listFrNum.append(listDico[i].split()) # découpe les lignes en mots et écrit toutes les entrées dans listFrNum
#
# #---- Interroge l'utilisateur
# while True:
#     nbeFrTemp = input("Entrez un nombre en toutes lettres (\"S\" pour sortir) : ") # gérer les erreurs de saisie
#     if nbeFrTemp == "S":
#         print("--> Merci quand même. Au-revoir.")
#         break
#     else:
#         nbeNumTemp = int(input("Maintenant, entrez la traduction de \"" + nbeFrTemp + "\" en numérique : "))  # gérer les erreurs de saisie
#         dicoFrNum[nbeFrTemp] = nbeNumTemp
#         listDico.extend(nbeFrTemp + " " + str(nbeNumTemp) + "\n")  # écrit dans le fichier : ajoute la nouvelle entrée + définition
#         print("--> Merci pour la contribution")
#
# #---- Découpe le dictionnaire pour alimenter un tableau
# #  qui sera ensuite rangé puis réenregistré(fonction à faire)
# for i in range(0,len(listDico)):
#     listDico[i] = listDico[i].strip() # retire les retours chariot
#     listFrNum.append(listDico[i].split()) # découpe les lignes en mots et écrit toutes les entrées dans listFrNum


listFrNum = sorted(listFrNum) # trie les entrées suivant la première colonne et remplace
#listFrNumTrans = [[row[i] for row in listFrNum] for i in range(len(listFrNum[0]))] # transpose





fichierDico.close()