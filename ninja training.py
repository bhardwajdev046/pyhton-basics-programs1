def fun(day, last,dp):
    if day==0:
        maxi=float('-inf')
        for i in range(3):
            if i!=last:
                maxi=max(maxi,ar[0][i])
        return maxi
    if dp[day][last]!=-1:
        return dp[day][last]
    maxi=float('-inf')
    for i in range(3):
        if i!=last:
            points=ar[day][i]+fun(day-1,i,dp)
            maxi=max(maxi,points)
    dp[day][last]=maxi
    return dp[day][last]



ar=[[10, 40, 70], [20, 50, 80], [30, 60, 90]]
dp=[[-1]*4 for _ in range(len(ar))]
day=len(ar)
last=len(ar[0])
print(fun(day-1,last,dp))