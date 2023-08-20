#this is temporary. if a user picks the same item more than once but with diffrent sizes try to append that items size inside the dict "cart"

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
print('====================MENU========================\n   item                 price\n')

counter=1
for pick in menu.values():
    print(f'| {counter}) {pick["item"]:16} | {pick["price"]:1}$ |')

    counter+=1
print('======================================================')

class Check:
    def __init__(self,order,items, items_and_sizes) -> None:
        self.order=order
        self.items=items
        self.items_and_sizes=items_and_sizes
        

    def calc(self):
        total=0
        for v in self.order.values():
            total+=v[0]
        discounted_percentage= 10 / 100 * total
        tax= total * 0.15

        print('\n=====================order summary=========================\n')

        if len(self.items) >= 4:
            print(f'10% discount granted!\n')
            for key, value in self.order.items():
                print(f'Item: {key:16} {value[1]}X | Price: {value[0]}$\n=========================================================')
            print(f'\nTotal: {round(total - discounted_percentage,2)}\nTax: {round(tax,2)}\n===================================')

        else:
            index=0
            for key, value in self.order.items():
                print(f'Item: {key:16} {value[1]:1}X | Price: {value[0]:7}$ | \n===========================================================')
                
            for i in items_and_sizes:
                print(f'\nitem: {i[0]:16} | size: {i[1]}\n---------------------------------------------------------')

            print(f'\nTotal: {round(total,2)}\nTax: {round(tax,2)}\n============================================================')
        print() 

        when=time.localtime()
        Time=time.strftime('%B %d %Y %I%p:%M:%S', when )
        print(f'date of the order:\n{Time}')
        print('=================================================')
        

items=[]

cart={}

while True: 
    picks=list(input('\npick the number of the item u want (click enter to choose the size you want) ').split())
    sizes=list(input('pick a size depending on the order of your items (L/M/S)').upper().split())

    for pick in picks:
      if pick not in menu:
          continue     
        
      cart[menu[pick]['item']] = [round(menu[pick]['price'] * picks.count(pick),2) , picks.count(pick),  ]

      items.append(menu[pick]['item'])
    break

items_and_sizes=zip(items,sizes)

order=Check(cart,items, items_and_sizes)
order.calc()