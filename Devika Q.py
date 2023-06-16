f=open("Devika.txt","r")
a=f.read()
c=a.split()
n="Navya"
for i in c:
    if i==n:
        pass
    else:
        print(i)
f.close()