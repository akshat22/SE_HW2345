import pytest

symTestObj=Sym()
def test_sym_add(self):
    symTestObj.add("a")
    symTestObj.add("a")
    symTestObj.add("a")
    symTestObj.add("a")
    symTestObj.add("b")
    symTestObj.add("b")
    symTestObj.add("c")
    assert symTestObj.total==7, "Addition failed"
def test_sym_mid(self):
    element=symTestObj.mid()
    assert element=='a',"Mode incorrect"
def test_sym_div(self):
    sd=symTestObj.div()
    assert sd>=1.37 and sd<=1.38, "Incorrect Standard Deviation"
