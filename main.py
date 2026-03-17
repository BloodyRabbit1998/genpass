import random

alphabet="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

n=int(input("Введите длину пароля: "))
password=''
for i in range(n):
    password+=random.choice(alphabet)
print(password)
