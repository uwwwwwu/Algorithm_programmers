#def solution(n):
#    # 1부터 n사이의 소수는 몇 개인가요?
#    answer = set(range(2,n+1)) #2~n까지 집합
#    print(answer)
#    answer = answer - set(range(2,n+1,2))
#                    - set(range(3,n+1,3))
#                    - set(range(4,n+1,4))
#    return 0

def solution(n):
    # 1부터 n사이의 소수는 몇 개인가요?
    answer = set(range(2,n+1)) #2~n까지 집합
    num =0
    for i in range(2,n+1):
        if i in answer:
            answer -=set(range(i,n+1,i))
            num +=1

    
    return len(answer)+num






# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(10))