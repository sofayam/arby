alifba = [
"'",
'a',
'b',
't',
'_t',
'j',
'^g',
'.h',
'_h',
'd',
'_d',
'r',
'z',
's',
'^s',
'.s',
'.d',
'.t',
'.z',
'`',
'.g',
'f',
'q',
'k',
'l',
'm',
'n',
'h',
'u',
'w',
'i',
'y',
'_A',
'T']

ord = {}
index = 1
for letter in alifba:
    ord[letter] = index
    index += 1
    

def getletter(s):
    for letter in alifba:
        if s[:len(letter)] == letter:
            return letter
    raise "No Letter found for %s" % s

def nextletter(l,s):
    return s[len(l):]

def arabic_compare(s1,s2):
    if s1 == s2: return 0
    l1 = getletter(s1)
    l2 = getletter(s2)
    if ord[l1] < ord[l2]:
        return -1
    elif ord[l1] > ord[l2]:
        return 1
    elif (nextletter(l1,s1) == "") and (nextletter(l2,s2) == ""): 
        return 0
    elif (nextletter(l1,s1) == ""):
        return -1
    elif (nextletter(l2,s2) == ""):
        return 1
    else:
        return arabic_compare(nextletter(l1,s1),nextletter(l1,s2))
    

