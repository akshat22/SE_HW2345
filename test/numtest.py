from code.columns import Num

numTestObj = Num()


def test_num_add(self):
    for i in range(1, 101):
        numTestObj.add(i)
    assert numTestObj.total == 100, "Addition failed"


def test_num_mid(self):
    element = numTestObj.mid()
    assert 50 <= element <= 52, "Incorrect Mode"


def test_sym_div(self):
    sd = numTestObj.div()
    assert 30.5 < sd < 32, "Incorrect Standard Deviation"
