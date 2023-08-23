from typing import Tuple

def w_avg(*l: Tuple[float, float]) -> float:
    return sum(x[0] * x[1] for x in l) / sum(x[1] for x in l)

def avg(it):
    return sum(it) / len(it)

def percentile(it, p):
    return sorted(it)[int(len(it) * p)]

def bounds(l, x, r):
    if x < l:
        x = l
        
    if x > r:
        x = r
    
    return x