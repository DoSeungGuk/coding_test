import heapq

def dijkstra(start):
    # 출발 지점에서
    INF = float('inf')
    distances = [INF] * N+1
    distances[start] = 0
    queue = [(0,start)]

    while queue:


while True:
    N, M = list(map(int, input().split())) # 장소 수, 도로 수
    S, D = list(map(int, input().split())) # 시작, 도착 점

    # 2차원 배열
    arr = [[] for _ in range(N+1)]

    for i in range(M):
        U, V, P = list(map(int, input().split()))
        arr[U].append([V,P])

    result = dijkstra(S)

'''
거의 최단 경로를 찾는 문제

문제에서 정의한 거의 최단 경로란 가장 빠른 경로를 제외한 다음으로 빠른 경로를 뜻한다.

만약 최단 경로가 3이라면 거의 최단 경로는 4 이상이 된다는 뜻이고

최단 경로는 여러 경로가 나올 수 있다.

거의 최단 경로는 없을 수도 있다.

그러면

1. 다익스트라를 이용해서 최단 경로를 구한 뒤
2. 거리를 기록하고 경로를 지운다.
3. 다시 다익스트라를 한다.
4. 2에서 기록한 거리와 동일하면 그 경로도 지운다.
5. 거의 최단 경로 즉, 2와 다른 값이 다익스트라를 통해 나오면 거의 최단 경로를 출력한다.
6. 경로가 없어지면? <- -1을 출력한다.
'''