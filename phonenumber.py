#1. 하나의 번호가 다른 번호의 앞에 있으면 false
# *전화번호는 총 1,000,000개 있음
# *전화번호 길이는 총 20이하 
# 해시함수는 임의의 길이의 데이터를 입력받아 일정한 길이의 비트열로 반환 시켜주는 함수

# 일단 string으로 정렬하면 앞에서부터 정렬됨
#  


def solution(phone_book):
    answer = True

    phone_book.sort()
    print(phone_book)

    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            print(False)
            return False
    print(answer)
    return answer


solution(["119", "97674223", "1195524421"])
solution(["123","456","789"])
solution(["12","123","1235","567","88"])
