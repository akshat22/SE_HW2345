import pytest

SymTestObj=Sym()
def test_sym_add(self):
    SymTestObj.add("a")
    SymTestObj.add("a")
    SymTestObj.add("a")
    SymTestObj.add("a")
    SymTestObj.add("b")
    SymTestObj.add("b")
    SymTestObj.add("c")
    assert SymTestObj.total==7, "Addition failed"
def test_sym_mid(self):
    element=SymTestObj.mid()
    assert element=='a',"Mode incorrect"
def test_sym_div(self):
    sd=SymTestObj.div()
    assert sd>=1.37 and sd<=1.38, "Incorrect Standard Deviation"
