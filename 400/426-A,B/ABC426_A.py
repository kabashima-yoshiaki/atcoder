x, y = input().split()
version = {}
version['Ocelot'] = 1
version['Serval'] = 2
version['Lynx'] = 3

print('Yes' if version[x] >= version[y] else 'No')