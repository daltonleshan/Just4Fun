def isMagic(numbers, n, index, sum_so_far):
    if index < len(numbers):
        return isMagic(numbers, n, index + 1, sum_so_far + numbers[index])  or isMagic(numbers, n, index + 1, sum_so_far - numbers[index])
    if sum_so_far == n:
        return True
    return False

    
def isMagicNumber(numbers, n):
    # n is a magic number if we can insert + or - between numbers in arr to obtain n
    return isMagic(numbers, n, 0, 0)

print(isMagicNumber([1,2,3,4],2))
