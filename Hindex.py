# 과학자의 생산성, 영향력 지표

# 논문 n편 h번이상 인용된 논문이 h편 이상, 나머지 논문이 h번 이하 인용되었다면 h의 최댓값
# 논문 수(1~1000), 인용 횟수(0~10000)

# [a,b,c,d,e] = 논문은 5개, 각각 인용된 수


def solution(citations):
    citations.sort(reverse=True)
    citations +=[0]
    answer = 0

    for i in range(1, len(citations)+1):
        if citations[i-1]>=i and citations[i] <= i:
            answer = i

    return answer



solution([3,0,6,1,5])
