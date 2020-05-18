# 앞뒤 번호에게만 빌려줄수있음
# 전체학생 = n (2~30)
# 도난당한 학생들의 번호  = lost (1~ n)
# 여벌의 체육복 = reserve (1~ n)

# 결과는 수업들을 수 있는 최대 학생 수

#set으로 만들고 최종본 만들기
# 앞뒤 확인 후 분배
# -> 실패 (앞에서부터 확인해도될듯)
#앞 살피고 뒤 살피고 쭈우우우ㅜ욱

def solution(n, lost, reserve):
    
    T_reserve = set(reserve) - set(lost) #체육복 빌려줄 수 있는 사람
    lost = set(lost) - set(reserve) # 잃어버린 사람

    
    for i in T_reserve: #1,3,5
        if i-1 in lost: #0,2,4    이런식으로 in을 쓰면 안에 들어가게 됨 먼저 앞부터 보기
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)

    return n-len(lost)



#solution(9,[2,3,4],[1,3,5])

#틀림 완전히 새롭게 풀자
def solutionn(n, lost, reserve):
    answer = [0]*(n+2) # 앞에 한칸 뒤에 한칸
    T_reserve = set(reserve) - set(lost) #체육복 빌려줄 수 있는 사람
    lost = set(lost) - set(reserve) # 잃어버린 사람
    count=0
    for i in T_reserve: #앞뒤로 +1해주기
        answer[i-1] += 1
        answer[i] = 5
        answer[i+1] += 1
        
    answer =[0]+answer[1:-1]+[0] # 앞뒤값 0으로 초기화
    print(answer)
    for i in range(1,len(answer)-1):
        if  answer[i] ==(1 or 2) and answer[i-1]==(5 or 6):
            answer[i]=8
            answer[i-1]=8
            answer[i-2] -= 1
            count+=1
            print(answer)
        elif answer[i] ==(1 or 2)  and answer[i+1]==(5 or 6):
            answer[i]=8
            answer[i+1]=8
            answer[i+2] -= 1
            count+=1
            print(answer)

    #[5,5,5... 인경우 못함 안해]
    return count + n-len(lost)


solutionn(5,[2,4],[1,3,5])