def largest_palindrome():
    largest=0
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            n=i*j
            if str(n) == str(n)[::-1]:
                if n>largest:
                    largest=n
    return largest
print(largest_palindrome())
