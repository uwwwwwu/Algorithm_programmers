#스파이의 옷 조합 수
#의상수 1~30개
#옷이름의 길이는 20이하 
#스파이는 하루에 최소 한개이상.....? 

#수학공부 완료
#각 옷종류에 안입은 경우를 +1하여 그냥 다 곱하기


def solution(clothes):
    if len(clothes)<1:
        return 1
   
    result=1
    sum =1

    sort_clothes = sorted(clothes, key = lambda x : x[1]) # 옷별로 정렬

    sort_clothes.append(["d","d"]) #뒤에 for문을 위해서 쓰레기문자 입력

    for i in range(len(sort_clothes)-1):
        if sort_clothes[i][1] != sort_clothes[i+1][1]: #배열의 앞뒤가 다르면 다른 종류의 옷으로 생각
            result *= (sum+1) #종류별 옷 개수 곱하기 
            sum=0 #옷 가지수 초기화
        sum+=1 # 앞뒤 같으면 가지수 하나 추가



    return result-1 #모두 안입는 경우 빼기



solution([["yellow_hat","headgear"], ["blue_sunglasses","eyewear"], ["green_turban","headgear"],["crow_mask", "face"], ["blue_sunglasses", "face"],["crow_mask", "facebook"], ["blue_sunglasses", "facebook"]])