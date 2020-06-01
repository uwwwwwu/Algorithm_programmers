# n = len(data)
# m = 데이터의 합

n,m=5,5
data =[1,2,3,2,5]

result=0
summary =0
end =0

#start를 차례대로 증가시키며 반복
for start in range(n):
    #end를 가능한만큼 이동시키기
    while summary < m and end <n: #summary가 5보다 작거나 end가 len(data)보다 크면 나가기
        summary += data[end]
        end += 1
        
    if summary == m:
        result += 1
    summary -= data[start]
    
print(result)