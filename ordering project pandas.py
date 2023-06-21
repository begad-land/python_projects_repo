
import time
import pandas as pd

menu={

   'item':['black coffe','milk coffee','chicken sandwich','pepsi','hotdog'],   
   'price':[3.65 , 4.25 , 5.35 , 1.99 , 2.45 ],

    }

df_menu=pd.DataFrame(menu)

df_menu.index=[1,2,3,4,5]

print('------------------menu--------------------------')

print(f'{df_menu}\n-------------------------------------------------')

#collecting the data

order=input('\npick the number that corresponds to the item you want ').split()


items_chosen=[df_menu.loc[int(num)] for num in order ]

items_and_prices=[]

item_rep_and_price={}


for item_chosen in items_chosen:
    items_and_prices.append([item_chosen.loc['item'],item_chosen.loc['price']])


for data_from_items_and_prices_var in items_and_prices:
    item_rep_and_price[data_from_items_and_prices_var[0]] = [ (items_and_prices.count(data_from_items_and_prices_var)) , data_from_items_and_prices_var[1] ]



print('\n------------------order summary-----------------------\n')

#order summary

total=0
for item in items_chosen:
    total+=item.loc['price']
tax= total * 0.15  

if len(items_chosen) >= 4:
    #10% discount
    discounted_percentage= 10 / 100 * total

    for key, value in item_rep_and_price.items():
        print(f'item: {key} {value[0]}X | price: {value[1]}\n---------------------------------------------------')
   
    print(f'10% offer granted!\ntotal: {round(total - discounted_percentage,2)}\ntax: {round(tax,2)}$ ')


else:
    
    for key, value in item_rep_and_price.items():
        print(f'item: {key} {value[0]}X | price: {value[1]}$\n-------------------------------- ')
        
    print(f'total: {round(total,2)} \ntax: {round(tax,2)}$')

when=time.localtime()
print('----------------------------------------------------') 
Time=time.strftime('%B %d %Y %I%p:%M:%S', when )
print(f'date of the order:\n{Time}')
print('----------------------------------------------------')
