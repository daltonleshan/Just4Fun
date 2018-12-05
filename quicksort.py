def partition(numbers, l, r):
    pivot = numbers[r]
    i = 0
    for j in range(r):
        if numbers[j] <= pivot:
            numbers[j], numbers[i] = numbers[i], numbers[j]
            i += 1
    numbers[i], numbers[r] = numbers[r], numbers[i]
    return i

    
def quicksort(numbers, l, r):
    if l < r:
        pi = partition(numbers, l, r)
        quicksort(numbers, l, pi - 1)
        quicksort(numbers, pi + 1, r)
    return numbers

a = [3,1,4,9,6]
b = [6,9,1,3,4]

print(quicksort(a, 0, len(a) - 1))
print(quicksort(b, 0, len(b) - 1))

