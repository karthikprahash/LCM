# LCM
n,m=map(int,input().split())
p=[]
q=[]
r=[]
for i in range(1,n+1):
    if n%i==0:
        p.append(i)
for x in range(1,m+1):
    if m%x==0:
        q.append(x)
for g in p:
    if g in q:
        r.append(g)
print((n*m)//max(r))
        
