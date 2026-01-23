# def fun(i,ar,given,target):
#     if i==len(given):
#         if target==0:
#             print(ar,end='')
#         return
    
#     ar.append(given[i])
#     target-=given[i]
#     fun(i+1,ar,given,target)

#     target+=given[i]
#     ar.pop()
#     fun(i+1,ar,given,target)
#     return ar

# ar=[]
# given=[1,2,3,4,6]
# target=5
# fun(0,ar,given,target)

# def fun(i,ar,given,target):
#     if i==len(given):
#         if target==0:
#             print(ar,end='')                    #Print only 1 subsequence
#             return True
#         else:
#             return False
    
#     ar.append(given[i])
#     target-=given[i]
#     if fun(i+1,ar,given,target)==True:
#         return True

#     target+=given[i]
#     ar.pop()
#     if fun(i+1,ar,given,target)==True:
#         return True
#     return False

# ar=[]
# given=[1,2,3,4,6]
# target=5
# fun(0,ar,given,target)

def fun(i,ar,given,target):
    if i==len(given):
        if target==0:
            return 1
        return 0
    
    ar.append(given[i])
    target-=given[i]
    take=fun(i+1,ar,given,target)

    target+=given[i]
    ar.pop()
    nontake=fun(i+1,ar,given,target)
    return take + nontake

ar=[]
given=[1,2,3,4,6]
target=5
count=0
print(fun(0,ar,given,target))