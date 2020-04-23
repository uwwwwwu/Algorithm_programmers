#1. 문자열들의 n번째 숫자를 기준으로 정렬
#2. 같은 문자인 경우에는 그냥 사전 순
# *소문자로 이루어짐
# *문자는 최대 50개

#[sun, bed, car] => [usun, ebed, acar]로 만들기


def solution(strings, n):
    result=[]
    for i in range(len(strings)):
        strings[i]= strings[i][n]+ strings[i]
    strings.sort();
    for i in range(len(strings)):
        result.append(strings[i][1:])

    return result

solution(["sun","bed","car"],1)
solution(["abce", "abcd", "cdx"],2)