f=open("Archana.txt")
lines=0
letters=0
words=0
for i in f:
    lines=lines+1
    letters=letters+len(i.strip())
    words=words+len(i.split())
print("Lines=",lines)
print("Letters=",letters)
print("Words=",words)