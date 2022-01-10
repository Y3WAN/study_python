# list=['d','c','a','b']
# list.reverse()
# print("리스트 항목 뒤집기",list)
# list.sort()
# print("리스트 항목 정렬하기",list)
# list.sort(reverse=True)
# print("리스트 항목 역정렬하기",list)
# for index,value in enumerate(list):
#     print("인덱스",index,"위치의 값은",value)

#import random 
# def rolling_dice(pip):
#     n=random.randint(1,pip)
#     print(pip,"면 주사위 굴린결과:",n)

# rolling_dice(4)

# import random 
# def rolling_dice(pip,repeat):
#     for r in range(1,repeat+1):
#         n=random.randint(1,pip)
#         print(pip,"면 주사위 굴린결과",r,":",n)

# rolling_dice(6,1)
# rolling_dice(6,2)
# rolling_dice(6,0)

# def p(*args):
#     str=""
#     for a in args:
#         str=str+a
#     print(str)

# p("!@#$%^&*")
    
# def hello(msg="안녕하세요"):
#     print(msg+"!")

# hello("오랜만이에요")

# def sum(*numbers):
#     sum_value=0
#     for number in numbers:
#         sum_value+=number
#     return sum_value

# resuit=sum(1,3)
# print("1+3=",resuit)
# print("1+3+5+7=",sum(1,3,5,7))

# def multi_num(multi,start,end):
#     resuit=[]
#     for n in range(start,end):
#         if n%multi == 0:
#             resuit.append(n)
#     return resuit
# multi2=multi_num(17,1,200)    
# print("multI_num(17,1,200):",multi2)







