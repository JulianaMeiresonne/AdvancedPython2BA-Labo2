''''
Écrivez un programme qui ouvre un fichier texte et qui retrouve tous les nombres qui y apparaissent.
Le programme produit en sortie un inventaire de ces nombres, séparés par des virgules et avec le numéro de ligne où ils apparaissent. Voici un exemple d’exécution :
& python3 labo2-q2.py monfichier.txt 
Line 3: 829, -12, 88
Line 12: 99 Line 28: +15
Astuce : Pour lire le paramètre de la ligne de commande, importez le module sys et utilisez la liste sys.args qui va contenir tous ces paramètres.
'''
import re

def computefile(path: str):
    pattern0 = r'[+-]?[0-9]+'#numéro de téléphone , r'^[+-]?[0-9]{0,100}$' = cela prend en compte '' car 0 c'est rien donc 0='', si je commence à 1 pas de probleme mais + = permet de faire de 1 à +inf
    # r'^[+-]?[0-9]+$' est trop severe car ^impose que le debut match et $ impose que la fin match
    p0 = re.compile(pattern0)
    mots = {}
    line = None
    i =0
    try:
        with open(path) as file:
            while line !='': # tant que line n'est pas à la dernier ligne de mon fichier '' alors ma boucle while continue
                i += 1
                line = file.readline() # il lit une ligne à chaque fois qu'il est applé
                if p0.match(line) != None:
                  mots[f'Line{i}'] = p0.findall(line)
    except FileNotFoundError:
        print('Le fichier est introuvable')
    except IOError:
        print("Erreur d'entrée/sortie")  
    return mots
print(computefile('number.txt'))
#Refaire l'exercices avec la fonction sys voir photo