class Account:
    """
    A class representing details for a person's account
    """

    def __init__(self, name):
        """
        Constructor to create initial state of a person's account
        :param name: Person's name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float):
        """
        Method to add to a person's account
        :param amount: Amount to be added to account
        :return: Whether amount was added to account
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float):
        """
        Method of subtracting from a person's account
        :param amount: Amount to be
        :return: Whether amount was subtracted from account
        """
        if 0 < amount < self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        """
        Method to access a person's account balance
        :return: Person's account balance
        """
        return self.__account_balance

    def get_name(self):
        """
        Method to access a person's name
        :return: Person's name
        """
        return self.__account_name
