#시간 에러..?
temp = []
move=0
for i in range(len(moves)):
    for j in range(len(board)):
        move=moves[i]-1
        if board[j][move]!=0:
            temp.append(board[j][move]) #인형 바구니에 넣기
            board[j][move]=0
            break


result=len(temp) #빼지 않은 상태에서 배열의 길이 체크
print(temp)

# 같은 인형 제거 시작!!!
i=0
while i<len(temp)-1:    
    if temp[i]==temp[i+1]:  #만약 위아래가 같으면 제거
        temp.remove(temp[i])
        temp.remove(temp[i])
        i=-1
    i+=1
print(temp)


print(result-len(temp))  #위에서 총길이구한거에서 뺀 인형의 배열의 길이



#2번째
def solution(board, moves):
    
    temp = [-1] #temp에 기본값
    move=0      #moves를 위해 만든 변수
    count=0     #사라진 인형 수
    
    for i in range(len(moves)):     #인형뽑기 순서
        for j in range(len(board)): #인형확인
            move=moves[i]-1         #배열은 0부터라서 -1
            if board[j][move]!=0:   #0이 아니면 인형가져오기
                if temp[-1]== board[j][move]: #temp(바구니) 맨 위 인형이 가져올 인형과 같으면
                    temp.pop()                 # 맨위에 인형 빼기
                    count+=1                    # 뺀 인형이 몇개인지 세는 변수
                else : temp.append(board[j][move]) #만약 인형이 같지 않으면 인형 넣기
                    
                board[j][move]=0                    #인형 뽑으면 0으로 채우기
                break               
                
    return count*2    
