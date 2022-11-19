from account import *


class Test:
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
        assert self.p1.deposit(20) == 20
        assert self.p2.deposit(10.5) == 10.5
        assert self.p1.deposit(-1) == 20

    def test_withdraw(self):
        assert self.p1.withdraw(5) == 15
        assert self.p2.withdraw(0.5) == 10
        assert self.p2.withdraw(0.5) == 10

