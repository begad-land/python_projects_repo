import time

import pandas as pd

menu={

   'item':['black coffe','milk coffee','chicken sandwich','pepsi','hotdog'],
   'price':[3.65 , 4.25 , 5.35 , 1.99 , 2.45 ]

    }

df_menu=pd.DataFrame(menu)

df_menu.index=[1,2,3,4,5]


print(f'{df_menu}\n-------------------------------------------------')

#collecting the data

order=input('pick the number that corresponds yo the item you want ').split()


items_chosen=[df_menu.loc[int(num)] for num in order ]

items=[]

reps={}


for i in items_chosen:
    items.append([i.loc['item'],i.loc['price']])

print(items)
    


for amount_of_reps in items:
    reps[amount_of_reps[0]]=[(items.count(amount_of_reps)),amount_of_reps[1]]

print(reps)
    

items_price={}


print('\n------------------order summary-----------------------\n')


total=0
for item in items_chosen:
    total+=item.loc['price']
tax= total * 0.15

if len(items_chosen) >= 4:

    discounted_percentage= 10 / 100 * total

    index=0
    for key, value in reps.items():
        print(f'item: {key} {value[0]}X | price: {value[1]}\n----------------------------- ')
   
        index+=1

    print(f'10% offer granted!\ntotal: {round(total - discounted_percentage,2)}\ntax: {round(tax,2)} ')

else:
    acounted_for=[]
    index=0
    
    for key, value in reps.items():
        print(f'item: {key} {value[0]}X | price: {value[1]}\n-------------------------------- ')
        acounted_for.append(item[0])
        index+=1
        

    print(f'total: {round(total,2)} \ntax: {round(tax,2)}')

when=time.localtime()
print('----------------------------------------------------') 
Time=time.strftime('%B %d %Y %I%p:%M:%S', when )
print(f'date of order\n{Time}')
print('----------------------------------------------------')

