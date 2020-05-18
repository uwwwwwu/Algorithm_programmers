#원소 없으면 -1

def solution(arr, divisor):
    num = max(arr) // divisor 

    answer = set(range(divisor,num*divisor+1,divisor))
   

    answer = set(arr) & set(answer)
    if(len(answer)==0):
        return [-1]
    
    return sorted(answer)


solution([5,9,7,10],5)