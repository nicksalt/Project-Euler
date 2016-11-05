scoring={'A':1, 'B':2, 'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,
         'Q':17,'R':18,'S':19,'T':20,'U':21, 'V':22,'W':23,'X':24,'Y':25,'Z':26}
f=open('42.txt','r')
l=f.read().split(',')
f.close()

def tranglenums(limit):
    l=[1]
    n=2
    while l[len(l)-1]<limit:
        l.append(int(.5*n*(n+1)))
        n+=1
    return l[:len(l)-1]


scorelist=[]
triangles=0
nums=(tranglenums(26**2))
for i in l:
    word=i[1:len(i)-1]
    score = 0
    for letter in word:
        score+=scoring[letter]
    if score in nums:
        triangles+=1
print(triangles)

    

