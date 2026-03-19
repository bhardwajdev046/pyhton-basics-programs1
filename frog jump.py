def fun(idx,arr,dp):
    if idx==0:
        return 0
    if dp[idx]!=-1:
        return dp[idx]
    a=fun(idx-1,arr,dp)+abs(arr[idx]-arr[idx-1])
    if idx>1:
        b=fun(idx-2,arr,dp)+abs(arr[idx]-arr[idx-2])
    else:
        b=float('inf')
    dp[idx]= min(a,b)
    return dp[idx]



# arr=[30, 20, 50, 10, 40]
arr=[20, 30, 40, 20]
idx=3
dp=[-1]*(idx+1)
print(fun(idx,arr,dp))