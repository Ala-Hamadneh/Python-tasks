class Person:
    def __init__(self,name,age,balance, bank_name):
        self.name = name
        self.age = age
        self.balance = balance
        self.bank_name = bank_name
def main():
    name="Alaa"
    age=23
    bank_balance=100.0
    bank_name="BOP"

    alaa=Person(name,age,bank_balance,bank_name)

    print("The class of name is : "+type(name).__name__)
    print("The class of age is : "+type(age).__name__)
    print("The class of bank_balance is : "+type(bank_balance).__name__)
    print("The class of alaa is : "+type(alaa).__name__)

if __name__ == "__main__":
    main()