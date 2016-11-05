coins=[1,2,5,10,20,50,100,200]


def Summing(coins, amount):
    ways=[0]*(amount+1)
    ways[0]=1
    for coin in coins:
        for i in range(coin, amount+1):
            ways[i]+=ways[i-coin]
    return ways[amount]
print(Summing(coins, 200))
