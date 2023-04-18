from account import *
import pytest

def setup_method(self):
  self.a1 = Account('Joe')
  
def teardown(self):
  del self.a1
  
def test_init(self):
  assert self.a1.get_name() == 'Joe'
  assert self.a1.get_balance() == 0.0
  
def test_deposit(self):
  assert self.a1.deposit(-20) == False
  assert self.a1.deposit(-20.0) == False
  assert self.a1.deposit(0) == False
  assert self.a1.deposit(0.0) == False
  assert self.a1.deposit(10) == True
  assert self.a1.deposit(10.0) == True
  
def test_withdraw
  assert self.a1.withdraw(-200) == False
  assert self.a1.withdraw(-200.0) == False
  assert self.a1.withdraw(0) == False
  assert self.a1.withdraw(0.0) == False
  assert self.a1.withdraw(10) == True
  assert self.a1.withdraw(20) == False
  assert self.a1.withdraw(20.0) == False
  assert self.a1.withdraw(10.0) == True
