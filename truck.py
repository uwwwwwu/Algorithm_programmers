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
    sum = 0
    count = 0
    answer = 0
    new_truck = []

    for i in range(len(truck_weights)): #2차원 배열로 만들기
        new_truck += [[truck_weights[i],bridge_length]]
    
    i = 0
    
    while 1 :
        if new_truck[0][1] == 0: #뒤에꺼가 0이면 나가기
                sum -= new_truck[0][0]
                count -= 1
                new_truck.pop(0)
                i -= 1
        
        if (sum + new_truck[i][0]) <= weight and (count + 1 ) <= bridge_length: # 여유되면 추가
                sum += new_truck[i][0]
                for k in range(0,i+1):
                    new_truck[k][1] -= 1 
                count += 1
                answer += 1
                i += 1 

        else :
            answer +=1
            for k in range(0,i):
                new_truck[k][1] -= 1 
            

        if len(new_truck) == i:
            answer += new_truck[i-1][1]
            break
    
    return answer+1


solution(2,10,[7,4,5,6])


