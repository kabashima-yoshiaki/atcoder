import random

N = 7
numbers = sorted(round(random.uniform(0, 3), 1) for _ in range(N))

print(numbers)