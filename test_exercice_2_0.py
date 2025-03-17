import pytest
import exercice_2_0
import re
#!!!!!!! le nom du fichier de test est important, il doit être : test_ ou se terminer par _test.py (ex: test_math.py) et 
#Les fonctions doivent commencer par test_ (ex: def test_addition():).

def test_expression_phone_number():
    exercice_2_0.pattern0
    p = re.compile(exercice_2_0.pattern0)
    assert p.match('+xx xxx xx xx xx') == None
    assert p.match('+33 333 33 33 33') != None
    assert p.match('+33 333 33 33 3') == None
    assert p.match('+33 333 33 33 33 ') == None
    assert p.match('33 333 33 33 33 ') == None


def test_roots():
    pass

def test_integrate():
    pass