import heapq
import sys

N = int(input())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        if x > 0:
            heapq.heappush(heap, [x, x])
        else:
            heapq.heappush(heap, [-x, x])