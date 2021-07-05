import random
a=int(input("enter the number of people : "))
b=[]
for i in range(a):
    c=input()
    b.append(c)
print("Participants",b)
print("winner : ",random.choice(b))
