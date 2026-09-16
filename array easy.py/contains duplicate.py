freq={}
nums=[int(x) for x in input().split()]
if len(nums)==1:
    print(False)
    break

for x in nums:
    if x not in freq:
        freq[x]=1
    else:
        freq[x]+=1
        print(True)
print(False) 