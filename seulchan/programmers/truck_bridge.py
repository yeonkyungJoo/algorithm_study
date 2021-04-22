# https://programmers.co.kr/learn/courses/30/lessons/42583
# 다리를 건너는 트럭
'''
input: int(bridge_length), int(weight), array(truck_weight)
output: int

1 <= brdge_length, weigth, len(truck_weight) <= 10000

# solution
## queue + bruth force (count)

q = deque(maxsize=bridge_length)  # 시간이 경과하면 트럭의 위치를 변경
truck_weigths = deque(truck_weights)  # popleft 하기위해 queue로 변경
count = 0

while sum(truck_weights) != 0:  # 다 0이 될 때 종료
    # next_truck
    truck = truck_weights[idx]
    
    if sum(q) + truck <= weight:  # 더 건널수 있음
    	truck = truck_weights.popleft()
    	q.add(truck)
    if sum(q) >= weigth:  # 더이상 못건넘
    	q.add(0)  # 0 추가
    count += 1  # loop당 1초씩 증가
    
-> time complex: O(count)
-> 더이상 못건너는 경우 loop를 줄일 수 있을듯
'''
from collections import deque
def solution(bridge_length, weight, truck_weights):
    count = 0
    bridge_queue = deque([0]*bridge_length)  # 시간이 경과하면 트럭 위치 변경
    truck_queue = deque(truck_weights)  # make queue for popleft
    weight_sum = 0  # sum(bridge_queue)가 시간복잡도가 O(n)이라서 피하기위해 생성
    
    while bridge_queue:
        # for calculating weight_sum
        arrived_weight = bridge_queue.popleft()
        weight_sum -= arrived_weight
        
        if truck_queue:
            if weight_sum + truck_queue[0] <= weight:  # can add more truck
                departure_weight = truck_queue.popleft()
                bridge_queue.append(departure_weight)
                weight_sum += departure_weight
            else:
                bridge_queue.append(0)
                
        count += 1
    return count   
'''
적당히 풀긴 했는데 잘 이해가 안가는 문제
다 건너는 시점이 +1이 되는 이유를 잘 모르겠음
'''

# class로 인터페이스를 생성하한 풀이가 인상깊어서 구현해봄
from collections import deque

DUMMY_TRUCK: int = 0

class Bridge:
    '''bridge implementation for calculating weight'''
    def __init__(self, max_length: int, max_weight: int) -> None:
        self.max_length: int = max_length
        self.max_weight: int = max_weight
        self.weight: int = 0
        self.queue: deque = deque([0]*max_length)

    def push(self, truck: int):
        '''add truck to bridge'''
        self.queue.append(truck)
        self._add_weight(truck)

    def pop(self) -> None:
        '''pop out truck from bridge'''
        arrived_truck = self.queue.popleft()
        self._subtract_weight(arrived_truck)

    def can_add(self, truck: int) -> bool:
        '''is possible to add more weight to the bridge'''
        return self.weight + truck <= self.max_weight and len(self) < self.max_length

    def _add_weight(self, weight: int):
        '''add total weight of bridge'''
        self.weight += weight

    def _subtract_weight(self, weight: int):
        self.weight -= weight

    def __bool__(self):
        return len(self) != 0

    def __iter__(self):
        yield from self.queue

    def __len__(self):
        return len(self.queue)

    def __repr__(self):
        return 'Bridge:[' + ','.join(map(str, self)) + '] ' + f'total weight: {self.weight}'


def solution(bridge_length, weight, truck_weights):
    count = 0

    bridge = Bridge(bridge_length, weight)
    truck_weights.reverse()

    while truck_weights:
        bridge.pop()

        next_truck = truck_weights[-1]
        bridge.can_add(next_truck)
        if bridge.can_add(next_truck):
            truck_weights.pop()
        else:
            next_truck = DUMMY_TRUCK

        bridge.push(next_truck)

        count += 1
    while bridge:
        bridge.pop()
        count += 1
    return count
