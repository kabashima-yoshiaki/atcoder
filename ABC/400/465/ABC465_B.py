
X, Y, L, R, A, B = map(int, input().split())
if B <= L or R <= A:
    print((B-A)*Y)
  
elif A <= L and (L <= B) and (B <= R):
    print((L-A)*Y + (B-L)*X)
   
elif A <= L and B  >= R:
    print((L-A)*Y +(R-L)*X + (B-R)*Y)
  
elif L <= A and B <= R:
    print((B-A)*X)
  
elif L <= A and R <= B:
    print((R-A)*X + (B-R)*Y)
   
    

    