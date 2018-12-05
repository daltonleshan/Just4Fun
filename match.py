def matches(p, s):
    p = p[::-1]
    s = s[::-1]
    if not s or not p:
        return False
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True
    for i in range(len(p)):
        if p[i] == '*' and dp[0][i-1]:
            dp[0][i+1] = True
    for i in range(len(s)):
        for j in range(len(p)):
            if p[j] == '.' or p[j] == s[i]:
                dp[i+1][j+1] = dp[i][j]
            if p[j] in {'*', '?'}:
                if p[j-1] != s[i] and p[j-1] != '.':
                    dp[i+1][j+1] = dp[i+1][j-1]
                elif p[j] == '*':
                    dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j] or dp[i+1][j-1] 
                else:
                    #dp[i+1][j+1] =  
                    pass
    return not dp[-1][-1]

print(matches(".*", "ab"))
print(matches("a*", "aa"))
print(matches("c*a*b", "aab"))
print(matches("a?bc", "abc"))
print(matches("a?bc", "ac"))
print(matches("abd", "abc"))
