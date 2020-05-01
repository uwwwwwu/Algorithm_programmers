#x부터 x씩 증가 하는 n개의 숫자..?
#ex) x, 2x, 3x, 4x

def solution(x,n):
    answer = []
    for i in range(n):
        answer.append(x*(i+1))
    return answer

def idea(x,n): #1,3인 경우
    print(range(n)) #range(0,3)
    print(list(range(n))) #[0,1,2]
    print(list(range(1,n))) #[1,2]
    print(list(range(1,n*x+1,x))) #[1,2,3]
    print([0]*2)
    return 0

#range(x,n*x+1,x)) -> range(x,(n+1)*x,x)) 마이너스인 경우는 안됨
#테스트 8에서 에러남 => 아마 x가 0인 경우인듯 

def fsolution(x, n):
    if x==0 : return [0]*n
    return list(range(x,(n+1)*x,x))

solution(1,2)
idea(1,3)