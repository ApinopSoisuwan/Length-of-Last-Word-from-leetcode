def lengthOfLastWord(s):
    s = s.split()
    c = []
    for i in s:
        c.append(len(i))
    return ((c[::-1][0]))

t1 = "   fly me   to   the moon  "
t2 = "Today is a nice day"
print(lengthOfLastWord(t2))
