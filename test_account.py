import pytest
from account import *


class Test:
    def setup_method(self):
        self.a1 = Account('Joe')

    def teardown(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'Joe'
        assert self.a1.get_balance() == 0.0

    def test_deposit(self):
        assert self.a1.deposit(-20.0) is False
        assert self.a1.get_balance() == pytest.approx(0.0, abs=0.01)
        assert self.a1.deposit(0.0) is False
        assert self.a1.get_balance() == pytest.approx(0.0, abs=0.01)
        assert self.a1.deposit(10.0) is True
        assert self.a1.get_balance() == pytest.approx(10.0, abs=0.01)

    def test_withdraw(self):
        self.a1.deposit(20.0)
        assert self.a1.withdraw(-200.0) is False
        assert self.a1.get_balance() == pytest.approx(20.0, abs=0.01)
        assert self.a1.withdraw(0.0) is False
        assert self.a1.get_balance() == pytest.approx(20.0, abs=0.01)
        assert self.a1.withdraw(10.0) is True
        assert self.a1.get_balance() == pytest.approx(10.0, abs=0.01)
        assert self.a1.withdraw(20.0) is False
        assert self.a1.get_balance() == pytest.approx(10.0, abs=0.01)
        assert self.a1.withdraw(10.0) is True
        assert self.a1.get_balance() == pytest.approx(0.0, abs=0.01)
