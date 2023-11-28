
# sourcery skip: for-append-to-extend, simplify-generator
import random
import string
import time
import re

letters1=list(string.ascii_uppercase)

nums=['1','2','3','4','5','6','7','8','9']

symbols=['@','$','&','*','#']


pattern=re.compile(r'[0-9]+[A-Z]+[@#%&*]{1,4}')

while True:
    for i in nums:
        letters1.append(i)

    for symbol in symbols:
        letters1.append(symbol) 

    password = [random.choice(letters1) for x in range(9)]
    password=''.join(password)

    if pattern.search(password) is None:
        continue

    print(password)    
    time.sleep(6)
