import re

def solution(dartResult):
    answer=[1,1,1]
    
    tmp_number = re.findall('\d+',dartResult) #숫자만 ['10', '2', '3']
    tmp_string = re.findall('[A-Z][*#]?',dartResult)#문자만 ['S', 'D*', 'T']
    
    answer[0] = tmp_number[0]
    answer[1] = tmp_number[1]
    answer[2] = tmp_number[2]
    
    
    # 1이랑 2.3 구분
    for i in range(len(tmp_string[0])):
        if tmp_string[0][i] == "D":
            answer[0] = int(tmp_number[0]) * int(answer[0])
        elif tmp_string[0][i] == "T":
            answer[0] = int(answer[0])*int(answer[0]) * int(answer[0]) #SDT 구분
            
        if tmp_string[0][i] == "*":
            answer[0] = 2 * int(answer[0])
        elif tmp_string[0][i] == "#":
            answer[0] = (-1) * int(answer[0]) # *,#구분

            
    for i in range(1,3):
        for j in range(len(tmp_string[i])):
            if tmp_string[i][j] == "D":
                answer[i] = int(tmp_number[i]) * int(answer[i])
            elif tmp_string[i][j] == "T":
                answer[i] = int(answer[i])*int(answer[i]) * int(answer[i])  #SDT 구분
        
        for j in range(len(tmp_string[i])):
            if tmp_string[i][j] == "*":
                answer[i-1] = 2*int(answer[i-1])
                answer[i] = 2*int(answer[i])
            elif tmp_string[i][j] == "#":
                answer[i] = (-1)*int(answer[i])  #*,#구분

    return int(answer[0])+int(answer[1])+int(answer[2])

solution("1S*2T*3S")