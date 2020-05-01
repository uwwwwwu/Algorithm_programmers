#스파이의 옷 조합 수
#의상수 1~30개
#옷이름의 길이는 20이하 
#스파이는 하루에 최소 한개이상.....? 

#일단 딕셔너리로 옷종류별 갯수 정리
#조합함수쓰기


from itertools import combinations
def solution(clothes):
    answer = len(clothes)
    result=[]
    comb=[]
    sum =1

    sort_clothes = sorted(clothes, key = lambda x : x[1])

    sort_clothes.append(["d","d"])

    for i in range(len(sort_clothes)-1):

        if sort_clothes[i][1] != sort_clothes[i+1][1]:
            result += [str(sum)+ sort_clothes[i][1]]
            sum=0
        sum+=1


    #조합수
    for i in range(2,len(result)+1):
        comb += list(combinations(result,i))

    
    #곱셈
    for i in range(len(comb)):
        sum=1
        for j in range(len(comb[i])):
            sum *= int(comb[i][j][0])
        answer+=sum
    
  
    return answer



solution([["yellow_hat","headgear"], ["blue_sunglasses","eyewear"], ["green_turban","headgear"],["crow_mask", "face"], ["blue_sunglasses", "face"]])