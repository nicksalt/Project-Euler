def pentagonal(num):
    candidate=((24*num+1)**.5+1)/6
    return candidate==int(candidate)

def find():
    for k in range(1,10000):
        for j in range(k-1, 0, -1):
            pj=j*(3*j-1)/2
            kj=k*(3*k-1)/2
            s=pj+kj
            if pentagonal(s):
                d=abs(kj-pj)
                if pentagonal(d):
                    return (int(d), k, j)
           
print(find())
