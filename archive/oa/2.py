
import sys 
from typing import List
from collections import defaultdict


data = []
for line in sys.stdin: 
    data.append(line.strip())
  
curr_exch = []
for d in data[0].split(';'): 
    src, des, wt = d.split(',')
    curr_exch.append((src, des, float(wt)))

def maxAmount(curr_exch: List[str], from_curr, to_curr):
    g = defaultdict(list)
    for src, des, wt in curr_exch:
        g[src].append((des, float(wt)))
        g[des].append((src, 1.0/float(wt)))
    
    rate = -1.0
    visited = set()
    
    def dfs(src, des, exch):
        nonlocal rate
        if src not in g or des not in g: 
            return
        if src == des:
            rate = max(rate, exch)
            return 
        visited.add(src)
        for adj, wt in g[src]:
            if adj not in visited: 
                dfs(adj, des, exch * wt)

    dfs(from_curr, to_curr, 1.0)
    return rate 

ans = maxAmount(curr_exch, data[1], data[2])
print(ans)