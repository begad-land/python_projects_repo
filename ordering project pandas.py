
import time as tm
import pandas as pd

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
        
        print(f'1)cash\n2)debit\n ')

        method=input('how would you like to pay? ')
        
        if method in ['1', 'cash']:
            self.cash.cash_status()

        elif method in ['2', 'debit']:
            self.debit.debit_status()

#calculating the total
class Total:
    def __init__(self,lst_prices=[]) -> None:
        self.lst_prices=lst_prices
        self.total_bill=0

    def calc_total(self):
        for price in self.lst_prices:
            self.total_bill+=price
        return round(self.total_bill,2)
    
#gathering the items
class Items:
    def __init__(self,lst_items=[]) -> None:
        self.lst_items=lst_items

#creating and presenting the elements of the invoice
class Invoice:
    def __init__(self,order) -> None:
        self.order=order
        self.total=Total(v[0] for k, v in self.order.items())
        self.items=Items(self.order[k] for k in self.order)
        
    def invoice_presentaion(self):
        amount_of_items=0
        fees= self.total.calc_total() * 0.15

        for k, v in self.order.items():
            amount_of_items+=v[1]

        print()
        for k, v in self.order.items():
            print(f'Item: {k:5} {v[1]}X | Price: {v[0]}$\n\n------------------------------------------')

        if amount_of_items >= 4:
            discounted_percentage= 10 / 100 * self.total.calc_total()
            print(f'10% DISCOUNT GRANTED!')
            print(f'Total: {round(self.total.calc_total() - discounted_percentage,2)}$\n------------------------------------------')
        else:
            print(f'Total: {round(self.total.calc_total()),2}$\n------------------------------------------')

        print(f'fees: {round(fees,2)}$')
        when=tm.localtime()
        Time=tm.strftime('%B %d %Y %I%p:%M:%S', when )
        print(f'date of the order:\n{Time}')    

menu={
    'foods':['pizza','steak','burger','Mango juice','mushroom soup'],
    'prices':[5.36, 30.15 ,10.45, 4.25, 15.75],
    }
menu_df=pd.DataFrame(menu)
menu_df.index=['1','2','3','4','5']

print(f'-------------MENU-----------\n{menu_df}')

lst_of_nums=['1','2','3','4','5']

order={}

#try to move this chunk of code into the Items class############################################
while True:
    picks=list(input('-----------------------------\ninsert the number of the item that you want ').split())

    for pick in picks:
        if pick not in lst_of_nums:
            continue

        order[menu_df.loc[pick]['foods']]=[
                                          round(menu_df.loc[pick]['prices'] * picks.count(pick),2), picks.count(pick)
                                          ] 
    break
###################################################################################################
pay=Pay()
pay.getting_payment_method()

invoice=Invoice(order)
invoice.invoice_presentaion()