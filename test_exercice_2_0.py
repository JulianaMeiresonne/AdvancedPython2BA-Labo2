import pytest
import exercice_2_0
import re
#!!!!!!! le nom du fichier de test est important, il doit être : test_ ou se terminer par _test.py (ex: test_math.py) et 
#Les fonctions doivent commencer par test_ (ex: def test_addition():).

def test_expression_phone_number():
    p = re.compile(exercice_2_0.pattern0)
    assert p.match('+xx xxx xx xx xx') == None
    assert p.match('+33 333 33 33 33') != None
    assert p.match('+33 333 33 33 3') == None
    assert p.match('+33 333 33 33 33 ') == None
    assert p.match('33 333 33 33 33 ') == None


def test_expression_integers():
    p = re.compile(exercice_2_0.pattern1)
    assert p.match('-3') != None
    assert p.match('0') != None
    assert p.match('a') == None
    assert p.match('3') != None

def test_registration_plate():
    p = re.compile(exercice_2_0.pattern2)
    assert p.match('1ABC345') != None
    assert p.match('3567TYU') != None
    assert p.match('567TYU') != None
    assert p.match('ABC345') != None
    assert p.match('6784457') == None
    assert p.match('aaaaa') == None
    assert p.match('AAAAA') == None

def test_expression_windows_volume():
    p = re.compile(exercice_2_0.pattern3)
    assert p.match('C:\\') != None