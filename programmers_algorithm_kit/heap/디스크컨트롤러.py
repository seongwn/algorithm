"""
Level 3

문제 설명

하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 이 문제에서는 우선순위 디스크 컨트롤러라는 가상의 장치를 이용한다고 가정합니다. 우선순위 디스크 컨트롤러는 다음과 같이 동작합니다.

어떤 작업 요청이 들어왔을 때 작업의 번호, 작업의 요청 시각, 작업의 소요 시간을 저장해 두는 대기 큐가 있습니다. 처음에 이 큐는 비어있습니다.
디스크 컨트롤러는 하드디스크가 작업을 하고 있지 않고 대기 큐가 비어있지 않다면 가장 우선순위가 높은 작업을 대기 큐에서 꺼내서 하드디스크에 그 작업을 시킵니다. 이때, 작업의 소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것 순으로 우선순위가 높습니다.
하드디스크는 작업을 한 번 시작하면 작업을 마칠 때까지 그 작업만 수행합니다.
하드디스크가 어떤 작업을 마치는 시점과 다른 작업 요청이 들어오는 시점이 겹친다면 하드디스크가 작업을 마치자마자 디스크 컨트롤러는 요청이 들어온 작업을 대기 큐에 저장한 뒤 우선순위가 높은 작업을 대기 큐에서 꺼내서 하드디스크에 그 작업을 시킵니다. 또, 하드디스크가 어떤 작업을 마치는 시점에 다른 작업이 들어오지 않더라도 그 작업을 마치자마자 또 다른 작업을 시작할 수 있습니다. 이 과정에서 걸리는 시간은 없다고 가정합니다.

각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 정수 배열 jobs가 매개변수로 주어질 때, 우선순위 디스크 컨트롤러가 이 작업을 처리했을 때 모든 요청 작업의 반환 시간의 평균의 정수부분을 return 하는 solution 함수를 작성해 주세요

"""


class DiskController:
    # priority: com_time -> req_time -> com_time
    def __init__(self, arr=[]):
        self.heap = arr

    def pop(self):
        if not self.heap:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()

        pop_data, self.heap[0] = self.heap[0], self.heap.pop()
        current, child = 0, 1
        while child < len(self.heap):
            sibling = child + 1
            if sibling < len(self.heap) and self.check_priority(self.heap[child], self.heap[sibling]):
                child = sibling
            if self.check_priority(self.heap[current], self.heap[child]):
                self.heap[current], self.heap[child] = self.heap[child], self.heap[current]
                current = child
                child = current * 2 + 1
            else:
                break

        return pop_data

    def push(self, process):
        self.heap.append(process)
        current = len(self.heap) - 1

        while current > 0:
            parent = (current - 1) // 2
            if self.check_priority(self.heap[parent], self.heap[current]):
                self.heap[parent], self.heap[current] = self.heap[current], self.heap[parent]
                current = parent
            else:
                break

    def check_priority(self, p1, p2):
        if p1.com_time != p2.com_time:
            return p1.com_time > p2.com_time

        elif p1.req_time != p2.req_time:
            return p1.req_time > p2.req_time

        return p1.idx > p2.idx


class Process:
    def __init__(self, idx, req_time, com_time):
        self.idx = idx
        self.req_time = req_time
        self.com_time = com_time


def solution(jobs):
    answer = 0
    cur_time = 0

    dc = DiskController([])

    jobs = sorted(jobs)
    for i in range(len(jobs)):
        dc.push(Process(i, jobs[i][0], jobs[i][1]))
        if i != len(jobs) - 1:
            if jobs[i][0] == jobs[i + 1][0] or (jobs[i + 1][0] <= cur_time + 1 and cur_time != 0):
                continue

        while dc.heap:
            proc = dc.pop()
            answer += max(0, cur_time - proc.req_time) + proc.com_time
            cur_time = max(proc.req_time, cur_time) + proc.com_time
            if i != len(jobs) - 1:
                if jobs[i + 1][0] <= cur_time + 1:
                    break

    return answer // len(jobs)

#     while dc.heap:
#         proc = dc.pop()
#         if proc.
#         answer += max(0, current_time - proc.req_time) + proc.com_time
#         current_time = max(proc.req_time, current_time) + proc.com_time

#     return answer // len(jobs)