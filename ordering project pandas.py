
import time as tm
import pandas as pd



class Total:
    def __init__(self,lst_prices=[]) -> None:
        self.lst_prices=lst_prices
        self.total_bill=0

    def calc_total(self):
        for price in self.lst_prices:
            self.total_bill+=price
        return self.total_bill

class Items:
    def __init__(self,lst_items=[]) -> None:
        self.lst_items=lst_items



class Invoice:
    def __init__(self,order) -> None:
        self.order=order
        self.total=Total(self.order[k][0] for k, v in self.order.items())
        self.items=Items(self.order[k] for k in self.order)
        

    def invoice_presentaion(self):
        print()
        for k, v in self.order.items():
            print(f'Item: {k:5} {v[1]}X | Price: {v[0]}$\n\n------------------------------------------')

        print(f'Total:{round(self.total.calc_total(),2)}$\n------------------------------------------')
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

while True:
    picks=list(input('-----------------------------\ninsert the number of the item that you want ').split())

    for pick in picks:
        if pick not in lst_of_nums:
            continue

        order[menu_df.loc[pick]['foods']]=[
                                          round(menu_df.loc[pick]['prices'] * picks.count(pick),2), picks.count(pick)
                                          ] 
    break

invoice=Invoice(order)
invoice.invoice_presentaion()
