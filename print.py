def solution(priorities, location):
    
    answer=priorities #복사
    result = priorities[location] #내 프린터 우선순위
    count = 0 #몇번째인지
    if max(priorities)==result: #max 값이면
        countarr=priorities[0:location+1]#몇번있는지 확인
        return countarr.count(result)
        
    
    for i in range(len(priorities)):#나보다 우선순위 쎈거
        if priorities[i]>result:
            count += 1

    
    num = len(priorities)-1
    
    for i in range(9,result,-1):
        for j in range(num,num-len(priorities),-1):
            if answer[j]==i:
                    num= j
                    if num <0:
                        num += len(priorities)
                    break;

    while 1 :
        if num <0:
            num += len(priorities)
        else: 
            break
        
    if num <location:
        countarr=answer[num:location]
    else :
        countarr= answer[num:]+ answer[:location]
    
    print(countarr)

    return count+countarr.count(result)+1

solution([2,1,3,2,3,2,2,7,5,3,3,2,1],3)