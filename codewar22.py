def m(arr):
    count=0
    total=0
    for i in arr:
        if i>0:
            count+=1
        if i<0:
            total+=i

    return [count,total ] if len(arr)!=0 else  []
print(m(arr=[1,2,3,4,15]))
