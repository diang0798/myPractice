from array import *
#
# arr = array('i', [])
#
# n = int(input("Enter the length of the array: "))
#
# for i in range(n):
#     x = int(input("Enter the next value: "))
#     arr.append(x)
#
# print(arr)
#
# val = int(input("Enter the value for search: "))
#
# k = 0
# for e in arr:
#     if e == val:
#         print(k)
#         break
#     k += 1
#
# print(arr.index(val))

# P1: Remove the nth element in the array
myarr = array('i', [2, 4, 6, 8, 10])
print(myarr)
index = int(input("Enter the index of the element to remove: "))
myarr.remove(myarr[index])
print(myarr)


# P2: Reverse an array
for i in range(len(myarr)//2):
    temp = myarr[i]
    myarr[i] = myarr[-(i+1)]
    myarr[-(i+1)] = temp
print(myarr)
# by function
myarr.reverse()
print(myarr)