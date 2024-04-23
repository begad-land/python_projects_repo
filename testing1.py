
lst = [7,2,1,5,6,9]

new_list = []

smallest = lst[1]
index = 0
num = lst[index]

for i in range(len(lst)):
    if smallest > num:
        smallest = num
        lst.remove(smallest)
        new_list.append(smallest)
        
        i = 0
        index = 0
        num = lst[index]
        smallest = lst[1]
        continue
       
    index+=1
    num = lst[index]
        

print(smallest)
          
