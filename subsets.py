def subsets(arr):
    if arr is None or len(arr) == 0:
        return []
    ans = [[]]
    for n in arr:
        ans += [m + [n] for m in ans]
    return ans

print(subsets([1,2,3]))
print(subsets([5,2,4]))
