import webbrowser
list1 = ["https://www.google.com/webhp?hl=ko&ictx=2&sa=X&ved=0ahUKEwjJu4HWjYn1AhVEsFYBHbT3DVQQPQgI",
"https://www.naver.com/",
"https://www.inflearn.com/"]
while (True):
    a=str(input("가고싶은 사이트 이름을 입력: "))
    if a=="구글":
        webbrowser.open(list1[0])
        break
    elif a=="네이버":
        webbrowser.open(list1[1])
        break
    elif a=="인프런":
        webbrowser.open(list1[2])
        break
    else :
        print("다시 입력해주세요")
        continue

