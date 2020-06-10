# n은 500000000이하의 자연수
# 3곱하기 n으로 나누기 => 몇자리 수인지 (3,9,27..)
# 자리값에서 나올수 있는 숫자 배열 % 나머지
from itertools import product

def solution(n):
    i = 1 
    num = 1 #몇자리 수인지
    item = [1,2,4]

    if n==1 or n==2 or n==3:
        return str(item[n-1])

    while 1:
        if n-(i*3) <= 0:
            break  
        else :
            n -= (i*3) 
            i *= 3
            num += 1

    answer = str(list(product(item,repeat= num))[n-1])
    print(answer.replace(', ','')[1:-1])
    
    return answer



solution(1)

#시간에러 3진법으로 풀자 -> 재귀
def solution2(n):
    n -=1
    item = "124"
    i, j = divmod(n, 3)
    if i == 0:
        return item[j]
    else :
        return solution(i) + item[j]