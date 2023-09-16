
print(f'1)cash\n2)debit\n ')

class Cash:
    def cash_status(self):
        print(f'payment: cash')

class Debit:
   def debit_status(self):
        print(f'payment: debit ')
        debit_no=str(input('insert your debit no '))

        while len(debit_no) !=7:
            print('ERROR: there are still missing numbers')
            debit_no=input('insert your debit no ')

        print(f'your debit number is ****{debit_no[4::]}')

class Pay:
    def __init__(self,) -> None:
        self.cash=Cash()
        self.debit=Debit()

    def getting_payment_method(self):
        method=input('how would you like to pay? ')

        if method in ['1', 'cash']:
            self.cash.cash_status()

        elif method in ['2', 'debit']:
            self.debit.debit_status()


pay=Pay()
pay.getting_payment_method()    