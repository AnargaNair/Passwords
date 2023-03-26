import random

chars="qwertyuiopasdfghjklzxcvbnm_!@#-"

amount=input("Amount:")
amount=int(amount)

length=input("Length:")
length=int(length)

for pwd in range(amount):
    passwords=" "
    for i in range(length):
        passwords += random.choice(chars)
    print(passwords)
