# This program initializes the savings account class

import savings_account


def main():

    # Accepting the interest rate, account number and account balance from the user

    print('\nEnter the following information for your savings account.\n')
    account_number = input("Enter your Account Number: ")
    interest_rate = float(input("Enter the Interest Rate: "))
    account_balance = float(input("Enter your Balance: "))

    # Creating the savings account object

    savings_account1 = savings_account.Savings_Account(
        account_number, interest_rate, account_balance)

    # Accepting the interest rate, account number, account balance and maturity date from the user

    print('\nEnter the following information for the Certificate of Deposit.\n')
    account_number = input("Enter your Account Number: ")
    interest_rate = float(input("Enter the Interest Rate: "))
    account_balance = float(input("Enter your Balance: "))
    maturity_date = input("Enter Maturity Date: ")

    # Creating the savings account object

    certificate_of_deposit1 = savings_account.Certificate_of_Deposit(
        account_number, interest_rate, account_balance, maturity_date)

    # Print the Savings Account Data Entered to Screen
    print(
        f'''\nData Entered by the User:\n\nSavings Account\n----------------\nAccount Number: {savings_account1.return_account_number()}\nInterest Rate: {savings_account1.return_interest_rate()}\nBalance: ${savings_account1.return_account_balance():.2f}''')
    
     # Print the Certificate of Deposit Data Entered to Screen
    print(
        f'''\nData Entered by the User:\n\nCertificate of Deposit\n---------------------\nAccount Number: {savings_account1.return_account_number()}\nInterest Rate: {savings_account1.return_interest_rate()}\nBalance: ${savings_account1.return_account_balance():.2f}\nMaturity date: {certificate_of_deposit1.return_maturity_date()}''')


# Calling the main function

if __name__ == '__main__':
    main()