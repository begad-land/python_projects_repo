
import time as tm
import pandas as pd

menu={
    'foods':['Pizza','Steak','Burger','Mango','Soup','Sausage'],
    'prices':[6.36, 30.15 ,10.45, 4.25, 15.75, 3.30],
    }

menu_df=pd.DataFrame(menu)
menu_df.index=['1','2','3','4','5','6']

print(f'---------MENU---------\n{menu_df}')

class TakingOrder:
    def __init__(self,order={},) -> None:
        self.order=order

    def taking_the_order(self):
        while True:
            picks=list(input('-----------------------------\ninsert the number of the item that you want ').split())
            print()

            for pick in picks:
                if pick not in ['1','2','3','4','5','6']:
                    continue
                self.order[menu_df.loc[pick]['foods']]={
                        'Price': menu_df.loc[pick]['prices'] * picks.count(pick),
                        'Quantity':picks.count(pick),
                }
            break

    def order_DF(self):
        return pd.DataFrame(self.order)


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
            self.total+=price['Price']

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
            self.Qnt+=i['Quantity']

        return self.Qnt

class Invoice:
    def __init__(self) -> None:
       self.takingorder=TakingOrder() 
       self.calculations=Calculations()

    def invoice_presentaion(self):

        print(f'{self.takingorder.order_DF()}\n---------------------------------------------')

        if self.calculations.quantity() >= 4:
            print(f'12% DISCOUNT GRANTED!')
            self.calculations.calc_total()
            print(f'Total: ${self.calculations.calc_discount()}')

        else:
            print(f'Total: ${self.calculations.calc_total()}')

        print(f'Fees: ${self.calculations.calc_fees()}\n---------------------------------------------')
        when=tm.localtime()
        Time=tm.strftime('%B %d/%Y %I%p:%M:%S', when )
        print(f'date of the order:\n{Time}')      

x=TakingOrder()
x.taking_the_order()

invoice=Invoice()
invoice.invoice_presentaion()
