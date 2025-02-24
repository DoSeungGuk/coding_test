def len_cable(n,cables):
    low = 1
    high = max(cables)
    result = 0
    while low <= high:
        mid = (low+high)//2
        # 만들 수 있는 임시 케이블 수
        temp_cables = 0
        for i in range(len(cables)):
            temp_cables += cables[i] // mid

        # 랜선 개수가 충분할 때
        if temp_cables >= n:
            low = mid + 1
            result = mid

        # 랜선 개수가 부족할 때
        else:
            high = mid -1

    return result


k,n = list(map(int,input().split()))
cables = []
for i in range(k):
    cables.append(int(input()))

print(len_cable(n,cables))
'''
전형적인 이진탐색 문제이다.

선을 자를 길이를 구할 때 1,2,3,4... 매 번 숫자를 올려가면서 답을 구할 수도 있지만 
이는 시간이 너무 오래 걸리며 

1.
low 값을 1
high 값을 최대 길이의 선을 기준으로 설정한다.

2.
low+high 값을 2로 나눈 값을 mid로 설정하고

3.
mid로 모든 선을 나눴을 때 몫을 구한다.
모든 몫을 더한 값이 n 이상이면 low 값을 mid+1 값으로 변경한다.
result 변수를 설정하고 결과를 저장한다.

반대의 경우 high 값을 mid-1 값으로 변경한다.

4.
2번 3번을 반복한다. 
low 값이 high 값을 초과하면 종료

'''