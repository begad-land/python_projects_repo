
import random
import string

letters1=list(string.ascii_uppercase)

nums=['1','2','3','4','5','6','7','8','9']

for i in nums:
    letters1.append(i)

password=[]

for x in range(8):
    password.append(random.choice(letters1))

print(''.join(password))