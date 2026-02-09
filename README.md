<h1 align="center">My first Pychat Bot</h1>
<p align="center"><i>Le projet explore l'analyse de texte pour créer un système de réponse basé sur la fréquence des mots, fondamental pour les chatbots et l'intelligence artificielle comme ChatGPT.</i></p>
<h1>Important</h1>
Il est inscrit que le projet a été créé le 14 décembre.
Ayant rencontré un problème sur le projet en raison de commits et de pushes de fichiers non désirés, nous avons dû créer un nouveau projet, ce qui explique la date de création du 14 décembre.

<h1>Utilisation</h1>

Pour utiliser le programme, il suffit de cliquer sur la flèche verte dans le fichier 'main.py' pour lancer le menu. 
Ensuite, sélectionnez les choix désirés en lisant le menu et en inscrivant les numéros correspondants.

<h1>Fonctions</h1>
<h3>liste_de_fichier</h3>
Ce code définit une fonction appelée liste_de_fichier qui prend en entrée le chemin d'un répertoire. Elle retourne une liste de noms de fichiers dans le répertoire donné. La fonction utilise la fonction os.listdir pour obtenir une liste de tous les noms de fichiers dans le répertoire, puis ajoute chaque nom de fichier à une liste appelée files_names. Enfin, elle retourne la liste files_names.

<h3>extraire_noms_de_famille</h3>
Ce code définit une fonction appelée extraire_noms_de_famille qui prend une liste de noms de fichiers en entrée. Elle extrait le nom de famille de chaque nom de fichier et renvoie une liste des noms de famille uniques. La fonction crée tout d'abord deux listes vides, noms_de_famille_inter et noms_de_famille. Ensuite, elle itère sur chaque nom de fichier et extrait le nom de famille en trouvant l'indice du premier caractère après le '_' et l'indice du premier caractère avant l'extension '.txt'. Elle supprime les chiffres finaux du nom de famille et l'ajoute à la liste noms_de_famille_inter. Enfin, elle itère sur la liste noms_de_famille_inter et ajoute chaque nom de famille unique à la liste noms_de_famille. La liste noms_de_famille est ensuite renvoyée.

<h3>clean_text</h3>
Ce code définit une fonction appelée clean_text qui prend un texte en entrée et renvoie le texte nettoyé. La fonction convertit le texte en minuscules et supprime la ponctuation, remplaçant les tirets et les apostrophes par des espaces.

<h3>TF</h3>
Ce code définit une fonction appelée TF qui prend une chaîne de caractères en entrée. La fonction compte le nombre d'occurrences de chaque mot dans la chaîne et renvoie un dictionnaire où les mots sont les clés et le nombre d'occurrences est la valeur. Pour cela, elle divise la chaîne en mots, initialise un dictionnaire vide, puis itère sur chaque mot de la chaîne. Si un mot est déjà présent dans le dictionnaire, il augmente le compteur de 1. Si le mot n'est pas présent, il l'ajoute au dictionnaire avec un compteur de 1. Enfin, il renvoie le dictionnaire des occurrences de mots.

<h3>IDF</h3>
Ce code calcule les scores IDF (Inverse Document Frequency) pour chaque mot dans les fichiers d'un répertoire donné. Il initialise un dictionnaire pour stocker les scores IDF, compte le nombre total de documents, puis itère sur chaque fichier dans le répertoire. Pour chaque fichier, il lit le contenu, le divise en mots, et incrémente le score IDF pour chaque mot unique. Enfin, il calcule les scores IDF pour chaque mot à l'aide d'une formule mathématique et retourne le dictionnaire des scores IDF.

<h3>TFIDF</h3>
Ce code définit une fonction appelée TFIDF qui calcule la matrice TF-IDF pour une liste de documents. La fonction prend deux arguments : liste_TF, qui est une liste de dictionnaires représentant les termes et leur fréquence pour chaque document, et dictionnaire_IDF, qui est un dictionnaire représentant les termes et leur fréquence inverse dans les documents (IDF).

La fonction initialise une matrice vide appelée matrice_tfidf et itère ensuite sur chaque document dans la liste liste_TF. Pour chaque document, elle initialise un dictionnaire vide appelé document_tfidf et itère ensuite sur chaque terme dans le dictionnaire dictionnaire_IDF.

Pour chaque terme, la fonction calcule le TF-IDF en multipliant la fréquence du terme dans le document (document[terme]) par son IDF (dictionnaire_IDF[terme]). Si le terme n'est pas présent dans le document, le TF-IDF est défini à 0.0.

Enfin, la fonction ajoute le dictionnaire document_tfidf à la matrice matrice_tfidf et retourne la matrice résultante.

<h3>mots_non_importants</h3>
Ce code définit une fonction appelée mots_non_importants qui prend une matrice de dictionnaires en entrée. Il itère sur chaque dictionnaire dans la matrice, et pour chaque mot et score dans le dictionnaire, il vérifie si le score est égal à 0.0. Si le score est 0.0, le mot est ajouté à une liste appelée mots_score_zero. La fonction compte ensuite les occurrences de chaque mot dans la liste mots_score_zero en utilisant la classe Counter. Enfin, elle sélectionne les mots qui apparaissent 8 fois dans la liste et qui ont un score de 0.0 dans chaque dictionnaire, et les renvoie sous forme de liste appelée mots_non_importants.

<h3>mots_plus_importants</h3>
Ce code définit une fonction appelée mots_plus_importants qui prend une matrice de dictionnaires en entrée et renvoie les trois mots ayant les scores les plus élevés.

La fonction crée un dictionnaire appelé mots_scores pour stocker les scores de chaque mot. Ensuite, elle itère sur chaque dictionnaire dans la liste matrice, et pour chaque mot et score dans le dictionnaire, elle vérifie si le mot existe déjà dans le dictionnaire mots_scores. Si le mot n'existe pas, il est ajouté au dictionnaire avec son score. Si le mot existe déjà, le code vérifie si le score est plus élevé et le met à jour si nécessaire.

Enfin, la fonction trie les mots en fonction de leurs scores et renvoie les trois premiers mots ayant les scores les plus élevés. Le nombre de mots à renvoyer peut être ajusté en modifiant la valeur dans la découpe [:3] à la fin de l'assignation de mots_plus_eleves.

<h3>mots_repetes_chirac</h3>
Ce code définit une fonction appelée mots_repetes_chirac qui prend un dictionnaire en entrée. Il trie le dictionnaire par les valeurs de manière décroissante et récupère les cinq mots les plus répétés. Enfin, il renvoie ces cinq mots.

<h3>filtrer_mots_pas_importants</h3>
Ce code définit une fonction appelée filtrer_mots_pas_importants qui filtre les mots qui ne sont pas importants à partir d'un dictionnaire donné TFchirac en fonction d'une liste de mots mots_pas_importants. Il crée un nouveau dictionnaire discours_chirac_sans_mots_pas_importants en itérant sur chaque paire clé-valeur dans TFchirac et en ajoutant la paire au nouveau dictionnaire uniquement si la clé (le mot) n'est pas présente dans la liste mots_pas_importants. La fonction renvoie ensuite le nouveau dictionnaire.

<h3>trouver_president_mot</h3>
Ce code définit une fonction appelée trouver_president_mot qui prend deux paramètres : liste_presidents (une liste de noms de présidents) et mot (un mot).

La fonction parcourt la liste des présidents à partir du deuxième élément et vérifie si le mot donné est présent dans l'élément actuel. Si le mot est trouvé, il ajoute le nom du président précédant cet élément à une nouvelle liste appelée presidents.

Enfin, la fonction renvoie la liste des présidents.

<h3>mot_frequence_president</h3>
Ce code définit une fonction mot_frequence_president qui prend en paramètres une liste et un mot. Il calcule la fréquence du mot donné pour chaque président dans la liste et renvoie le nom du président ayant la fréquence la plus élevée de ce mot dans son dictionnaire.

<h3>tokenisation_question</h3>
Ce code définit une fonction appelée tokenisation_question qui prend une question en entrée et la tokenise en mots individuels. La fonction itère sur chaque caractère de la question et vérifie s'il est en majuscule, en minuscule, un espace ou une ponctuation. S'il est en majuscule, il le convertit en minuscule et l'ajoute au mot actuel. S'il est en minuscule, il l'ajoute au mot actuel. S'il s'agit d'un espace ou d'un signe de ponctuation, il ajoute le mot actuel à une liste et réinitialise le mot actuel. Enfin, il retourne la liste des mots.

<h3>question_corpus</h3>
Ce code définit une fonction appelée question_corpus qui prend une question en entrée.

La fonction effectue les étapes suivantes :

  - Elle obtient le répertoire du fichier courant.
  - Elle crée un chemin vers le répertoire 'cleaned' dans le répertoire courant.
  - Elle charge le dictionnaire IDF depuis le répertoire 'cleaned'.
  - Elle tokenize la question pour obtenir une liste de mots.
  - Elle filtre les mots qui ne sont pas présents dans le dictionnaire IDF.
  - Elle renvoie la liste filtrée de mots.

Le but de ce code est d'extraire une liste de mots pertinents à partir d'une question en la comparant à un corpus.

<h3>TF_question</h3>
Ce code définit une fonction appelée TF_question qui calcule la fréquence des termes d'une question donnée. Il convertit d'abord la question en une liste de mots, puis les mots sont joints en une seule chaîne de caractères. Enfin, il retourne la fréquence des termes de la chaîne à l'aide d'une fonction appelée TF.

<h3>TF_IDF_question</h3>
Ce code définit une fonction appelée TF_IDF_question qui prend une question en entrée.

La fonction commence par définir la variable directory avec le chemin absolu du fichier actuel. Elle concatène ensuite le nom du répertoire avec la chaîne de caractères 'cleaned' et assigne le résultat à la variable cleaned_dir.

Ensuite, elle appelle une fonction appelée IDF avec cleaned_dir comme argument et assigne la valeur de retour à la variable IDFdic.

Ensuite, elle appelle une autre fonction appelée question_corpus avec question comme argument et assigne la valeur de retour à la variable liste_mot_question.

Après cela, elle initialise une liste vide appelée vecteur_tf_idf.

Le code parcourt ensuite chaque paire clé-valeur dans le dictionnaire IDFdic. À l'intérieur de la boucle, il initialise une variable appelée score_tf à 0. Il parcourt ensuite les indices de la liste liste_mot_question et vérifie si la clé actuelle est égale au mot à l'indice actuel. Si c'est le cas, il incrémente score_tf de 1.

Pour chaque paire clé-valeur, il calcule le score_idf en prenant la valeur du dictionnaire IDFdic. Il ajoute ensuite le produit de score_tf et score_idf à la liste vecteur_tf_idf.

Enfin, la fonction renvoie la liste vecteur_tf_idf.

<h3>produit_scalaire</h3>
Ce extrait de code définit une fonction appelée produit_scalaire qui prend deux listes, a et b, en tant que paramètres. La fonction calcule le produit scalaire des deux listes en itérant sur les éléments de b et en multipliant chaque élément correspondant de a et b, puis en ajoutant le résultat à une variable appelée scalaire. Enfin, la fonction renvoie le produit scalaire calculé.

<h3>norme_vecteur</h3>
Ce morceau de code définit une fonction appelée norme_vecteur qui calcule la norme euclidienne d'un vecteur a. Il initialise une variable norme à 0, puis itère sur chaque élément de a, le met au carré et l'ajoute à norme. Enfin, il retourne la racine carrée de norme en utilisant la fonction math.sqrt.

<h3>similarite</h3>
This code defines a function called similarite that takes two parameters a and b. It calculates the dot product of a and b using a function called produit_scalaire, and divides it by the product of the norms of a and b calculated using a function called norme_vecteur. The result is returned.

<h3>document_pertinent</h3>
Ce code définit une fonction appelée document_pertinent qui prend deux paramètres : matrice_TF_IDF et vecteur_TF_IDF. Il initialise une variable similariteMax à 0 et une variable de chaîne vide discoursPertinent.

Ensuite, il itère sur les éléments du dictionnaire matrice_TF_IDF. Pour chaque élément, il calcule la similarité entre vecteur_TF_IDF et la valeur de l'élément actuel en utilisant une fonction similarite. Si la similarité est supérieure à similariteMax, il met à jour similariteMax et assigne le nom_doc correspondant à discoursPertinent.

Enfin, il retourne la valeur de discoursPertinent.

<h3>creer_matrice</h3>

Ce code définit une fonction appelée creer_matrice qui prend en entrée une liste de dictionnaires (matrice_dicos).

La fonction effectue les étapes suivantes :

  - Elle crée un ensemble de tous les mots uniques en itérant sur chaque dictionnaire de matrice_dicos et en ajoutant les clés à l'ensemble.
  - Elle trie les mots uniques par ordre alphabétique et les stocke dans une liste appelée mots_uniques_tries.
  - Elle crée un dictionnaire appelé index_mot qui associe chaque mot unique à un indice unique.
  - Elle initialise une matrice (nouvelle_matrice) avec des listes vides, où le nombre de lignes est égal au nombre de dictionnaires dans matrice_dicos, et le nombre de colonnes est égal au nombre de mots uniques.
  - Elle remplit la matrice avec les valeurs numériques des dictionnaires dans matrice_dicos, en utilisant les indices du dictionnaire index_mot.
  - Enfin, elle renvoie la matrice remplie.
    
En résumé, ce code crée une représentation matricielle d'une collection de dictionnaires, où chaque ligne correspond à un dictionnaire et chaque colonne correspond à un mot unique, les valeurs indiquant la présence ou l'absence du mot dans chaque dictionnaire.

<h1>Créateur</h1>
Axel Monsarrat
Yanis Amara
