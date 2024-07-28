def gcd(x,y):
    m=[]
    for i in range(1,x+1):
        if x%i==0:
            m.append(i)
    print("m:", m)    
    n=[]
    for j in range(1,y+1):
        if y%j==0:
            n.append(j)
    print("n:",n)
    
    c=[]
    for f in m:
        if f in n:
            c.append(f)
    return max(c)



print("GCD: ",gcd(8,12))



def igcd(x,y):
    cf=[]
    for i in range(1,min(x,y)+1):
        if x%i==0 and y%i==0:
            cf.append(i)
    return max(cf)

print("GCD:",igcd(4,12))



def wgcd(x,y):
    for i in range(1,max(x,y)+1):
        if x%i==0 and y%i==0:
            mcf=i
            
    return mcf

print("MCF: ", wgcd(4,12))


def gcdd(x,y):
    i=min(x,y)
    while i>0:
        if x%i==0 and y%i==0:
            return i
        else:
            i=i-1
    

print("mcf:",gcdd(4,12))