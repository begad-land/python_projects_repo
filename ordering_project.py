
print('OFFER DAY!!\norder more than 3 items and get a 5$ discount ')


print()
print('__________Menu_____________')
print('   items        price')
menu={
    1:{'item':'black coffee', 'price':3 },
    2:{'item': 'milk coffee' , 'price':4 },
    3:{'item' :'chicken sandwich', 'price':5 },
    4:{'item':'pepsi', 'price':2 }
    }

for i,y in menu.items():
    print(f'{i}.{y["item"]} | {y["price"]}$')

class Check:
    def __init__(self,order,calculate) -> None:
        self.order=order
        self.calculate=calculate

    def calc(self):

    
        total=0
        for i in self.calculate :
            total+=i
        tax = total * 0.12

        if len(self.order) > 3: 
            discount=total-5
            print('for ordering more than 3 items you get a 5$ discount')

            for i in self.order:
                print(f'your order: {i["item"]}| price: {i["price"]}$', end='   ' )
            print()
            print(f'your total: {total}$\nafter the discount {discount}$ ')
            print(f'the tax for your order is {round(tax,2)}$')

        else:
         
            for i in self.order:
                print(f'your order: {i["item"]}| price: {i["price"]}$', end='   ' )
            print()    
            print(f'total: {total}$')
            print(f'the tax for your order is {round(tax,2)}$')


prices=[]

pick=None

all=[]

x=None

while x!='q' :
    pick=menu[int(input('pick a number that corresponds with the item you would like to order '))]
    all.append(pick)
    prices.append(pick['price'])
    x=input('insert q to quit ')

order=Check(all,prices)
order.calc()
