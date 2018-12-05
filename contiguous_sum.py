def printContigSum(nums, target):
    if nums is None:
        return
    nums.sort()
    def dfs(nums, target, path, index):
        if target < 0:
            return
        if target == 0:
            print(path)
            return
        print('path ', path)
        for i in range(index, len(nums)):
            dfs(nums, target - nums[i], path + [nums[i]], i)
    dfs(nums, target, [], 0)

print(printContigSum([1,2,3], 3))

