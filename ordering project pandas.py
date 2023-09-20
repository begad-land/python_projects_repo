
import time as tm
import pandas as pd

menu={
    'foods':['pizza','steak','burger','Mango juice','mushroom soup'],
    'prices':[5.36, 30.15 ,10.45, 4.25, 15.75],
    }
menu_df=pd.DataFrame(menu)
menu_df.index=['1','2','3','4','5']

print(f'-------------MENU-----------\n{menu_df}')

lst_of_nums=['1','2','3','4','5']

class TakingOrder:
    def __init__(self,order={}) -> None:
        self.order=order

    def taking_the_order(self):
        
        while True:
            picks=list(input('-----------------------------\ninsert the number of the item that you want ').split())

            for pick in picks:
                if pick not in lst_of_nums:
                    continue
                self.order[menu_df.loc[pick]['foods']]=[
                                                            round(menu_df.loc[pick]['prices'] * picks.count(pick),2), picks.count(pick)
                                                        ]
            break
        return self.order

    
#calculate anything that needs calculation in the invoice class
class Calculations:
    def __init__(self, discount=0 , Qnt=0 , total=0 , fees=0 ) -> None:
        self.discount=discount
        self.Qnt=Qnt
        self.total=total
        self.fees=fees
        self.takingorder=TakingOrder()
    
    def calc_total(self):
        for price in self.takingorder.order.values():
            self.total+=price[0]

        return round(self.total,2)
        
    def calc_fees(self):
        self.fees=self.total * 0.15

        return round(self.fees,2)
    
    def calc_discount(self):
       discount_percent= 12 / 100 * self.total
       self.discount= self.total - discount_percent

       return round(self.discount,2)
    
    def quantity(self):
        for i in self.takingorder.order.values():
            self.Qnt+=i[1]

        return self.Qnt

class Invoice:
    def __init__(self) -> None:
       self.takingorder=TakingOrder() 
       self.calculations=Calculations()

    def invoice_presentaion(self):
        for k, v in self.takingorder.order.items():
            print(f'Item: {k:7} {v[1]}X | Price: ${v[0]}\n---------------------------------------------')

        if self.calculations.quantity() >= 4:
            print(f'12% DISCOUNT GRANTED!')
            self.calculations.calc_total()
            print(f'Total: {self.calculations.calc_discount()}')

        else:
            print(f'Total: {self.calculations.calc_total()}')

        print(f'Fees: {self.calculations.calc_fees()}\n---------------------------------------------')
        when=tm.localtime()
        Time=tm.strftime('%B %d %Y %I%p:%M:%S', when )
        print(f'date of the order:\n{Time}')      

x=TakingOrder()
x.taking_the_order()

invoice=Invoice()
invoice.invoice_presentaion()