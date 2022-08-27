# Input: arr1= [1,2,3,0,0,0], m= 3,arr2=[2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] .
# You are given two integer arrays arr1 and arr2 which are sorted in a non-decreasing order and there are two numbers m and n which represent the number of elements in arr1 and arr2 respectively.

# Your task is to merge arr1 and arr2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead should be stored inside the array arr1. To achieve this, arr1 has a length of m + n , where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. arr2 has a length of n.

# Input Format
# First Parameter - m , the number of elements in arr1

# Second Parameter - n, the number of elements in arr2

# Third Parameter - integer array arr1 of length (m+n)

# Fourth Parameter - integer array arr2 of length n

# Output Format
# Return the integer array arr1 with elements merged in non-decreasing order.

# Example 1:
# Input: arr1 = [0], m = 0, arr2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note:- That because m = 0, there are no elements in arr1. The 0 is only there to ensure the merge result can fit in arr1.
# Example 2:
# Input: arr1 = [1], m = 1, arr2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:
# Input: arr1= [1,2,3,0,0,0], m= 3,arr2=[2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] .

# arr1= [1,2,3,0,0,0]
# arr2=[2,5,6]
# i=0
# b=[]
# c=[]
# d=[]
# while i<len(arr1) and i<len(arr2):
#     if arr1[i]==0 and arr2[i]==0:
#         continue
#     c.append(arr1[i])
#     d.append(arr2[i])
#     e=c+d
#     b.append(e)
#     # e=c+d
#     # b.append(c+d)
#     i=i+1
# print(sorted(e))

# arr1= [1,2,3,0,0,0]
# arr2=[2,5,6,0]
# m=int(input("enter no"))
# n=int(input("enter no"))
# z=[]
# # b=[]
# i=0
# while i<m:
#     z.append(arr1[i])
#     i=i+1
# j=0
# while j<n:
#     z.append(arr2[j])
#     j=j+1
# # print(a)
# # x=0
# # z=[]
# # y=0
# # while y<len(a):
# #     if a[y]>x:
# #         x=a[y]
# #         z.append(x)
# #     y=y+1
# # print(z)
# k=0
# while k<len(z):
#     x=k+1
#     while x<len(z):
#         if z[k]>z[x]:
#             temp=z[k]
#             z[k]=z[x]
#             z[x]=temp
#         x+=1
#     k=k+1
# print(z)


# arr1= [1,2,3,0,0,0]
# arr2=[2,5,6,0]
# m=int(input("enter no"))
# n=int(input("enter no"))
# a=[]
# for i in range(0,m):
#     a.append(arr1[i])
# for j in range(0,n):
#     a.append(arr2[j])
# print(a)


# n=int(input("enter no: "))
# i=1
# f=0
# while i<=n:
#     if n%i==0:
#         f=f+1
#     i=i+1
# if f==2:
#     print("prime")
# else:
#     print("not prime")
#     print("not prime")

# num=int(input("enter the no"))
# length=len(str(num))
# temp=num
# sum=0
# while temp>0:
#     digit=temp%10
#     sum=sum+digit**length
#     temp=temp//10
# if sum==num:
#     print(num,"is armstrong")
# else:
#     print(num,"is not an armstrong")

# def build_string(*args):
#     return "I like {1}!".format(",".join(args))

# test.assert_equals(build_string('Cheese','Milk','Chocolate'), 'I like Cheese, Milk, Chocolate!', 'Return the correct String')
# test.assert_equals(build_string('Cheese','Milk'), 'I like Cheese, Milk!', 'Return the correct String')
# test.assert_equals(build_string('Chocolate'), 'I like Chocolate!', 'Return the correct String')



# def shortcut( s ):
#     i=0
#     string=""
#     vowels=("a","e","i","o","u")
#     for i in s:
#         if i not in vowels:
#             string+=i
#     return string

# def add_extra(list_of_numbers):
#     i=0
#     sum=0
#     while i<len(list_of_numbers):
#         sum+=list_of_numbers[i]
#         i=i+1
#     return (sum)
# print(add_extra(list_of_numbers=[1,2]))

# def add_extra(list_of_numbers):
#     i=0
#     a=[]
#     while i<len(list_of_numbers):
#         a.append(list_of_numbers[i])
#         i=i+1
#     a.append(i+1)
#     return a


# print(add_extra(list_of_numbers=[1,2]))

# def build_string(*args):
#     i=0
#     str=""
#     while i<len(args):
#         string="I like "+args+"!"
#         str+=string
#     return str


# print(build_string('Cheese','Milk','Chocolate'))

# n=int(input("enter no: "))
# i=1
# t=0
# while i<=n:
    

# Task
# Write a function that returns true if the number is a "Very Even" number.

# If a number is a single digit, then it is simply "Very Even" if it itself is even.

# If it has 2 or more digits, it is "Very Even" if the sum of its digits is "Very Even".

# Examples
# number = 88 => returns false -> 8 + 8 = 16 -> 1 + 6 = 7 => 7 is odd 

# number = 222 => returns true -> 2 + 2 + 2 = 6 => 6 is even

# number = 5 => returns false

# number = 841 => returns true -> 8 + 4 + 1 = 13 -> 1 + 3 => 4 is even




# n=int(input("enter a number"))
# if n%2==0:
#     i=1
#     while i<=n:
#         if n%2==0:
#             print(n)
#         i=i+1
# else:
#         a=n/2
#         c=int(a)
#         i=1
#         while i<=c:
#             if n%2!=0:
#                 print(n)
#             i=i+1

# # # # take user input and if you put 4 it will sum all the no that you  enter 
# a=int(input("entr no"))
# i=1
# sum=0
# while i<=a:
#     n=int(input("enter the number"))
#     sum=sum+n
#     print(sum)
#     i=i+1
# print("total",sum)

# a=int(input("enter no"))
# i=1
# sum=0
# while i<=a:
#     b=int(input("enter no"))
#     sum=sum+b
#     print(sum)
#     i=i+1
# print(sum)


# n=int(input("enter the even number"))
# i=2
# while i<=n:
#     if i%2==0:
#         print(i)
#         i=i+2


# a='eptyuio'
# i=0
# b=''
# while i<len(a):
#     if i==3:
#         b=a[i]
#         print(b)
#     i=i+1
        

# def merge_the_tools(string, k):
#     for i in range(0, len(string), k):
#         uniq = ''
#         for c in string[i : i+k]:
#             if (c not in uniq):
#                 uniq+=c
#         print(uniq)  

# a="aabbcccde"
# i=0
# k=3
# b=''
# while i<k:
#     j=0
#     while j<len(a):
        
#         if a[j]==k:
#             print(a[i])
#             # print(b)
#         j=j+1
#     i=i+1
        # print(a[j])
        
    # print(a[i])
    # i=i+k


# shifted = a[d%n:] + a[:d%n]
# for num in shifted:
#     print(num, end=' ')  


# a="aabbcccde"
# i=0
# b=''
# while i<len(a):

#     if a[i] not in b:
#         b=a[i]
#         print(b)
#     i=i+1


# >>> string = "abracadabra"
# >>> l = list(string)
# >>> l[5] = 'k'
# >>> string = ''.join(l)
# >>> print string
# abrackdabra

# def mutate_string(string, position, character):
#     stru=""
#     l=list(string)
#     l[position]=character
#     # print(l)
#     i=0
#     while i<len(l):
#         stru+=l[i]
#         i=i+1
#     return stru

# print(mutate_string(string="abracadabra", position=5, character="k"))
# a=["a","b","c"]
# i=0
# while i<len(a):
#     print(a[i])
#     i=i+1

# def count_substring(string, sub_string):
#     i=0
#     c=0
#     srt=""
#     while i<len(string):
#         j=0
#         while j<len(sub_string):
#             if sub_string[i] in string:
#                 print(sub_string[j])
#                 # c=c+1
                
            
#             # print(c)
#             j=j+1
#         # print(sub_string[j]) 
#         i=i+1
#         break
# count_substring(string="ABCDCDC", sub_string="CDC")


# def count_substring(string, sub_string):
#     i=0
#     c=0
#     srt=""
#     while i<len(string):
#         j=0
#         while j<len(sub_string):
#             if sub_string[i] in string:
#                 v=sub_string[j]
#                 if v not in srt:
#                     srt+=v
#                     c=c+1
                   
            
#             j+=1
#         print(c)
#         i+=1
#         break

# count_substring(string="ABCDCDC", sub_string="CDC")

# def count_substring(string, sub_string):
#     string_length=len(string)
#     sub_length=len(sub_string)
#     t=string_length-sub_length
#     i=0
#     count=0
#     while i<=t:
#         if string[i:sub_length]==sub_string:
#             count+=1
#         sub_length+=1
#         i+=1
#     return count

# print(count_substring(string="ABCDCDC", sub_string="CDC"))

# num=int(input("enter no"))
# b=int(input("enter no"))
# for i in range(num,b+1):
# # for i in range(2,b+1):
#     f=0
#     for j in range(2,i):
#         if (i%j==0):
#             f=1
#             # break
#     if f==0:
#         print(i,end=' ')



# num=int(input("enter no"))
# b=int(input("enter no"))
# i=num
# while i<=b:
#     f=0
#     j=1
#     while j<=i:
#         if i%j==0:
#             f=1
#         j=j+1
#     i=i+1
#     if f==0:
#         print(i,end=" ")

# def rotateLeft(d, arr):
#     i=0
#     a=[]
#     while i<d:
#         a.append(arr[i])
#         i=i+1
#     i=0
#     while d<len(arr):
#         arr[i]=arr[d]
#         i=i+1
#         d=d+1
#     arr[:]=arr[:i]+a
#     return arr
# print(rotateLeft(d=2,arr=[1,2,3,4,5]))



# a=[1,2,3,4,5]
# i=0
# b=[]
# while i<len(a):

#     i=i+1
# print()
    

# def rotateLeft(d, arr):
#     i=0
#     empty=[]
#     while i<d:
#         empty.append(arr[i])
#         i=i+1
#     i=0
#     while i<len(arr):
#         arr[i]=arr[d]
#         i=i+1
#         d=d+1
#     arr[:]=arr[:i]+empty
#     return arr

# print(rotateLeft(d=2, arr=[1,2,3,4,5]))


   
# n = int(input("enter no"))
# student_marks = {}
# for i in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input("enter name")
# o=list(student_marks[query_name])
# u=sum(o)/len(o)
# print("%.2f"%u)





# N = int(input())
# commands =[]
# scores =[]
# ans =[]
# for _ in range(N):
#     c, *line = input().split()
#     print(c)
#     commands.append(c)
#     s = list(map(int,line))
#     scores.append(s)
# def new_func(score, command):
#     if command == "insert" and score != []:
#         ans.insert(score[0],score[1])
#     elif command == "print":
#         print(ans)
#     elif command == "remove" and score != []:
#         ans.remove(score[0])
#     elif command == "append"and score != []:
#         ans.append(score[0])
#     elif command == "sort":
#         ans.sort()
#     elif command == "pop":
#         ans.pop()
#     elif command == "reverse":
#         ans.reverse()
# for i in range(N):
#     new_func(scores[i], commands[i])


# def miniMaxSum(arr):
#     i=0
#     min=0
#     max=-arr[0]

#     while i<len(arr):
#         # print(arr[i])
#         min=min+arr[i]
#         max=max+arr[i]
#         i=i+1
#     return max
# print(miniMaxSum(arr=[7, 69 ,2, 221, 8974]))


# def miniMaxSum(arr):
#     i=0
#     min=0
#     max=0

#     while i<len(arr):
#         if arr[i]>max:
#             max=arr[i]
#         elif arr[i]<max and arr[i]> min:
#             min=arr[i]
#         # min=min+arr[i]
#         # max=max+arr[i]
#         i=i+1
#     return max,min
# print(miniMaxSum(arr=[7, 69,2,1, 221, 8974]))

# def miniMaxSum(arr):
#     i=0
#     total=0
#     sum=0
#     while i<len(arr):
#         mini=min(arr)
#         maxi=max(arr)
#         total=total+arr[i]
#         # sum+=arr[i]
#         minimum=total-maxi
#         maximum=total-mini

#         i=i+1
#     # return(mini,maxi)
#     return minimum,maximum
# print(miniMaxSum(arr=[1 ,2 ,3 ,4, 5]))

# def miniMaxSum(arr):
#     i=0
#     total=0
#     while i<len(arr):
#         mini=min(arr)
#         maxi=max(arr)
#         total=total+arr[i]
#         # sum+=arr[i]
#         minimum=total-maxi
#         maximum=total-mini
#         i=i+1
#     # return(mini,maxi)
#     print(minimum,maximum)

# def plusMinus( arr):
#     i=0
#     length=len(arr)
#     pos=0
#     neg=0
#     zero=0
#     while i<len(arr):
#         if arr[i]>0:
#             pos+=1
#             posi=pos/length
#         elif arr[i]<0:
#             neg+=1
#             negi=neg/length
#         elif arr[i]==0:
#             zero+=1
#             zer=zero/length
#         i=i+1
#     print("%.6f\n"%posi,negi,zer)
#     # print("%.6f"%negi)
#     # print("%.6f"%zer)
#     # return ("%.6f"%posi,"%.6f"%negi,"%.6f"%zer)
# plusMinus( arr = [-1,-1,0,1,1])
# # print(plusMinus( arr = [-4, 3, -9, 0, 4, 1]))


# def plusMinus(arr):
#     i=0
#     length=len(arr)
#     pos,neg,zero=0,0,0
#     while i<len(arr):
#         if arr[i]>0:
#             pos+=1/length
#             # posi=pos/length
#         elif arr[i]<0:
#             neg+=1/length
#             # negi=neg/length
#         else:
#             zero+=1/length
#             # zer=zero/length
#         i=i+1
#     print("%.6f\n"%pos+"%.6f\n"%neg+"%.6f\n"%zero)
#     # Write your code here


#


# def compareTriplets(a, b):
#     count1=0
#     count2=0
#     i=0
#     while i<len(a) :
#         if a[i]>b[i]:
#             count1+=1
#         elif a[i]<b[i]:
#             count2+=1
#         i=i+1
#     return (count1,count2) 
# print(compareTriplets(a=[17, 28 ,30], b=[99 ,16, 8]))

# # ar_count = int(input().strip())

# #     ar = list(map(int, input().rstrip().split()))

# #     result = aVeryBigSum(ar)

# #     fptr.write(str(result) + '\n')

# #     fptr.close()

# def diagonalDifference(arr):
#     left,right=0,0
#     i=0
#     while i<len(arr):
#         left1=arr[i][i]
#         right1=arr[i][len(arr)-i-1]
#         left+=left1
#         right+=right1
#         i=i+1
#     return abs (right-left)
# The abs() function returns the absolute value of the specified number.
# # input..

# # 11,5,12
# # 4,5,10

# # 11 2 4
# # 4 5 6
# # 10 8 -12

# def printfizz(a):
#     if a%3==0 and a%5==0: 
#         print("fizzbazz")
#     elif a%3==0:
#         print("fizz")
#     elif a%5==0:
#         print('bazz')
#     else:
#         print(a)
# printfizz(a=int(input("enter the no: ")))
