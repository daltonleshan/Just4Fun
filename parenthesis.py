def permutations(n):
    def recurse(perm, left, right):
        if len(perm) == n * 2:
            print(perm)
            return
        if left < n:
            recurse(perm + '(', left + 1, right)
        if right < left:
            recurse(perm + ')', left, right + 1)

    recurse('', 0, 0)

permutations(3)
