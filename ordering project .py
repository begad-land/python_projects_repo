import time
print('\nOFFER DAY!!\norder 4 items or more to get 10% off your order ')
menu={
    '1':{'item':'Black coffee', 
        'price':3.65 },

    '2':{'item': 'Milk coffee' ,
        'price':4.25 },

    '3':{'item' :'Chicken sandwich', 
        'price':5.35 },

    '4':{'item':'Pepsi', 
        'price':1.99 },
        
    '5':{'item':'Hotdog', 
        'price':2.45},

    '6':{'item': 'Lemonade', 
        'price': 1.36},

    '7':{'item':'Ice Cream', 
        'price':3.47},
    }
print('-------------------MENU---------------------------\n item                   price\n')

counter=1
for i in menu.values():
    print(f'| {counter}) {i["item"]:16} | {i["price"]:1}$ |')

    counter+=1
print('-----------------------------------------------')

class Check:
    def __init__(self,order,amount) -> None:
        self.order=order
        self.amount=amount

    def calc(self):
        total=0
        for v in self.order.values():
            total+=v[0]
        discounted_percentage= 10 / 100 * total
        tax= total * 0.15

        print('\n-------------------------order summary-----------------------\n')

        if self.amount >= 4:
            print(f'10% discount granted!\n')
            for key, value in self.order.items():
                print(f'Item: {key} {value[1]}X | Price: {value[0]}$\n----------------------------------------------')
            print(f'\nTotal: {round(total - discounted_percentage,2)}\nTax: {round(tax,2)}')

        else:
            for key, value in self.order.items():
                print(f'Item: {key} {value[1]}X | Price {value[0]}$\n----------------------------------------------')
            print(f'\nTotal: {round(total,2)}\nTax: {round(tax,2)}')
        print()
        when=time.localtime()
        print('----------------------------------------------------') 
        Time=time.strftime('%B %d %Y %I%p:%M:%S', when )
        print(f'date of the order:\n{Time}')
        print('----------------------------------------------------')
        


items=[]

cart={}

while True: 
    pick=list(input('\npick the number of the item u want (click enter to checkout) ').split())

    for i in pick:
      cart[menu[i]['item']]=[round(menu[i]['price'] * pick.count(i),2) ,pick.count(i)]  
      items.append(menu[i]['item'])
      
    break

order=Check(cart,len(items))
order.calc()