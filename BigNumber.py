def solution(n):
    # 함수를 완성하세요.
    
    len_t = []
    answer =[]

    n=list(map(str,n))

    print(n)
    for i in range(len(n)):
        print(n[i])
        if len(n[i]) == 3:
            len_t.append(str(int(n[i])/100))

        elif len(n[i]) == 2:
            len_t.append(str(int(n[i])/10))

        else:
            if n[i]=='9':
                answer =['9']
            else: len_t += n[i]
            
    print(len_t)gi
    len_t.sort(reverse=True)

    for s in range(len(len_t)-1):
        if int(float(len_t[s])*10) == int(float(len_t[s+1])*10):
            len_t[s], len_t[s+1] = len_t[s+1], len_t[s]
          
    answer= answer+len_t
    
    answer= ''.join(answer).replace(".","")

    return answer
