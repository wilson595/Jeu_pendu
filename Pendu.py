#fonctions nécessaires
import random  #pour sélectionner un mot aléatoire dans la liste des mots disponibles
import unicodedata #pour supprimer les accents
import os #pour gérer les fichiers et les chemins du système


def enlever_accents(texte):
    """
    Supprime les accents d'une chaîne de caractères pour faciliter la comparaison.
    Exemple : 'éèàûô' devient 'eeauo'.
    """
    texte = unicodedata.normalize('NFD', texte)  # Décompose les caractères accentués
    texte = texte.encode('ascii', 'ignore')      # Supprime les parties non ASCII (les accents)
    texte = texte.decode("utf-8")                # Reconvertit en chaîne UTF-8
    return str(texte)

def choisir_mot(fichier="mots_pendu.txt"):
    """
    Choisit un mot aléatoire depuis le fichier spécifié s'il existe.
    Sinon, utilise une liste de mots par défaut.
    Supprime les accents des mots pour uniformiser le jeu.
    """
    mots_par_defaut = [ "surprenant", "judicieuse", "derisoire", "hôpital",
        "écriture", "délicieux", "carbone", "veneneux" ]

    if os.path.isfile(fichier):  # Vérifie que le fichier existe
        with open(fichier, 'r', encoding='utf-8') as f:
            lignes = f.readlines()
        mots = []
        for ligne in lignes:
            mot = ligne.strip().lower()
            if mot:
                mot_sans_accents = enlever_accents(mot)
                mots.append(mot_sans_accents)
        if mots:
            return random.choice(mots)  # Choisit un mot aléatoire de la liste
        else:
            print(f"Avertissement : Le fichier '{fichier}' est vide. Utilisation de la liste par défaut.")
    else:
        print(f"Avertissement : Le fichier '{fichier}' est introuvable. Utilisation de la liste par défaut.")

    return random.choice(mots_par_defaut)

def demander_lettre(lettres_devinees):
    """
    Demande à l'utilisateur une lettre valide :
    - une seule lettre
    - un caractère alphabétique
    - non déjà proposé
    Supprime les accents pour standardiser les réponses.
    """
    while True:
        proposition = enlever_accents(input("Entrez une lettre : ").lower())
        if len(proposition) != 1:
            print("Veuillez entrer une seule lettre.")
        elif not proposition.isalpha():
            print("Veuillez entrer un caractère alphabétique.")
        elif proposition in lettres_devinees:
            print("Vous avez déjà deviné cette lettre. Essayez-en une autre.")
        else:
            return proposition

def donner_indice(mot, lettres_devinees, chances_restantes):
    """
    BONUS : Donne une lettre qui ne se trouve PAS dans le mot.
    Cela aide le joueur à éliminer des possibilités.
    """
    if chances_restantes > 0:
        lettres_possibles = "abcdefghijklmnopqrstuvwxyz"
        lettres_disponibles = []
        for lettre in lettres_possibles:
            if lettre not in mot and lettre not in lettres_devinees:
                lettres_disponibles.append(lettre)
        if lettres_disponibles:
            indice = random.choice(lettres_disponibles)
            print(f"Indice : La lettre '{indice}' N'EST PAS dans le mot.")
            return indice
        else:
            print("Désolé, aucun indice disponible pour le moment.")
    return None
#fonctions nécessaires
import random  #pour sélectionner un mot aléatoire dans la liste des mots disponibles
import unicodedata #pour supprimer les accents
import os #pour gérer les fichiers et les chemins du système


def enlever_accents(texte):
    """
    Supprime les accents d'une chaîne de caractères pour faciliter la comparaison.
    Exemple : 'éèàûô' devient 'eeauo'.
    """
    texte = unicodedata.normalize('NFD', texte)  # Décompose les caractères accentués
    texte = texte.encode('ascii', 'ignore')      # Supprime les parties non ASCII (les accents)
    texte = texte.decode("utf-8")                # Reconvertit en chaîne UTF-8
    return str(texte)

def choisir_mot(fichier="mots_pendu.txt"):
    """
    Choisit un mot aléatoire depuis le fichier spécifié s'il existe.
    Sinon, utilise une liste de mots par défaut.
    Supprime les accents des mots pour uniformiser le jeu.
    """
    mots_par_defaut = [
        "surprenant", "judicieuse", "derisoire", "hôpital",
        "écriture", "délicieux", "carbone", "veneneux"
    ]

    if os.path.isfile(fichier):  # Vérifie que le fichier existe
        with open(fichier, 'r', encoding='utf-8') as f:
            lignes = f.readlines()
        mots = []
        for ligne in lignes:
            mot = ligne.strip().lower()
            if mot:
                mot_sans_accents = enlever_accents(mot)
                mots.append(mot_sans_accents)
        if mots:
            return random.choice(mots)  # Choisit un mot aléatoire de la liste
        else:
            print(f"Avertissement : Le fichier '{fichier}' est vide. Utilisation de la liste par défaut.")
    else:
        print(f"Avertissement : Le fichier '{fichier}' est introuvable. Utilisation de la liste par défaut.")

    return random.choice(mots_par_defaut)

def afficher_mot(mot, lettres_devinees):
    """
    Affiche le mot à deviner avec des lettres découvertes et des tirets pour les autres.
    Exemple : si le mot est 'maison' et que 'm' et 'o' ont été devinées, affiche : 'm _ _ _ o _'
    """
    affichage = ""
    for lettre in mot:
        if lettre in lettres_devinees:
            affichage += lettre + " "
        else:
            affichage += "_ "
    return affichage.strip()

def demander_lettre(lettres_devinees):
    """
    Demande à l'utilisateur une lettre valide :
    - une seule lettre
    - un caractère alphabétique
    - non déjà proposé
    Supprime les accents pour standardiser les réponses.
    """
    while True:
        proposition = enlever_accents(input("Entrez une lettre : ").lower())
        if len(proposition) != 1:
            print("Veuillez entrer une seule lettre.")
        elif not proposition.isalpha():
            print("Veuillez entrer un caractère alphabétique.")
        elif proposition in lettres_devinees:
            print("Vous avez déjà deviné cette lettre. Essayez-en une autre.")
        else:
            return proposition

def donner_indice(mot, lettres_devinees, chances_restantes):
    """
    BONUS : Donne une lettre qui ne se trouve PAS dans le mot.
    Cela aide le joueur à éliminer des possibilités.
    """
    if chances_restantes > 0:
        lettres_possibles = "abcdefghijklmnopqrstuvwxyz"
        lettres_disponibles = []
        for lettre in lettres_possibles:
            if lettre not in mot and lettre not in lettres_devinees:
                lettres_disponibles.append(lettre)
        if lettres_disponibles:
            indice = random.choice(lettres_disponibles)
            print(f"Indice : La lettre '{indice}' N'EST PAS dans le mot.")
            return indice
        else:
            print("Désolé, aucun indice disponible pour le moment.")
    return None

# Fonction principale du jeu 

def jouer_pendu():
    """
    Lancement de la boucle principale du jeu du Pendu.
    Le joueur a 6 chances pour deviner un mot, lettre par lettre.
    """
    mot_a_deviner = choisir_mot("mots_pendu.txt")
    if not mot_a_deviner:
        print("Erreur : Impossible de sélectionner un mot. Fin du jeu.")
        return

    lettres_devinees = []
    chances = 6
    jeu_termine = False
    indice_utilise = False

    print("Bienvenue au jeu du Pendu !")

    while not jeu_termine:
        print("-" * 50)
        print(f"Mot à deviner : {afficher_mot(mot_a_deviner, lettres_devinees)}")
        print(f"Chances restantes : {chances}")
        if lettres_devinees:
            print("Lettres déjà proposées :", end=" ")
            for lettre in sorted(lettres_devinees):
                print(lettre, end=", ")
            print()  # saut de ligne
        else:
            print("Lettres déjà proposées : Aucune")

        # Proposer un indice uniquement après le premier essai
        if 0 < chances < 6:
            if not indice_utilise or input("Voulez-vous un indice ? (o/n) : ").lower() == 'o':
                resultat_indice = donner_indice(mot_a_deviner, lettres_devinees, chances)
                if resultat_indice:
                    lettres_devinees.append(resultat_indice)
                    print(f"L'indice '{resultat_indice}' a été ajouté à vos lettres devinées (il n'est pas dans le mot).")
                indice_utilise = True

        lettre = demander_lettre(lettres_devinees)
        lettres_devinees.append(lettre)

        if lettre in mot_a_deviner:
            print(f"Bonne pioche ! La lettre '{lettre}' est dans le mot.")
            lettres_restantes = False
            for l in mot_a_deviner:
                if l not in lettres_devinees:
                    lettres_restantes = True
                    break
            if not lettres_restantes:
                print("-" * 50)
                print(f"Félicitations ! Vous avez trouvé le mot : '{mot_a_deviner}'")
                jeu_termine = True
        else:
            print(f"Dommage ! La lettre '{lettre}' n'est pas dans le mot.")
            chances -= 1
            if chances == 0:
                print("-" * 50)
                print(f"Vous avez perdu ! Le mot était : '{mot_a_deviner}'")
                jeu_termine = True

    if input("Voulez-vous rejouer ? (o/n) : ").lower() == 'o':
        jouer_pendu()
    else:
        print("Merci d'avoir joué ! À bientôt.")

jouer_pendu()
