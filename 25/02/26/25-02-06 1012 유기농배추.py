'''
배추를 재배한다.
배추를 해충으로부터 보호
배추흰지렁이를 구입
배추 근처에 서식하며 해충을 잡아먹는다
어떤 배추에 배추흰지렁이가 한 마리라도 살고있으면 이 지렁이는 인접한 다른 배추로 이동 가능
그 배추들 역시 해충으로부터 보호받을 수 있음

상하좌우 네 방향에 다른 배추가 위치한 경우 서로 인접한 것

배추를 군데군데 심어둠

배추가 모여있는 곳은 지렁이 한 마리만 있으면 되므로 서로 인접해 있는  배추들이 몇 군데 퍼져있는지 조사해라

접근 방법
완전탐색이 제일 빠르겠는데
인접 dxdy로 확인하고 지나가면 -1 처리해주고
bfs를 사용해서 탐색을 한다.
다 지나가면 count에 1 증가시키고 다시 탐색
기초적인 bfs 문제였습니다.

끝.
'''
from collections import deque


def bfs(i, j):
    que = deque([(i,j)])
    farm[i][j] = 0
    while que:
        a,b = que.popleft()
        for k in range(4):
                a1 = a+dx[k]
                b1 = b+dy[k]
                if 0<= a1 < M and 0<= b1 < N and farm[a1][b1]:
                    que.append((a1,b1))
                    farm[a1][b1] = 0


T = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for tc in range(T):

    M, N, K = list(map(int, input().split()))

    farm = [[0]*N for _ in range(M)]
    for _ in range(K):
        x, y = list(map(int, input().split()))
        farm[x][y] = 1

    count = 0
    for i in range(M):
        for j in range(N):
            if farm[i][j]:
                bfs(i,j)
                count += 1

    print(count)
