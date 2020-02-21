def is_anagram(w1,w2):
    a = {}
    for c in w1.lower():
        if c == ' ': continue
        if c not in w2: return False
        if c in a: a[c] += 1
        else: a[c] = 1
    for c in w2.lower():
        if c == ' ': continue
        if c not in a: return False
        if a[c] == 0: return False
        a[c] -= 1
    return True
##print(is_anagram('nag a ram','anaxgram'))

keyL = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
keyD = {' ': 0, 'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4, 'i': 4, 'j': 5, 'k': 5, 'l': 5, 'm': 6, 'n': 6, 'o': 6, 'p': 7, 'q': 7, 'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8, 'w': 9, 'x': 9, 'y': 9, 'z': 9}

def to_dict(keyL):
    ans = {}
    for idx in range(len(keyL)):
        for c in keyL[idx]:
            ans[c] = idx
    return ans

def to_nums(word):
    ans = ''
    for c in word:
        ans += str(keyD[c])
    return ans

def to_letters(num):
    globalPool = ['']
    while num > 0:
        d = num % 10
        num //= 10
        tempArr = []
        for c in keyL[d]:
            tempArr += list(map(lambda x: c + x,globalPool))
        globalPool = tempArr
    return globalPool

##x = int(to_nums('i luv u'))
##print(x)
##print(len(to_letters(x)))





