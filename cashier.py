

def num_coins(cents):  
    coins = [25,10,5, 1]
    num_of_coins = {'total': float('inf')}
    for i in range(len(coins)):
        cents_copy = cents
        temp = {25:0, 10:0, 5:0, 1:0, 'total': 0}
        for coin in coins:
            temp['total'] += cents_copy//coin
            temp[coin] += cents_copy//coin
            cents_copy = cents_copy % coin
        if (temp['total'] < num_of_coins['total']):
            num_of_coins = temp
        
        coins = coins[-1:] + coins[:-1]
        #shift coins once
    
    print('cents',cents)
    print(num_of_coins)
    
    
    
num_coins(125)