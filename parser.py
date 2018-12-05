
def splitter(string):
    split = string.split(',')
    n = len(split)
    j = 0
    ans = []
    while j < n:
        char = split[j].strip()
        print(char, j)
        if char == '':
            pass
        elif char[0] == '"':
            curr = ''
            while char[len(char) - 1] != '"':
                curr += char + ','
                j += 1
                char = split[j]
            curr += char
            to_add = ''
            i = 0
            while i < len(curr) - 1:
                lock = curr[i] == '"' and curr[i] == curr[i+1]
                if curr[i] == '"':
                    to_add += curr[i + 1]
                    i += 2 
                else:
                    to_add += curr[i]
                    i += 1
            ans.append(to_add[:len(curr) - 1])
        else:
            ans.append(char)
        j += 1
    return ans


while True:
    try:
        s = input()
    except EOFError:
        break
    ans = splitter(s)
    buff = "{}, {} years old, is from {} and is interested in {}.\n"
    n = len(ans)
    interest = (n - 4) if n % 7 == 0 else (n - 3)
    print(buff.format(ans[0], ans[n-1], ans[n-2], ans[interest])) 
