# Python program for the above approach
def dfs(temp, n, sol):
    if (temp > n):
        return
    sol.append(temp)
    dfs(temp * 10, n, sol)
    if (temp % 10 != 9):
        dfs(temp + 1, n, sol)
 
n = 130
result = []
dfs(1, n, result)
print(result)