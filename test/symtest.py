import pytest
from code.columns import Sym

symTestObj = Sym()


def test_sym_add(self):
    symTestObj.add("a")
    symTestObj.add("a")
    symTestObj.add("a")
    symTestObj.add("a")
    symTestObj.add("b")
    symTestObj.add("b")
    symTestObj.add("c")
    assert symTestObj.total == 7, "Addition failed"


def test_sym_mid(self):
    element = symTestObj.mid()
    assert element == 'a', "Incorrect Mode"


def test_sym_div(self):
    sd = symTestObj.div()
    assert 1.37 <= sd <= 1.38, "Incorrect Standard Deviation"
