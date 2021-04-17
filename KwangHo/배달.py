from queue import PriorityQueue
def solution(N, road, K):
    q = PriorityQueue() #우선순위초기화
    q.put([1, 0]) #시작위치 추가
    dist = [float('inf')] * (N + 1) #거리초기화
    dist[1] = 0 #자기자신거리0
    while not q.empty(): #빌때까지
        current, current_cost = q.get() #우선순위에선 팝이라한다.
        for src, dest, cost in road: #전체 돌면서
            next_cost = cost + current_cost #현재까지의 코스트+현재의 코스트
            if src == current and next_cost < dist[dest]: #현재에서 작은값 갱신된곳 푸쉬
                dist[dest] = next_cost
                q.put([dest, next_cost])
            if dest == current and next_cost < dist[src]: #현재에서 역으로 작으면 갱신 푸쉬
                dist[src] = next_cost
                q.put([src, next_cost])
    return len([i for i in dist if i <= K])
'''
예전에 플로이드 본게 있어서 그걸로할라다가
다익스트라 파이썬으로 해보자해서 하는데
우선순위큐를 써야 최소값을 팝 할수 있다해서
그거 보고 코드짜는법 숙지후 / 복사코딩함
'''