# 재귀
def solution(n):
    n -=1
    item = "124"
    i, j = divmod(n, 3)
    if i == 0:
        return item[j]
    else :
        return solution(i) + item[j]

solution(1)
solution(2)
solution(3)
solution(4)
solution(5)
solution(6)
solution(7)
solution(8)
solution(9)
solution(10)
solution(11)


