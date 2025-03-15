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

pattern1 = r'^[\+\-]{1}[0-9]{1}$' # nombre entier
p1 = re.compile(pattern1)
#print(p1.match("3")) => cella doit etre mon test 

pattern2 = r'^[1-9]{1}?$' #plaque d’immatriculation
p2 = re.compile(pattern2)
print(p2.match("3"))

pattern3 = r'^\+[0-9]{2}\s[0-9]{3}\s[0-9]{2}\s[0-9]{2}\s[0-9]{2}$' #nom d’un volume sous windows
p3 = re.compile(pattern3)
print()
check = "None"
#and p1.match(Responce) and p2.match(Responce) and p3.match(Responce)
while check == "None" :
    print("Entrez votre numéro de téléphone sous la forme +xx xxx xx xx xx")
    Responce = input()
    if p0.match(Responce) is not None :
        check = "OK"
    else :
        print("Le numero de téléphone entré n'est pas sous +xx xxx xx xx xx, réessayez!!")  