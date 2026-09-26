S = input()
if S  in 'red' or S in 'blue' or S in 'green':
    print(S.replace('red', 'SSS', 3).replace('blue', 'FFF', 3).replace('green', 'MMM', 3))
else:
    print("Unknown")

