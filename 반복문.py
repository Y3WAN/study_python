#for
'''
for x in range(3,9,2):
    print(x)

for ch in "LOVE":
    print(ch)

for itme in ["힙합","발라드"]:
    print(itme+"즐겨듣는다")

for itme in (2560,1440):
    print(itme)

pl={"C":1972,"java":1995,"python":1991}
for key in pl:
    print(key,":",pl[key])

for itme in {"HTML5","CSS3","javaScript"}:
    print(itme+"를 할수있다")

for i in range(1,9+1):
    print("2*{}={}".format(i,i*2))

for i in range(1,9+1):
    print("3*{}={}".format(i,i*3))

for i in range(1,9+1):
    print("4*{}={}".format(i,i*4))

for i in range(1,9+1):
    print("5*{}={}".format(i,i*5))

for dan in range(2,5+1):
    for i in range(1,9+1):
        print("{}*{}={}".format(dan,i,dan*i))
    print("-----------")

table=[["월","화","수"],[100,200,300]]
for row in table:
    for col in row:
        print(str(col)+" ")
    print()

for i in range(1,9+1):
    if i==7:
        break
    print("2*{}={}".format(i,i*2))

for i in range(1,9+1):
    if i%2==0:
        continue
    print("2*{}={}".format(i,i*2))

array=[]
for i in range(1,10,2):
    array.append(i*i)

array=[i*i for i in range(1,10,2) if i*i > 30]

x=3
while x<6:
    print(x)
'
x=3
while x<6:
    print(x)
    x+=1

eaho =input()
while (True):
    if eaho=="exit":
        break
    print(eaho)
    eaho=input()
'''