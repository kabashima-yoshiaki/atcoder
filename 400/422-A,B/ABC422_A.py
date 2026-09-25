""" s = input()

memo = [int(s[0:1]), int(s[2:3])]
if memo[1] < 8:
    print('{}-{}'.format(memo[0], memo[1]+1))
elif memo[0] < 8 and memo[1] == 8:
    print('{}-{}'.format(memo[0]+1, 1)) """

s = input()
a = int(s[0])
b = int(s[2])
if b == 8:
    print(str(a+1) +'-1')
else:
    print(str(a) + '-' + str(b+1))
