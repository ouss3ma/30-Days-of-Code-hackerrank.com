def calc(d,y,m,d_ex,m_ex,y_ex):
    if y_ex>y:return(0)
    elif y_ex<y:return(10000)
    elif m_ex>m:return(0)
    elif m_ex<m:return((m-m_ex)*500)
    elif d_ex>=d:return(0)
    else: return((d-d_ex)*15)

d,m,y=map(int,input().split())
d_ex,m_ex,y_ex=map(int,input().split())

print(calc(d,y,m,d_ex,m_ex,y_ex))
