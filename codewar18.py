
def maps(a):
    i=0
    mul=[]
    while i<len(a):
        b=a[i]+a[i]
        i=i+1
        mul.append(b)
    return mul
print(maps(a=[1,2,3]))

