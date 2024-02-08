        # Author     : Sanjaykumar.M
        # Date       : 08-02-2024
        # Description: python string methods questions
        # Batch time : 4.00 - 7.00pm

#find the index and modify that index value ?

name = input("Enter a name: ")
index_to_modify = int(input("Enter the index to modify: "))
modified_letter = input("Enter the modified letter: ")
modified_name = name[:index_to_modify] + modified_letter + name[index_to_modify + 1:]
print("Original Name:", name)
print("Modified Name:", modified_name)

#bank balanvce is 1000 and the user want debit and credit and balance and that amount of interest for yrs?
balance = 1000
print("balance :",balance)
user_want = input("credit or debit : ")
debit_amt = int(input("debit amt : "))
bank_balance = int(balance)-int(debit_amt)
print("bank balance : ", bank_balance)
user_wants = input("credit or debit : ")
credit_amt = int(input("credit amt : "))
bank_balance = int(bank_balance)+int(credit_amt)
print("bank balance : ", bank_balance)
interest_percentage = float(input("interest percentage % : "))
time = int(input("period of time : "))
interest_1_year = int(bank_balance) * int(interest_percentage) * int(time)/100
print("1 year of interest amt : ", interest_1_year)

