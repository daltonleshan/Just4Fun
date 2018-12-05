#lowercase and uppercase combination

def permute(string):
    inp = string.lower()
    n = len(inp)
    perms = 1 << n
    for i in range(perms):
        combinations = [c for c in inp]
        for j in range(n):
            print(i, j, i >> j)
            if ((i >> j) & 1):
                combinations[j] = inp[j].upper()
        print(''.join(combinations))

permute("AB")
