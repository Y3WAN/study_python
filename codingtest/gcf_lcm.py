#최대공약수와 최소공배수
def solution(n, m):
    answer = []
    for i in range(min(n,m),0,-1):
        if n%i==0 and m%i==0:
            answer.append(i)
            break
    for w in range (max(n,m),(n*m)+1):
        if w%n==0 and w%m==0:
            answer.append(w)
            break
    return answer