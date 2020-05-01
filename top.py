#왼쪽으로 갔을때 자신보다 큰 수 있으면 리턴 없으면 0
#for문 반대로 돌려서 생각
# 4,3,2,1,0순으로 탐색해서 자신보다 크면 반환


def solution(heights):
    answer = [0]*len(heights)

    for i in range(len(heights)-1,0,-1): #-1씩 줄어들고 마지막부터 두번째꺼까지 (첫번째꺼 x)
        for j in range(i-1,-1,-1):
            if heights[i]<heights[j]:
                answer[i]=j+1
                break

    print(answer)    
   
        
    return answer


solution([6,9,5,7,4])