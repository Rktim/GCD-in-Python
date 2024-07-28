
#Euclid's Algorithm
def gcd(a,b):
    if a<b:
        a,b=b,a
    if a%b==0:
        return b
    else:
        r=a%b
        return gcd(b,r)
    
print(gcd(4,12))

#With While
def d(a,b):
    if a<b:
        a,b=b,a
    while a%b!=0:
        a,b=b,a%b
    return b

print(d(4,12))