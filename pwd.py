import random 
from time import sleep


no=[6,7,8,9]
char=["!","@","#","$","%","^","&","*","=","+","-"]
print("Welcome to Gitesh6432 password genrator")

Ft=input("Enter your Favourite Thing : ")


r=random.choice(Ft)
Ft=Ft.replace(r,r.upper())

rn=random.randint(1000,9999)
rc=random.choice(char)
final=Ft+rc+str(rn)


print(final)