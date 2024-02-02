a = int(input())

# 내 답안. 한줄에 다 넣으면 지저분할 것 같았는데 그냥 괜찮은 듯.  
for i in range(1,a+1):
    # if i % 2 == 0 and i % 4 != 0:
    #     pass
    # elif (i // 8) % 2 == 0:
    #     pass
    # elif (i % 7) < 4:
    #     continue
    # else:
    #     print(i, end=' ') 


# 해설 - 조건을 모두 만족하지 않는 수들만 출력합니다.
for i in range(1, a + 1):
    if(i % 2 == 0 and i % 4 != 0) or (i // 8) % 2 == 0 or (i % 7) < 4:
        continue
    print(i, end=" ")