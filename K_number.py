#1. 배열의 i~j번째 숫자 정렬
#2. k번째 수 구하기
#3. 1,2 단계 최대 50번 반복 후 배열로 출력



def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        test=array[commands[i][0]-1:commands[i][1]]
        test.sort()
        answer.append(test[commands[i][2]-1])
        test.clear()

    return answer


solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])