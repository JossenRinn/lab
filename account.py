class Account:
  def __init__(self, name: str) -> None:
      self.__account_name = name
      self.__account_balance = 0
      """
      Constructor to create initial state of an account 
      :param name: Name  of account holder
      """

  def deposit(self, amount: float) -> bool:
      if amount>0:
          self.__account_balance += amount
          return True
      else:
          return False
      """
      Method to deposit money into the account balance
      :param amount: Amount to be deposited to account_balance
      :return: Status of if money was deposited (True/False)
      """

  def withdraw(self, amount: float) -> bool:
      if amount <=0 or amount> self.__account_balance:
          return False
      else:
          self.__account_balance -= amount
          return True
      """
      Method to withdraw money from the account balance
      :param amount: Amount to be withdrawn from the account balance
      :return: Status of if money was withdrawn (True/False)
      """

  def get_balance(self) -> float:
      return self.__account_balance
  """
  Method that returns the account balance.
  :return: Account balance.
  """

  def get_name(self) -> str:
      return self.__account_name
  """
  Method that returns the account name.
  :return: Account name
  """




