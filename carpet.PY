# 행을 x, 열을 y
# A = x + y
# B = xy
# c = x - y
def solution(brown, yellow):
    a = brown/2 +2
    b = brown + yellow
    c = ((a**2) - (4*b))**0.5
    x = int((a+c)/2)
    y = int(a - x)
    answer = [x,y]
    print(answer)
    return answer


solution(10,2)