from keyboard import*
from random import*
from module1 import*
def start():
    print("Kivi,Käärid,Paber")
    m=3
    while m not in [1,2]:
        try:
            m=int(input("Kellega mängime?\n1-botid \n2-robotid "))
        except:
            ValueError
    return m
v1=["Kivi","Käärid","Paber"]
v2=["Kivi","Käärid","Paber"]
m=start()
if m==1:
    bot_vs_bot(v1,v2)
elif m==2:
    while 1:
        pass
