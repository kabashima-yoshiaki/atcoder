if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from dezero import test_mode
import dezero.functions as F

x = np.ones(5)
print(x)

# When training
y = F.dropout(x)
print(y)

# When testing (predicting)
with test_mode():
    y = F.dropout(x)
    print(y)

N, M = map(int, input().split())
G = [[] for _ in range(N)] 
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1   
    G[a].append(b)
    G[b].append(a)
