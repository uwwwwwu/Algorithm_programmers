#numbers 숫자배열
#target 타겟넘버
#포화이진트리 만들기
#모든 경우의 수 배열에 넣고 카운트..?
def solution(numbers, target):
    answer = [0]
    count =0
    
    for i in numbers:
        tree = []
         
        for j in answer:
            tree += [j+i]
            tree += [j-i]
            count+=1
            if count ==1:
                answer.pop(0)
        answer=tree          #처음에는 이걸 +시킴.....................

    return answer.count(target)


solution([1,2,3,4],3)