# frequency of character
L = "Python is very easy language"
d = {}
d.keys()
for i in L.split():
    keys = d.keys()
    if i in keys:
        d[i]+=1
    else:
        d[i] = 1
print(d)

