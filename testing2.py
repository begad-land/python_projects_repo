
import time as tm
import pandas as pd

class Total:
    def __init__(self,lst_prices=[]) -> None:
        self.lst_prices=lst_prices
        self.total_bill=0

    def calc_total(self):
        for price in self.lst_prices:
            self.total_bill+=price
        return round(self.total_bill,2)

class Items:
    def __init__(self,lst_items=[]) -> None:
        self.lst_items=lst_items

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
            print(f'Total: {self.total.calc_total()}$\n------------------------------------------')

        print(f'fees: {round(fees,2)}$')
        when=tm.localtime()
        Time=tm.strftime('%B %d %Y %I%p:%M:%S', when )
        print(f'date of the order:\n{Time}')    

menu={
    'foods':['pizza','steak','burger','Mango juice','mushroom soup'],
    'prices':[5.36, 30.15 ,10.45, 4.25, 15.75],
    }

sizes=['L','M','S']



menu_df=pd.DataFrame(menu)
menu_df.index=['1','2','3','4','5']

print(f'-------------MENU-----------\n{menu_df}')

lst_of_nums=['1','2','3','4','5']
order={}

items=[]
prices=[]
amount=[]


while True:
    picks=list(input('-----------------------------\ninsert the number of the item that you want ').split())



    sizes_picked=list(input('insert sizes ').upper().split())

    for pick in picks:
        if pick not in lst_of_nums:
            continue

        items.append(menu_df.loc[pick]['foods'])
        prices.append(menu_df.loc[pick]['prices'])
        amount.append(picks.count(pick))
        order={
              'Item':items,
              'Price':prices,
              'size':sizes,
              }

    break

order_df=pd.DataFrame(order)

print(order_df)



#order2={
        #'items':items,
        #'prices':prices,
        #'sizes':sizes_picked,
        #'amount':amount
       #


#invoice=Invoice(order)
#invoice.invoice_presentaion()

