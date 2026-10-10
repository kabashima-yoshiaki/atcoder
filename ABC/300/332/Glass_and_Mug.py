k,g,m=map(int,input().split())
g_t=0
m_t=0
for i in range(k):
    if g_t == g:
        g_t = 0
    elif m_t == 0:
        m_t = m
    else:
        while m_t != 0 and g_t != g:
            m_t -= 1
            g_t += 1
print(g_t, m_t)