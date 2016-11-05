def longest_collatz():
    chain=10
    num=13
    for i in range(999999,100000,-2):
        n=i
        subchain=0
        while n!=1:
            if n%2==0:
                n=n/2
            else:
                n= 3*n+1
            subchain+=1
        if subchain>chain:
            chain = subchain
            num=i
    return num
            
        
