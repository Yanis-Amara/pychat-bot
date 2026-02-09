import os
import string
import math
from collections import defaultdict
from collections import Counter

def liste_de_fichier(directory):
    """
        Retourne une liste de noms de fichiers dans un répertoire donné.
    Args:
        directory (str): Le chemin du répertoire.
    Returns:
        list: Une liste de noms de fichiers.
    """

    files_names = []

    for filename in os.listdir(directory):
        files_names.append(filename)

    return files_names


def extraire_noms_de_famille(files_names):
    """
        Extrait les noms de famille d'une liste de noms de fichiers.
    Args:
        files_names (list): Une liste de noms de fichiers.
    Returns:
        list: Une liste des noms de famille uniques extraits des noms de fichiers.
    """

    noms_de_famille_inter = []
    noms_de_famille = []

    for nom in files_names:
        # Trouver l'indice du premier caractère après le '_' dans le nom de fichier
        debut_nom_famille = nom.index('_') + 1

        # Trouver l'indice du premier caractère avant l'extension '.txt' dans le nom de fichier
        fin_nom_famille = nom.index('.txt')

        # Extraire le nom de famille en utilisant les indices trouvés
        nom_famille = nom[debut_nom_famille:fin_nom_famille].rstrip('0123456789')

        noms_de_famille_inter.append(nom_famille)

    for element in noms_de_famille_inter:
        # Vérifier si le nom de famille n'est pas déjà dans la liste finale
        if element not in noms_de_famille:
            noms_de_famille.append(element)

    return noms_de_famille


def clean_text(text):
    """
        Fonction pour nettoyer le texte en supprimant la ponctuation,
        en convertissant en minuscules et en remplaçant
        les tirets et les apostrophes par des espaces.

        :param text: Le texte à nettoyer
        :return: Le texte nettoyé
    """

    text = text.lower()
    # Supprime la ponctuation et remplace les tirets et les apostrophes par des espaces
    for punctuation in string.punctuation:
        if text == "-":
            text = text.replace("-", '')
        elif punctuation not in ["'", '-']:
            text = text.replace(punctuation, '')
        else:
            text = text.replace("'", ' ')
            text = text.replace('-', ' ')

    return text


def TF(chaine):
    """"
        Compte le nombre d'occurrences de chaque mot dans une chaîne.
    Args:
        chaine (str): La chaîne à analyser.
    Returns:
        dict: Un dictionnaire contenant les mots comme clés et leur nombre d'occurrences comme valeurs.
    """

    mots = chaine.split()
    occurrences = {}
    for mot in mots:
        # Vérifier si le mot est déjà présent dans le dictionnaire des occurrences
        if mot in occurrences:
            occurrences[mot] += 1
        else:
            occurrences[mot] = 1

    return occurrences



def IDF(directory):
    """
        Calcule les scores IDF pour chaque mot dans les fichiers d'un répertoire.
    Args:
        directory (str): Le chemin du répertoire contenant les fichiers.
    Returns:
        dict: Un dictionnaire contenant les scores IDF pour chaque mot.
    """

    idf_scores = defaultdict(float)

    total_documents = 0

    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r') as file:
            content = file.read()

        words = content.split()

        # Parcours des mots uniques dans le contenu
        for word in set(words):
            # Incrémentation du score IDF pour le mot
            idf_scores[word] += 1

        # Incrémentation du nombre total de documents
        total_documents += 1

    # Calcul des scores IDF pour chaque mot
    for word in idf_scores:
        # Utilisation de la formule mathématique pour le calcul du score IDF
        idf_scores[word] = math.log10(total_documents / idf_scores[word])

    return dict(idf_scores)


def TFIDF(liste_TF, dictionnaire_IDF):
    """
        Calculer la matrice TF-IDF pour une liste de documents.
    Args:
        liste_TF (list): Une liste de dictionnaires représentant les termes et leur fréquence pour chaque document.
        dictionnaire_IDF (dict): Un dictionnaire représentant les termes et leur inverse document frequency (IDF).
    Returns:
        list: Une matrice représentant le TF-IDF de chaque terme dans chaque document.
    """

    matrice_tfidf = []

    for document in liste_TF:
        document_tfidf = {}
        for terme in dictionnaire_IDF.keys():
            # Calcul du TF-IDF pour chaque terme dans le document
            if terme in document.keys():
                document_tfidf[terme] = document[terme] * dictionnaire_IDF[terme]
            else:
                # Si le terme n'est pas dans le document, le TF-IDF est à 0.0
                document_tfidf[terme] = 0.0
        matrice_tfidf.append(document_tfidf)

    return matrice_tfidf


def mots_non_importants(matrice):
    """
        Obtenir les mots non importants à partir d'une matrice de dictionnaires.
    Args:
        matrice (list): Une matrice de dictionnaires contenant des mots et leurs scores.
    Returns:
        list: Une liste des mots non importants ayant un score de 0.0 dans chaque dictionnaire.
    """


    mots_score_zero = []

    for dictionnaire in matrice:
        for mot, score in dictionnaire.items():
            # Vérifier si le score est égal à 0.0,si oui il ajoute le mot a la liste
            if score == 0.0:
                mots_score_zero.append(mot)

    occurrences_mots = Counter(mots_score_zero)

    # Sélectionner les mots qui apparaissent 8 fois pour garder seulement qui  ont un score de 0.0 dans chaque dictionnaire
    mots_non_importants = [mot for mot, occurrence in occurrences_mots.items() if occurrence == 8]

    return mots_non_importants


def mots_plus_importants(matrice):
    """
    Cette fonction prend une matrice de dictionnaires en entrée et retourne les trois mots ayant les scores les plus élevés.

    """
    mots_scores = {}

    for dictionnaire in matrice:
        for mot, score in dictionnaire.items():
            # Vérifier si le mot existe dans le dictionnaire
            if mot not in mots_scores:
                mots_scores[mot] = score
            else:
                # Si le mot existe déjà, vérifier s'il a un score plus élevé
                if score > mots_scores[mot]:
                    mots_scores[mot] = score

    # Trier les mots en fonction de leurs scores et obtenir les trois premiers
    mots_plus_eleves = sorted(mots_scores, key=mots_scores.get, reverse=True)[:3] # On peut faire varier le nombres de mots renvoyer ici

    return mots_plus_eleves


def mots_repetes_chirac(dictionnaire):
    """
    Cette fonction renvoie les cinq mots les plus repetes dans un dictionnaire.

    """
    # Trie le dictionnaire par valeur dans l'ordre decroissant
    tri_valeurs = sorted(dictionnaire, key=dictionnaire.get, reverse=True)

    # Recupere les cinq premiers mots triés
    mots_repetes = tri_valeurs[:5] # On peut faire varier le nombres de mots renvoyer ici

    return mots_repetes


def filtrer_mots_pas_importants(TFchirac, mots_pas_importants):
    """
    Filtrer les mots pas importants du discours de Chirac.

    """
    # le code itère à travers chaque paire clé-valeur dans le dictionnaire "discours_chirac".
    # Si la clé (le mot) n'est pas présente dans la liste "mots_pas_importants",
    # alors cette paire clé-valeur est ajoutée au nouveau dictionnaire "discours_chirac_sans_mots_pas_importants"
    discours_chirac_sans_mots_pas_importants = {mot: valeur for mot, valeur in TFchirac.items() if mot not in mots_pas_importants}

    return discours_chirac_sans_mots_pas_importants


def trouver_president_mot(liste_presidents, mot):
    """
    Trouve les noms des présidents qui précèdent un mot dans une liste.

    """
    presidents = []

    for i in range(1, len(liste_presidents)):
        if mot in liste_presidents[i]:
            # Ajout du nom du président précédent à la liste des présidents
            presidents.append(liste_presidents[i-1])

    return presidents


def mot_frequence_president(liste, mot):
    """
    Renvoie le nom du président ayant la fréquence la plus élevée d'un mot donné dans son dictionnaire.

    """
    # Obtenir le compte de fréquence du mot pour chaque président
    mots_par_president = [dico.get(mot, 0) for dico in  liste[1::2]]

    # Trouver le compte de fréquence maximum et son index
    max_occurrences = max(mots_par_president)
    index_max = mots_par_president.index(max_occurrences)

    # Renvoyer le nom du président ayant la fréquence la plus élevée
    return liste[index_max * 2]


def tokenisation_question(question):
    """
    Tokenise une question en mots individuels.

    """
    phrase = []
    mot = ''

    for lettre in question:
        # Si le caractère est en majuscule
        if lettre in string.ascii_uppercase:
            lettre = lettre.lower()
            mot += lettre

        # Si le caractère est en minuscule
        elif lettre in string.ascii_lowercase:
            mot += lettre

        # Si le caractère est un espace ou une ponctuation
        elif lettre == " " or lettre in string.punctuation:
            phrase.append(mot)
            mot = ''

    return phrase


def question_corpus(question):
    """
    Extrait une liste de mots pertinents à partir d'une question en la comparant à un corpus.

    """
    directory = os.path.dirname(os.path.abspath(__file__))

    cleaned_dir = os.path.join(directory, 'cleaned')

    IDFdic = IDF(cleaned_dir)

    phrase = tokenisation_question(question)

    # Filtrer les mots qui ne sont pas présents dans le dictionnaire IDF
    liste_mot = [mot for mot in phrase if mot in IDFdic]

    return liste_mot


def TF_question(question):
    """
    Calcule la fréquence des termes d'une question donnée.

    """
    phrase = question_corpus(question)

    chaine = " ".join(phrase)

    return TF(chaine)


#Comme IDF du corpus = IDF question
# Supposons que vous ayez déjà les fonctions suivantes : question_corpus() et IDF()

def vecteur_TF_IDF(question):
    """
        Calcule les scores TF-IDF pour chaque mot dans la question donnée.
        Args:
            question (str): La question pour laquelle on veut calculer les scores TF-IDF.
        Returns:
            dict: Un dictionnaire contenant les mots de la question comme clés et les scores TF-IDF correspondants comme valeurs.
    """
    directory = os.path.dirname(os.path.abspath(__file__))
    cleaned_dir = os.path.join(directory, 'cleaned')
    IDFdic = IDF(cleaned_dir)
    liste_mot_question = question_corpus(question)

    tf_idf_scores = {}  # Dictionnaire pour stocker les scores TF-IDF

    for mot in liste_mot_question:
        if mot in IDFdic:  # Vérifie si le mot est présent dans le dictionnaire IDF
            score_tf = liste_mot_question.count(mot)  # Calcul du score TF pour le mot
            score_idf = IDFdic[mot]  # Récupération du score IDF pour le mot

            tf_idf_scores[mot] = score_tf * score_idf  # Calcul du score TF-IDF et stockage dans le dictionnaire

    return tf_idf_scores


def produit_scalaire(a, b):
    """
        Calcule le produit scalaire entre deux vecteurs.
        Args:
            a (list): Le premier vecteur.
            b (list): Le deuxième vecteur.
        Returns:
            int: Le produit scalaire des deux vecteurs.
    """
    scalaire = 0
    for i in range(len(b)):
        scalaire += (a[i] * b[i])
    return scalaire


def norme_vecteur(a):
    """
        Calcule la norme du vecteur a.
        Args:
            a (list): Le vecteur a.
        Returns:
            float: La norme du vecteur a.
    """
    norme = 0
    for i in range(len(a)):
        norme += (a[i]) ** 2
    return math.sqrt(norme)


def similarite(a,b):
    """
        Calcule la similarité entre deux vecteurs a et b.

        Args:
            a (list): Le premier vecteur.
            b (list): Le deuxième vecteur.

        Returns:
            float: La similarité entre les deux vecteurs.
    """
    return produit_scalaire(a, b) / (norme_vecteur(a) * norme_vecteur(a))


def document_pertinent(matrice_finale, vecteur_mots_question):
    """
        Trouve le discours le plus pertinent en comparant les similarités
        entre le vecteur TF-IDF donné et les vecteurs de la matrice finale.
        Args:
            matrice_final (list): La matrice finale contenant les vecteurs TF-IDF
                                  et les discours associés.
            vecteur_TF_IDF (list): Le vecteur TF-IDF à comparer.
        Returns:
            str: Le discours le plus pertinent.
    """
    similariteMax = 0
    discoursPertinent = ""
    valeurs_TFIDF = [valeur for valeur in vecteur_mots_question.values() if isinstance(valeur, float)]
    for listescore in range(1, len(matrice_finale), 2):
        similarite_doc = similarite(matrice_finale[listescore], valeurs_TFIDF)
        if similarite_doc > similariteMax:
            similariteMax = similarite_doc
            discoursPertinent = matrice_finale[listescore - 1]
    return discoursPertinent


def creer_matrice(matrice_dicos):
    """
        Crée une matrice numérique à partir d'une liste de dictionnaires.
        Args:
            matrice_dicos (list): Une liste de dictionnaires contenant des mots et leurs valeurs numériques.
        Returns:
            list: Une matrice numérique représentant les valeurs des mots dans chaque dictionnaire.
    """
    mots_uniques = set()
    for dico in matrice_dicos:
        mots_uniques.update(dico.keys())

    mots_uniques_tries = sorted(mots_uniques)

    # Création d'un dictionnaire pour mapper chaque mot à un indice unique
    index_mot = {mot: i for i, mot in enumerate(mots_uniques_tries)}

    # Initialisation de la matrice avec des listes vides
    nb_documents = len(matrice_dicos)
    nb_mots = len(mots_uniques_tries)
    nouvelle_matrice = []
    for _ in range(nb_documents):
        nouvelle_matrice.append([0] * nb_mots)

    # Remplissage de la matrice avec les valeurs numériques
    for i, dico in enumerate(matrice_dicos):
        for mot, valeur in dico.items():
            j = index_mot[mot]
            nouvelle_matrice[i][j] = valeur

    return nouvelle_matrice


def TF_IDF_plus_eleve(question):
    """
        Trouve le mot avec le score TF-IDF maximal dans un vecteur donné.

        Args:
            vecteur_TF_IDF (list): Le vecteur contenant les mots et leurs scores TF-IDF.

        Returns:
            str: Le mot avec le score TF-IDF maximal.
    """
    dico_TFIDF_question = vecteur_TF_IDF(question)
    if not dico_TFIDF_question:  # Vérifie si le dictionnaire est vide
        return None

    mot_max = max(dico_TFIDF_question, key=dico_TFIDF_question.get)
    return mot_max
