#n*n지도
# 비트 연산자
# 나눗셈 출력..?


def solution(n,arr1,arr2):
    answer = []

    result=[]
 
    for i in range(n):
        answer.append(arr1[i] | arr2[i]) # 최종 지도


    # 이진법 표현
    for i in range(len(answer)):
        data = ""
        while(answer[i] != 0): # 0이면 " "
            if answer[i]%2==0:
                data = " " + data
                answer[i] = answer[i]//2
            else:               # 1이면 "#"
                data = "#" + data
                answer[i] = answer[i]//2
        
        data = (" "*n) +data       # 1인 경우 대비하여 
        result.append(data[-n:])   # 개수만큼 자르기
    return result



solution(5,[9,20,28,18,11],[30,1,21,17,28])