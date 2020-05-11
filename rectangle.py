#별찍기
#이중 for문은 시간 오래 걸림


#a, b = map(int, raw_input().strip().split(' '))

#첫번째방법
for i in range(b):
    print("*"*a)
    print("\n")



#두번째 방법
print("*"*a+"\n")*b