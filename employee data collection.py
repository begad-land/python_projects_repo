
import random as rn

names=[]
positions=[]
employees={}
index=0

while True: 
    name=input('insert the name of the employee ')
    names.append(name)

    if name=='':
        break

    position=input('insert the employees position ( ')
    positions.append(position)
    print('----------------------------------------------------------------')
    
names.remove('')

for i in range(len(names)):
    id=rn.randint(1000,9999)
    employees[id]=[names[index],positions[index]]
    index+=1


#with open('test.txt','r+') as file:
    #for k, v in employees.items():
        #file.writelines(f'\nID:{k}\nName: {v[0]}\nPosition: {v[1]}\n-----------------------------------------')


