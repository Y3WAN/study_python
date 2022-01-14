def solution(n):
    answer = ''
    a="수"
    for i in range(1,n+1):
        if i%2==0:
            answer+="박"
        else:
            answer+=a
    return answer