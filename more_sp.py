# k이상 스코 음식으로 만들고 싶음
# 섞.스코 = 가장 덜매운  스코 + (두번째 덜매운 *2)
# 섞어야하는 최소 횟수 return (못만들면 -1)
# 스코빌 길이 = 2~1000000, k는 0~1000000000, 스코빌원소=0~1000000

# 1. 처음에 오름차 순으로 정렬
# 2. 가장 앞에꺼가 k보다 작으면 돌아가기 -> 그렇지 않으면 return
# 3. 0,1번이 섞어지면 버블 정렬로 다시 정렬
# 4. 2-3반복
# 5. 갯수가 2개 이면서 0번째가 k보다 작으면 섞는 계산 후해봄 
#        -> 만약에 k보다 작으면 -1 return 
from collections import deque

def solution(scoville2, K):
    scoville2.sort()
    scoville = deque(scoville2)
    answer = 0

    while 1:
        if scoville[0] < K:
            if len(scoville)==2 :
                if scoville[0]+(scoville[1]*2)<K:
                    return -1
                else:
                    return answer+1
                    
            scoville[1] = scoville[0]+(scoville[1]*2)
            scoville.popleft()
            #버블 정렬
            i=0
            for i in range(len(scoville)-1):
                if scoville[i]>scoville[i+1] :
                    scoville[i], scoville[i+1] = scoville[i+1], scoville[i]
                else:
                    break
                
            answer += 1

        else : 
            return answer
    


solution([1,2,3,9,10,12],7)