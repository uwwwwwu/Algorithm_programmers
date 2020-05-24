#예산
#부서별 물품 금액조사
#최대한 많은 부서의 물품
# d = 부서별 신청 금액 (1~100/최대100000원씩)
# budget= 총예산(1~10000000)
#순서 정렬 후 ~~~
def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        answer += d[i]
        if answer > budget:
            return i
    return len(d)


solution([1,3,2,5,4],9)