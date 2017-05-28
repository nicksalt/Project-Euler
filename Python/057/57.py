# Noticed pattern in numerator and denominator

numerator = 3
denominator = 2
more_digits = 0
for i in range(1,1000):
    denominator = numerator + denominator
    numerator = denominator + (denominator - numerator)
    if len(str(numerator)) > len(str(denominator)):
        more_digits+=1
print(more_digits)