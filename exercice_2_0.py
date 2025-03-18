''''
Écrivez un programme qui demande à l’utilisateur d’encoder une chaine de caractères et qui vérifie si cette dernière satisfait exactement le motif suivant :
(a) Un numéro de téléphone de la forme +xx xxx xx xx xx où les x sont tous des chiffres.
(b) Un nombre entier, qui commence éventuellement avec un signe + ou − devant, et sans espaces aucun.
(c) Une plaque d’immatriculation qui peut prendre l’un des deux formes XLLLDDD ou XDDDLLL,
où L est une lettre et D est un chiffre, et X est un chiffre optionnel (entre 1 et 9).
(d) Le nom d’un volume sous windows qui est, pour rappel, de la forme C:\ (une lettre majuscule
suivie de deux-points et backslash).
'''
import re

pattern0 = r'^\+[0-9]{2}\s[0-9]{3}\s[0-9]{2}\s[0-9]{2}\s[0-9]{2}$'#numéro de téléphone
p0 = re.compile(pattern0)

pattern1 = r'^[\+\-]?[0-9]{1}$' # nombre entier #? permet de rendre le crochet optionel donc c'est soit +, soit - soit rien devant 
p1 = re.compile(pattern1)

pattern2 = r'^[0-9]?[A-Z]{3}[0-9]{3}|[0-9]?[0-9]{3}[A-Z]{3}$' #plaque d’immatriculation
p2 = re.compile(pattern2)

pattern3 = r'^C:\\$' #nom d’un volume sous windows
p3 = re.compile(pattern3)
check = "None"


if __name__ == '__main__':
    while check == "None" :
        print("Entrez votre numéro de téléphone sous la forme +xx xxx xx xx xx")
        Responce0 = input()
        print("Entrez nombre entier")
        Responce1 = input()
        print("Entrez votre plaque d’immatriculation sous la forme XLLLDDD ou XDDDLLL")
        Responce2 = input()
        print("Entrez Le nom d’un volume sous windows sous la forme C:\\")
        Responce3 = input()
        if p0.match(Responce0) and p1.match(Responce1) and p2.match(Responce2) and p3.match(Responce3) is not None :
            check = "OK"
        elif p0.match(Responce0) == "None":
            print("Le numero de téléphone entré n'est pas correct, réessayez!!")
        elif p1.match(Responce1) == "None":
            print("Le nombre entier entré n'est pas correct, réessayez!!")
        elif p2.match(Responce2) == "None":
            print("La plaque d’immatriculation entrée n'est pas correct, réessayez!!")
        elif p3.match(Responce3) == "None":
            print("Le nom du volume sous windows entré n'est pas correct, réessayez!!")

# Collect Error 1 : mon code de base avait une erreur, l'expressoin reeguliere était mal écrite donc on code avait une erreur quand il collecter les donner pour faire les test après
#Collect Error 2 : mon code avait des input() donc au moment de la collect de donner ça bloquer sur le input() donc il faut mettre if __name__ == '__main__': ppur que si mon n'est pas dans le ficher main alors cette partie du code s'execute

# Test project : On sera coter sur le coverage de notre project => voir S1 coverage