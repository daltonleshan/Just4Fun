def calculator(prefix, string):
    if string == '':
        print(prefix)
    else:
        for i,c in enumerate(string):
            calculator(prefix + c, string[:i] + string[i+1:])

def permutation(string):
    calculator("", string)


permutation('ab')
permutation('abc')
