import random
a=int(input("사람수:"))
b=random.randint(1,a)
c=[]
for i in range(1,a+1):
    d=input("{}번 이름:".format(i))
    if i==b:
        print("{}번 당첨".format(i))
        break














