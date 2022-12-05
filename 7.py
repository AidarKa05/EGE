from itertools import product, permutations
s = map(''.join, (product(sorted('МСТФ'), repeat=4)))
#s = list(filter(lambda x: x.count('А') == 1, s))
s = list(s)
print(s)
ln = len(s)
print(ln)
print(s[137])
'''for i in range(ln):
    w = s[i]
    if w.count('Ы') == 0 and w.count('АА') == 0:
        print(i)
        print(w)
        break'''
