import sys 
from typing import List
from collections import defaultdict

# drawing using Excalidraw
# USD,CAD,1.3;USD,GBP,0.71;USD,JPY,109;GBP,JPY,155
# USD,GBP,0.7;USD,JPY,109;GBP,JPY,155;CAD,CNY,5.27;CAD,KRW,921
data = []
for line in sys.stdin: 
    # print("line ",line)
    data.append(line.strip())
    if line.strip() == 'JPY':
        print("break")
        break;

exchanges = []
for d in data[0].split(';'): 
    src, des, weight = d.split(',')
    exchanges.append((src, des, float(weight)))
    # print(exchanges)

# Compute the exchange rate
def maxAmountofExchange(exchanges: List[str], from_currency, to_currency):
    graph = defaultdict(list)
    for src, des, weight in exchanges:
        graph[src].append((des, float(weight)))
        graph[des].append((src, 1.0/float(weight)))
        print(src, des, float(weight))
        print(des, src, 1.0/float(weight))
    
    rate = -1.0
    visited = set()
    
    # DFS recursive 
    def dfs(src, des, exch):
        nonlocal rate
        if src not in graph or des not in graph: 
            return
        if src == des:
            rate = max(rate, exch)
            return 
        visited.add(src)
        for neighbor, weight in graph[src]:
            if neighbor not in visited: 
                dfs(neighbor, des, exch * weight)

    
    dfs(from_currency, to_currency, 1.0)
    print("rate is", rate)
    return rate 

maxAmountofExchange(exchanges, data[1], data[2])