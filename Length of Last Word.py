def lengthOfLastWord(s):
    s = s.split()
    p = len(s) - 1
    i = len(s[p])
    return i

t1 = "   fly me   to   the moon  "
t2 = "Today is a nice day"
print(lengthOfLastWord(t2))
