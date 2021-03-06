#스파이의 옷 조합 수
#의상수 1~30개
#옷이름의 길이는 20이하 
#스파이는 하루에 최소 한개이상.....? 

#일단 종류별로 가짓수 구하기
#뒤에 곱하기..
#종류별 가짓수를 딕셔너리로..?



from itertools import combinations
def solution(clothes):
    if len(clothes)<1:
        return 1
    answer = len(clothes) #옷 하나만 입었을 때 가지수로 
    result=[]
    comb=[]
    sum =1

    sort_clothes = sorted(clothes, key = lambda x : x[1]) # 옷별로 정렬

    sort_clothes.append(["d","d"]) #뒤에 for문을 위해서 쓰레기문자 입력

    for i in range(len(sort_clothes)-1):
        if sort_clothes[i][1] != sort_clothes[i+1][1]: #배열의 앞뒤가 다르면 다른 종류의 옷으로 생각
            result += [str(sum)+ sort_clothes[i][1]] #가지수+옷종류 문자로 해서 결과배열에 추가
            sum=0 #옷 가지수 초기화
        sum+=1 # 앞뒤 같으면 가지수 하나 추가


    #조합수
    for i in range(2,len(result)+1): #조합 수 따지기
        comb += list(combinations(result,i)) #조합테이블로 추가

    print(comb)


    #곱셈
    for i in range(len(comb)): 
        sum=1
        for j in range(len(comb[i])):
            sum *= int(comb[i][j][0])
            
        answer+=sum
    

    return answer



solution([["yellow_hat","headgear"], ["blue_sunglasses","eyewear"], ["green_turban","headgear"],["crow_mask", "face"], ["blue_sunglasses", "face"],["crow_mask", "facebook"], ["blue_sunglasses", "facebook"]])