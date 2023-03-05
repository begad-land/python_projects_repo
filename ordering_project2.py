
dic={'1':'a',
     '2':'b',
     '3':'c',
     '4':'d'}




inp=None

collection=[]

while True:
    if inp!='q':
        inp=input('insert ')
        collection.append(dic[inp])
    else:
        print(collection)

    
    

