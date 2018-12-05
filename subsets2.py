def subsets(arr):
    if arr is None or len(arr) == 0:
        return {} 
    ans = [[]] 
    for n in arr:
        ans += [m + [n] for m in ans]
ret = set()
for l in ans:
ret.add(tuple(l))
return ret

print(subsets([1,2,2]))
print(subsets([5,2,2]))
