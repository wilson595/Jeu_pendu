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

d