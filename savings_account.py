# This class contains the savings account details

class Savings_Account:

    # Creating the constructor to initialize the class attributes
    def __init__(self, account_number, interest_rate, account_balance):
        self.__account_number = account_number
        self.__interest_rate = interest_rate
        self.__account_balance = account_balance

    # The next following three methods are the setters/mutators
    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate

    def set_account_balance(self, account_balance):
        self.__account_balance = account_balance

    # The next following three methods are the getters/accessors
    def return_account_number(self):
        return self.__account_number

    def return_interest_rate(self):
        return self.__interest_rate

    def return_account_balance(self):
        return self.__account_balance


# This class represents a certificate of deposit account
class Certificate_of_Deposit(Savings_Account):

    # Initializing the attributes by calling the __init__ method
    def __init__(self, account_number, interest_rate, account_balance, maturity_date):

        # Calling the Savings Account Class init method. This inializes the values passed in the above init methods parameter
        Savings_Account.__init__(self, account_number,
                                 interest_rate, account_balance)

        # iniitializing the maturity_date attribute
        self.__maturity_date = maturity_date

    # Accessor and Mutator for the maturity attribute

    def set_maturity_date(self, maturity_date):
        self.__maturity_date = maturity_date

    def return_maturity_date(self):
        return self.__maturity_date
