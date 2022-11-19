class Account:
  def __init__(self, name: str) -> None:
      self.__account_name = name
      self.__account_balance = 0
      """
      Function to initialize account name and account balance variables
      :param name: Name  of account holder (account_name)
      """

  def deposit(self, amount: float) -> bool:
      if amount>0:
          self.__account_balance += amount
          return True
      else:
          return False
      """
      Function to Deposit money into the account balance, only if the amount is greater than or equal to 0.
      From here, returns true if money was added and false if no money was added.
      :param amount: Amount to be deposited to account_balance
      :return: If money was deposited
      """

  def withdraw(self, amount: float) -> bool:
      if amount <=0 or amount> self.__account_balance:
          return False
      else:
          self.__account_balance -= amount
          return True
      """
      Function to Withdraw money from the account balance, only if the amount is less than or equal to zero, or if
      the amount is greater than the account balance. Returns true if money was withdrawn and returns false
      if no money was withdrawn.
      :param amount: Amount to be withdrawn from account_balance
      :return: If money was withdrawn
      """

  def get_balance(self) -> float:
      return self.__account_balance
  """
  Function that returns the account balance.
  :return: Account balance.
  """

  def get_name(self) -> str:
      return self.__account_name
  """
  Function that returns the account name.
  :return: Account name
  """




