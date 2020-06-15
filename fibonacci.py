# 0 , 1 , 1 , 2 , 3 , 5, 8, 13, 21
#def solution(n):
#    answer=[0,1]
#    for i in range(1,n):
#        n=answer[i-1]+answer[i]
#        answer.append(n)
#    return answer[i+1]%1234567


def solution(n):
    a=0
    b=1
    for i in range(1,n):
        c=a+b
        a=b
        b=c
    return c%1234567