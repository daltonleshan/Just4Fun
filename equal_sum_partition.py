def find(nums):
    sum_t = 0
    if nums is None or len(nums) < 2:
        return sum_t
    
    n = len(nums)
    for i in range(n):
        sum_t += nums[i]
        sum_sub = 0
        for j in range(i+1, n):
            sum_sub += nums[j]
            if not (j + 1) % (i + 1):
                print("J: ", j, "I: ", i, sum_sub, sum_t)
                if sum_sub != sum_t:
                    break
                if j == n-1:
                    return sum_t
                sum_sub = 0
    return sum_t

a = [1,3,2,2,2,3,2,1]
b = [1,3,2,2,1,3]

#print(find(a))
print(find(b))
