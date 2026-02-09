from functions import *
import os

# initialisation des chemins
directory = os.path.dirname(os.path.abspath(__file__))
speeches_dir = os.path.join(directory, 'speeches')
cleaned_dir = os.path.join(directory, 'cleaned')


"""
    Cette premiere partie récupere les noms et prénoms des présidents.

    """
# récupere les noms des fichers.txt
files_names = liste_de_fichier(speeches_dir)

# extrait juste les noms
noms_de_famille = extraire_noms_de_famille(files_names)
#trie les noms de famille
sorted(noms_de_famille)

# créer un dico des noms
dico_noms_de_famille = {cle: valeur for cle, valeur in zip(range(1, 7), noms_de_famille)}

# créer dico des prénoms
dico_prenoms = {1: 'Jacques', 2: 'François', 3: 'Nicolas', 4: 'François', 5: 'Emmanuel', 6: 'Valéry'}

# assemble les deux dico pour avec prenom et nom
dico_noms_prenoms = {}
for cle in set(dico_noms_de_famille.keys()) | set(dico_prenoms.keys()):
    valeur1 = dico_noms_de_famille.get(cle, 0)
    valeur2 = dico_prenoms.get(cle, 0)
    dico_noms_prenoms[cle] = valeur2 + ' ' + valeur1

noms_prenoms = list(dico_noms_prenoms.values())

"""
    Cette seconde partie sert au nettoyage des discours.

    """
# Parcours les fichiers du dossier speeches
for filename in os.listdir(speeches_dir):
    # Ouverture du fichier
    file_path = os.path.join(speeches_dir, filename)

    # Si le fichier est un fichier texte
    if os.path.isfile(file_path) and filename.endswith('.txt'):
        # Lire le contenu du fichier
        with open(file_path, 'r') as file:
            # Lire le contenu du fichier et le stocker dans une variable
            content = file.read()

            # Appliquer la fonction clean_text sur le contenu
            cleaned_content = clean_text(content)

            # Ecrire le contenu nettoye dans un nouveau fichier
            cleaned_file_path = os.path.join(cleaned_dir, filename)

            # Ecrire le contenu nettoye dans le nouveau fichier
            with open(cleaned_file_path, 'w', encoding='utf-8') as cleaned_file:
                # Ecrire le contenu nettoye dans le nouveau fichier
                cleaned_file.write(cleaned_content.replace('\n', ' '))

"""
    Cette troisième partie sert à la creation de la matrice TF-IDF.

    """
# Initialisation de la matrice TF
TFlist = []
# Parcours des fichiers du dossier cleaned
for filename in os.listdir(cleaned_dir):
    # Ouverture du fichier
    file_path = os.path.join(cleaned_dir, filename)

    # Si le fichier est un fichier texte
    if os.path.isfile(file_path) and filename.endswith('.txt'):
        # Lire le contenu du fichier
        with open(file_path, 'r') as file:
            # Stocker dans une variable le contenu du fichier
            content = file.read()

            # Appliquer la fonction TF et l'ajouter à la liste TFlist
            TFlist.append(TF(content))


# Creation du dictionnaire IDF
IDFdic = IDF(cleaned_dir)

# Creation de la matrice TF-IDF grace a la fonction TFIDF
matrice = TFIDF(TFlist, IDFdic)

# Affichage de la matrice TF-IDF
'''for i in range (8):
    print(files_names[i])
    print(matrice[i])
print("-------------------------------------------------------------")'''


"""
    Cette quatrième partie sert à la creation du TF de chaque président et non de chaque fichier.

    """
# Recupere le TF des discours de Chirac additionné
count = 0
chirac_str = ''
# Parcours des fichiers du dossier cleaned
for filename in os.listdir(cleaned_dir):
    # Ouverture du fichier
    file_path = os.path.join(cleaned_dir, filename)

    # Si le fichier est un fichier texte et le nom du fichier se termine par Chirac1.txt ou Chirac2.txt
    if os.path.isfile(file_path) and filename.endswith('Chirac1.txt') or filename.endswith('Chirac2.txt'):
        # Lire le contenu du fichier
        with open(file_path, 'r') as file:
            # Stocker dans une variable le contenu du fichier
            content = file.read()

            # Ajouter le contenu du fichier à la chaine chirac_str
            chirac_str += content

# Appliquer la fonction TF sur la chaine chirac_str
TFchirac = TF(chirac_str)
# Stock la liste des mots non importants
mots_pas_importants = mots_non_importants(matrice)
# Supprime les mots non importants du TF des discours de Chirac
discours_chirac_sans_mots_pas_importants = filtrer_mots_pas_importants(TFchirac, mots_pas_importants)


# Recupere le TF des discours de Mitterrand additionné
count = 0
mitterrand_str = ''
# Parcours des fichiers du dossier cleaned
for filename in os.listdir(cleaned_dir):
    # Ouverture du fichier
    file_path = os.path.join(cleaned_dir, filename)

    # Si le fichier est un fichier texte et le nom du fichier se termine par Mitterrand1.txt ou Mitterrand2.txt
    if os.path.isfile(file_path) and filename.endswith('Mitterrand1.txt') or filename.endswith('Mitterrand2.txt'):
        # Lire le contenu du fichier
        with open(file_path, 'r') as file:
            # Stocker dans une variable le contenu du fichier
            content = file.read()

            # Ajouter le contenu du fichier à la chaine chirac_str
            mitterrand_str += content

# Appliquer la fonction TF sur la chaine mitterrand_str
TFmitterrand = TF(mitterrand_str)
# Initialisation de la liste TFpresident
TFpresident = []
# Fusion de tout les TF pour recuperer les TF par président et non discours
TFpresident.append(noms_prenoms[0])
TFpresident.append(TFchirac)
TFpresident.append(noms_prenoms[1])
TFpresident.append(TFmitterrand)
TFpresident.append(noms_prenoms[2])
TFpresident.append(TFlist[3])
TFpresident.append(noms_prenoms[3])
TFpresident.append(TFlist[5])
TFpresident.append(noms_prenoms[4])
TFpresident.append(TFlist[6])
TFpresident.append(noms_prenoms[5])
TFpresident.append(TFlist[7])



matrice_finale = []
for i in range (8):
    matrice_finale.append(files_names[i])
    matrice_finale.append(creer_matrice(matrice)[i])





# Menu :
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(".______   ____    ____   ______  __    __       ___      .___________.   .______     ______   .___________.")
print("|   _  \  \   \  /   /  /      ||  |  |  |     /   \     |           |   |   _  \   /  __  \  |           |")
print("|  |_)  |  \   \/   /  |  ,----'|  |__|  |    /  ^  \    `---|  |----`   |  |_)  | |  |  |  | `---|  |----`")
print("|   ___/    \_    _/   |  |     |   __   |   /  /_\  \       |  |        |   _  <  |  |  |  |     |  |     ")
print("|  |          |  |     |  `----.|  |  |  |  /  _____  \      |  |        |  |_)  | |  `--'  |     |  |     ")
print("| _|          |__|      \______||__|  |__| /__/     \__\     |__|        |______/   \______/      |__|     ")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
dossier = input("Saisie le nom du dossier à analyser : ")
while dossier not in os.listdir("./"):
    dossier = input("Saisie le nom du dossier à analyser : ")
print('\n')
print("Choisis une fonction parmi celles-ci : "'\n'
    '\n'
    "-1 : Affiche la liste des mots les moins importants"'\n'
    "-2 : Affiche les mots les plus importants"'\n'
    "-3 : Affiche les mots les plus répétés par Chirac"'\n'
    "-4 : Indiquer les noms des présidents qui ont parlé d'un mot en particulier et celui qui l’a répété le plus de fois"'\n'
    "-5 : Indiquer le  président qui a parler du climat et/ou de l’écologie"'\n'
    "-6 : Accéder au Pychat Bot"'\n')

fonction = int(input("Saisie la fonction à utiliser : "))

while fonction < 1 or fonction > 6:
    fonction = int(input("Saisie la fonction à utiliser :"))

print('\n')
if fonction == 1:
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Voici la liste des mots les moins importants :", mots_non_importants(matrice))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

elif fonction == 2:
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Voici les 3 mots les plus importants :", mots_plus_importants(matrice))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

elif fonction == 3:
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Voici les 5 mots les plus répétés par Chirac :", mots_repetes_chirac(discours_chirac_sans_mots_pas_importants))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

elif fonction == 4:
    word = input("Saisir le mot à analyser : ")
    president_qui_a_dit_le_mot = (trouver_president_mot(TFpresident, word))
    president_qui_a_dit_le_plus = mot_frequence_president(TFpresident, word)
    if president_qui_a_dit_le_mot == []:
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Aucun président n'a dit le mot «", word, "»")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    else:
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Les présidents qui ont dit le mot «", word, "» sont : ", president_qui_a_dit_le_mot)
        print("Le président qui a dit le plus le mot «", word, "» est :", president_qui_a_dit_le_plus)
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

elif fonction == 5:
    word = input("Saisir le mot à analyser : ")
    president_qui_a_dit_le_mot = (trouver_president_mot(TFpresident, word))
    if president_qui_a_dit_le_mot == []:
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Aucun président n'a dit le mot «", word, "»")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    else:
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Le président qui a dit le mot «", word, "» est : ", president_qui_a_dit_le_mot)
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

elif fonction == 6 :
    print("Quelle question voulez-vous poser ?"'\n')
    question = str(input("Saisir la question : "))
    vecteur_mots_question = vecteur_TF_IDF(question)
    print('\n')
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Les documents les plus pertinents sont : ", document_pertinent(matrice_finale, vecteur_mots_question))
    print("Le mot le plus pertinent est : ", TF_IDF_plus_eleve(question))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print('\n'
    "Voulez-vous utiliser une autre fonction ?"'\n'
    '\n'
    "-1 : Oui"'\n'
    "-2 : Non"'\n')

reponse = int(input("Saisir une réponse : "))

while reponse ==  1:
    print('\n')
    print("Choisis une fonction parmi celles-ci : "'\n'
          '\n'
          "-1 : Affiche la liste des mots les moins importants"'\n'
          "-2 : Affiche le/les mots le/les plus importants"'\n'
          "-3 : Affiche les mots les plus répétés par Chirac"'\n'
          "-4 : Indiquer les noms des présidents qui ont parlé d'un mot en particulier et celui qui l’a répété le plus de fois"'\n'
          "-5 : Indiquer le président qui a parler du climat et/ou de l’écologie"'\n'
          "-6 : Accéder au Pychat Bot"'\n')

    fonction = int(input("Saisie la fonction à utiliser : "))

    onction = int(input("Saisie la fonction à utiliser : "))

    while fonction < 1 or fonction > 6:
        fonction = int(input("Saisie la fonction à utiliser :"))

    print('\n')
    if fonction == 1:
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Voici la liste des mots les moins importants :", mots_non_importants(matrice))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    elif fonction == 2:
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Voici les 3 mots les plus importants :", mots_plus_importants(matrice))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    elif fonction == 3:
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Voici les 5 mots les plus répétés par Chirac :",mots_repetes_chirac(discours_chirac_sans_mots_pas_importants))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    elif fonction == 4:
        word = input("Saisir le mot à analyser : ")
        president_qui_a_dit_le_mot = (trouver_president_mot(TFpresident, word))
        president_qui_a_dit_le_plus = mot_frequence_president(TFpresident, word)
        if president_qui_a_dit_le_mot == []:
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Aucun président n'a dit le mot «", word, "»")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        else:
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Les présidents qui ont dit le mot «", word, "» sont : ", president_qui_a_dit_le_mot)
            print("Le président qui a dit le plus le mot «", word, "» est :", president_qui_a_dit_le_plus)
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    elif fonction == 5:
        word = input("Saisir le mot à analyser : ")
        president_qui_a_dit_le_mot = (trouver_president_mot(TFpresident, word))
        if president_qui_a_dit_le_mot == []:
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Aucun président n'a dit le mot «", word, "»")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        else:
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Le président qui a dit le mot «", word, "» est : ", president_qui_a_dit_le_mot)
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    elif fonction == 6:
        print("Quelle question voulez-vous poser ?"'\n')
        question = str(input("Saisir la question : "))
        vecteur_mots_question = vecteur_TF_IDF(question)
        print('\n')
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Les documents les plus pertinents sont : ", document_pertinent(matrice_finale, vecteur_mots_question))
        print("Le mot le plus pertinent est : ", TF_IDF_plus_eleve(question))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print('\n'
          "Voulez-vous utiliser une autre fonction ?"'\n'
          '\n'
          "-1 : Oui"'\n'
          "-2 : Non"'\n')


if reponse == 2:
    print('\n')
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Merci d'avoir utilisé Pychat Bot !")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
