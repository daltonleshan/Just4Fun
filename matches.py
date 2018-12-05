def matches(p, s):
    m = len(s)
    n = len(p)
    p = p[::-1]
    s = s[::-1]
    dp = [[False] * (n+1) for _ in range(m+1)]
    dp[0][0] = True
    special = {'*', '?', '+'}
    for i in range(2,n+1):
        dp[0][i] = dp[0][i-2] and p[i-1] in special 
    for i in range(1,m+1):
        for j in range(1,n+1):
            if p[j-1] in {'.', s[i-1]}:
                dp[i][j] = (s[i-1] == p[j-1] or p[j-1] == ".") and dp[i-1][j-1]  
            else:
                match = p[j-2] in {s[i-1], '.'}
                if p[j-1] == '*':
                    dp[i][j] = (j > 1 and dp[i][j-2]) or (dp[i-1][j] and match)
                elif p[j-1] == '?':
                    dp[i][j] = match and dp[i-1][j] or dp[i][j-2] 
                else:
                    dp[i][j] = match and dp[i][j-1] and j <= i+1 
    return dp[m][n]

assert(matches("",""))
assert(matches(".","a"))
assert(matches("",""))
assert(matches("+aab", "aab"))
assert(matches("*a", "aa"))
assert(matches("a*b*c", "abc"))
assert(matches("ab?bc", "abc"))
assert(matches("a?a?d", "a"))
assert(matches("a.c", "abc"))
assert(matches("a?bbc", "abc"))
assert(matches("?aab", "ab"))
assert(matches("ERROR: *.", "ERROR: file not found"))

assert(not matches(".",""))
assert(not matches("?",""))
assert(not matches("+",""))
assert(not matches("*",""))
assert(not matches("+aaab", "aab"))
assert(not matches("abbb?bc", "abc"))
assert(not  matches("ERROR: *.", "ERRROR: file not found"))
