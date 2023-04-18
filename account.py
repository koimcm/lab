class Account:
  '''
  A class representing a person's bank account.
  '''
    
  def __init__(self, name: str) -> None:
    '''
    Constructor to make a bank account with 0 dollars to start.
    :param name: Bank customer's name.
    '''
    self.account_name = name
    self.account_balance = 0.0
    
  def deposit(self, amount: float) -> Boolean:
    '''
    Function to add money to the account. 
    :param amount: Amount of money to be added to account.
    :return: Boolean based on if deposit was accepted or not.
    '''
    if amount > 0:
      self.account_balance += self.amount
      return True
    else:
      return False
      
  def withdraw(self, amount: float) -> Boolean:
    '''
    Function to withdraw money from account.
    :param amount: Amount of money to be withdrawn from the account.
    :return: Boolean based on if the withdrawl was accepted or not.
    '''
    if amount <= self.account_balance and amount > 0:
      self.account_balance -= self.amount
      return True
    else:
      return False
  
  def get_balance(self) -> float:
    '''
    Getter method for account balance.
    :return: Account's balance.
    '''
    return self.account_balance
  
  def get_name(self) -> str:
    '''
    Getter method for account holder's name.
    :return: Account holder's name.
    '''
    return self.account_name
