#그냥 밀어 넣을까..

def solution(s, n):
    answer = list(s)
    for i in range(len(answer)):
        if answer[i]!=" ":
            answer[i]=int(ord(answer[i]))+n
    
    for i in range(len(answer)):
        if answer[i] == ' ':
            continue
        if 123<=int(answer[i]) :
            answer[i] = chr(answer[i]-26)
        elif 91<=int(answer[i]) <97 :
            answer[i] = chr(answer[i]-26)
        elif answer[i] != ' ' :
            answer[i]= chr(answer[i])
        
            
    
    return ''.join(answer)
solution("AaZz",25)



def solution2(s, n):
    A=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]*2  #65~90
    B=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]*2  #97~120
    
    answer = list(s)
    for i in range(len(answer)):
        if answer[i].islower(): # 소문자면
            answer[i]=B[ord(answer[i])-97+n]
        elif answer[i].isupper(): # 대문자면
            answer[i]=A[ord(answer[i])-65+n]
        

    return ''.join(answer)

solution2(" z",1)