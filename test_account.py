import pytest
from account import *


class Test:
    """
    A class to test Account class
    """

    def setup_method(self):
        self.p1 = Account('Mike')
        self.p2 = Account('Alyssa')

    def teardown_method(self):
        del self.p1
        del self.p2

    def test_init(self):
        assert self.p1.get_name() == 'Mike'
        assert self.p1.get_balance() == 0
        assert self.p2.get_name() == 'Alyssa'
        assert self.p1.get_balance() == 0

    def test_deposit(self):
        assert self.p1.deposit(20) == pytest.approx(20, abs=0.001)
        assert self.p2.deposit(10.5) == pytest.approx(10.5, abs=0.001)
        assert self.p1.deposit(-1) is False
        assert self.p1.get_balance() == pytest.approx(20, abs=0.001)
        assert self.p2.deposit(0) is False
        assert self.p2.get_balance() == pytest.approx(10.5, abs=0.001)

    def test_withdraw(self):
        assert self.p1.withdraw(5) == pytest.approx(15, abs=0.001)
        assert self.p2.withdraw(0.5) == pytest.approx(10, abs=0.001)
        assert self.p1.withdraw(0) is False
        assert self.p1.get_balance() == pytest.approx(15, abs=0.001)
        assert self.p2.withdraw(-0.5) is False
        assert self.p2.get_balance() == pytest.approx(10, abs=0.001)
        assert self.p1.withdraw(100) is False
        assert self.p1.get_balance() == pytest.approx(15, abs=0.001)

