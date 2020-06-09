#1초에 1만큼 움직임
#bridge_length 다리길이 (1~1000)
#weight 견디는 무게 (트럭이 완전히 올라가면 무게재기) (1~1000)

#다리길이 = max count
#무게 = max sum
#answer = 총 시간
# 1. sum에 무게 넣기
# 1.1 count에 개수 넣기
# 둘다 max에 걸리면 time 추가


def solution(bridge_length, weight, truck_weights):
    sum = 0 #다리에 올라가는 총 무게 
    count = 0 #다리에 올라가는 총 트럭의 수
    answer = 0 #총 시간
    new_truck = [] # 2차원 배열을 위한 배열

    for i in range(len(truck_weights)): #2차원 배열로 만들기
        new_truck += [[truck_weights[i],bridge_length]]
    
    i = 0 #이거 안하면 위에 i가 적용됨
    
    while 1 :
        if new_truck[0][1] == 0: #뒤에꺼가 0이면 나가기
                sum -= new_truck[0][0] 
                count -= 1
                new_truck.pop(0)
                i -= 1 #pop했으니 -1
        
        if (sum + new_truck[i][0]) <= weight and (count + 1 ) <= bridge_length: # 여유되면 추가
                sum += new_truck[i][0] #무게 추가
                for k in range(0,i+1): #다리위에 있는 트럭들 다 -1시키기
                    new_truck[k][1] -= 1 
                count += 1
                answer += 1
                i += 1 #다음 트럭 가리키기

        else :
            answer +=1 #시간 1초 지남
            for k in range(0,i): #다리위에 있는 트럭들 다 -1시키기
                new_truck[k][1] -= 1 
            
        if len(new_truck) == i: #만약에 모든 트럭이 다리 위에 있다면
            answer += new_truck[i-1][1] # 뒤에 시간만큼 추가
            break # 무한루프 빠져나감
    
    return answer+1 #pop을 위에서 했기때문에 1추가


solution(2,10,[7,4,5,6])


