
# def m(arr):
#     if len(arr)==0:
#         return []
#     pos=sum([1 for i in arr if i>0])
#     neg=sum([i for i in arr if i<0])
#     return pos,neg
# print(m(arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
def m(arr):
    sum_neg=0
    c_p=0
    if len(arr)==0:
        return []
    i=0
    for i in range( arr):
        if arr[i]>0:
            c_p+=1
        elif arr[i]<0:
            sum_neg+=arr[i]
        i=i+1
    return c_p,sum_neg
print(m(arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))

def sum(arr):

    arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
    i=0
    count=0
    sum=0
    while i<len(arr):
        if len(arr)==0:
            return []
        elif arr[i]>0:
            count+=1
        elif arr[i]<0:
            sum=sum+arr[i]
        # elif len(arr)==0:
        #     return []
        i=i+1
    return count,sum
print(sum(arr=[]))
