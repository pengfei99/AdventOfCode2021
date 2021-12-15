import sys
import numpy as np
import heapq as hq

def search(m):
    h,w = np.shape(m)
    q = [(0,(0,0))]     # risk, starting point
    while q:
        risk, (x,y) = hq.heappop(q)
        if (x,y) == (w-1,h-1):
            return risk
        for x,y in [(x,y+1),(x+1,y),(x,y-1),(x-1,y)]:
            if x >= 0 and x < w and y >= 0 and y < h and m[y][x] >= 0:
                hq.heappush(q, (risk+(m[y][x] % 9)+1, (x,y)))
                m[y][x] = -1    # mark as seen

if __name__ == '__main__':
    m = np.genfromtxt(sys.argv[1], dtype=int, delimiter=1) - 1
    print(f"part 1, {search(m.copy())}")
    m = np.concatenate([m+i for i in range(5)], axis=0)
    m = np.concatenate([m+i for i in range(5)], axis=1)
    print(f"part 2, {search(m)}")