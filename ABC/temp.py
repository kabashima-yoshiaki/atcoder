import os 

for N in [200, 300, 400]:
    os.mkdir(f"./ABC/{N}")
    for n in range(N, N+100):
        os.mkdir(f"./ABC/{N}/{n}")
        for c in ["A", "B", "C", "D", "E", "F", "G"]:
            with open(f"./ABC/{N}/{n}/ABC{n}_{c}.py", "w") as f:
                pass 
