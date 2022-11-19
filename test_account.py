from pytest import *
import pytest
from account import *

class Test:
    def setup_method(self):
        self.p1 = Account('John')

    def teardown_method(self):
        del self.p1

    def test_init(self):
        assert self.p1.get_name() == 'John'
        assert self.p1.get_balance() == 0


    def test_deposit(self):
        assert self.p1.deposit(10) is True
        assert self.p1.deposit(-1) is False
        assert self.p1.deposit(0) is False

    def test_withdraw(self):
        assert self.p1.withdraw(-1) is False
        assert self.p1.withdraw(0) is False
        assert self.p1.withdraw(100) is False
        self.p1.deposit(5)
        assert self.p1.withdraw(2) is True


