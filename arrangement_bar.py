# n+1개로 나뉨
# start, end로 나눠서 ()의 개수세고 +1... 이런식
def solution(arrangement):
    answer = []
    count = 0
    end = 0
    result =0
    
    for start in range(len(arrangement)):
        end=(start+1)
        if arrangement[start]== "(":
            answer.append(arrangement[start])
        
        while len(answer) and (start != (len(arrangement)-1)): # 0이 아닐때 돌아가기
            
            if arrangement[end-1]+arrangement[end]== "()": # ()의 개수 세기
                count += 1
                

            if arrangement[end]==")":
                answer.pop()
            else : 
                answer.append(arrangement[end])
            
            end +=1
            
            
        
        result += (count+1)
        count = 0
        
    return result

#solution("(())")
solution("(((()())(())()))(())")



#위에꺼 대실패
# n번 자르면 n+1개로 나뉨 
def solution(arrangement):

    bar = 0  # 내 막대기
    result = 0 #자른 막대기
    arrangement = list(arrangement) #pop에서 error

    while arrangement:
        if arrangement[0] =="(": 
            bar += 1                    #막대기개수
            arrangement.pop(0)
            if arrangement[0]== ")":    #()이런거 제거
                bar -= 1
                result += bar            #잘랐으니깐 결과 +1
                arrangement.pop(0)       #없애
        else : 
            arrangement.pop(0)          # ) 이거나오면 없애
            bar -= 1                    # 다 자른거니깐 bar -1
            result += 1                 #끄트머리 +1


    
    print(result)
    return result


solution("()(((()())(())()))")