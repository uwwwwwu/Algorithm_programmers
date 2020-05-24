#기능 개발
#한번에 배포되는 기능 수
#progresses = 프로그램 작업 진도
# speeds = 작업 속도

# time = (100 - progre[0])/speeds[0])+(100 - progre[0])%speeds[0]) 삼항연산자?
# for 문으로 전체 읽고 100넘으면 출력?


def solution(progresses, speeds):
    
    answer = []
    time = ((100 - progresses[0])//speeds[0])+ (1 if (100 - progresses[0])% speeds[0] else 0) # 처음 기능을 몇분 해야되는 지
    timesum = time # 총 시간
    count = 1
    
    for i in range(1,len(progresses)):
        progresses_sum = (speeds[i]*timesum) + progresses[i] # 현재 작업 진도
        
        if progresses_sum >= 100 : # 100이 넘으면
            count += 1
            
        else :
            answer.append(count) # 그 전 기능의 개수 append
            time = ((100 - progresses_sum)//speeds[i])+ (1 if (100 - progresses_sum)% speeds[i] else 0) # 몇 분 해야되는 지 time
            timesum += time # 총 시간
            count = 1
   
    answer.append(count)     # 마지막으로 append
        
    return answer

solution([93,90,55,45,45],[2,30,5,5,5])