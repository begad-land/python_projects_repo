
# sourcery skip: for-append-to-extend, simplify-generator
import random
import string
import time

letters1=list(string.ascii_uppercase)

nums=['1','2','3','4','5','6','7','8','9']

symbols=['@','$','!','&','*']

while True:
    for i in nums:
        letters1.append(i)

    for symbol in symbols:
        letters1.append(symbol)    
    
    password = [random.choice(letters1) for x in range(8)]

    for i in symbols:
        if i not in password:
            continue
        
    print(''.join(password))
    time.sleep(6)
