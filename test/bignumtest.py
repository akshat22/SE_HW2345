from code.columns import Num
from code import config

numTestObj = Num()

def test_bignum(self):
    num = Num()
    config.the['nums']=32
    for i in range(1000):
        num.add(i+1)
    assert len(num._has)==32