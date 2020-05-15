import pytest

from python.Calc import Calc


class TestCalc:
    def setup(self):
        self.c = Calc()
    @pytest.mark.parametrize("a,b,expect",[(1,2,3),(0,0,0),(-1,1,0),(0.2,2,2.2)])
    def test_add(self,a,b,expect):
        res=self.c.add(a,b)
        assert res == expect
if __name__ == '__main__':
    pytest.main('-vs')