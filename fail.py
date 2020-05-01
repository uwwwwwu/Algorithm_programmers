#맨위 여섯줄은 => 실패율 구하자
#실패율 = 스테이지 클리어못함/스테이지 도착플레이어수
# N = 전체 스테이지 수        (1~500)
# stages = 현재 스테이지 번호(배열)  ex)[2,3,2,2]   (200000명 이하)
#           500스테이지 => 501번째 스테이지는 다 한사람
# 결과 = 실패율 높은게 제일 앞 쭉쭈꾸ㅉ꾸쭈꾺 (만약 같으면 작은 번호 우선)


# 1,2,2,2,3,3,4,6            8명
# 1 - 1/8                    1의 개수/총인원 
# 2 - 3/(8-1)                2의 개수/총인원- 1의 개수
# 3 - 2/(8-4)                3의 개수/총인원- 1,2의 개수

# 각각 단계에 몇명 있는지 구하고 빼기 
# count는 시간복잡도면서에서 안쓰는걸로
#                                (Counter import해도 됨) 
#                                 ex) from collections import Counter
#                                     Counter(stages)

#딕셔너리 정렬 후 예전 준호 오빠 방식으로 정렬 끝!


def solution(N, stages):
    answer=[]
    dic={}
    num=1
    sum=0
    stages.sort()
    stages.append(-1) #배열길이 늘려줌(마지막값 가지기 위해)

    #개수세기부터 [몇단계   ,    2의 개수   ,   1,2의개수 합]
    for i in range(len(stages)-1):
        if stages[i] != stages[i+1]:
            answer += [[stages[i],num,sum]] #이중배열
            sum+=num
            num=0
        num+=1

    #딕셔너리로 정리 해보고 싶음
    for i in range(N):
        dic[i+1]=0.0

    #실패율 데이터 넣기
    for i in range(len(answer)):
        if answer[i][0] != N+1:
            dic[answer[i][0]]= (answer[i][1])/(len(stages)-answer[i][2]-1)
    

    return list(dict(sorted(dic.items(),key=lambda x: x[1],reverse=True)).keys())

solution(5,[2,1,2,6,2,4,3,3])
solution(4,[4,4,4,4,4])


