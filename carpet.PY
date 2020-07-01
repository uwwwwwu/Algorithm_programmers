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
    return [x,y]


solution(10,2)

#한줄도 가능ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
def solution(brown, yellow):
    return [int(((brown/2 +2)+((((brown/2 +2)**2) - (4*(brown + yellow)))**0.5))/2),int((brown/2 +2) - (int(((brown/2 +2)+((((brown/2 +2)**2) - (4*(brown + yellow)))**0.5))/2)))]