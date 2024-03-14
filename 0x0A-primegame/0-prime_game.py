#!/usr/bin/python3
'''Prime Game'''

def isWinner(x, nums):
    '''Finds the winner'''
    winnerCounter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        roundWinner = isRoundWinner(nums[i], x)
        if roundWinner is not None:
            winnerCounter[roundWinner] += 1

    if winnerCounter['Maria'] > winnerCounter['Ben']:
        return 'Maria'
    elif winnerCounter['Ben'] > winnerCounter['Maria']:
        return 'Ben'
    else:
        return None

def isRoundWinner(n, x):
    '''Finds the round winner'''
    number_list = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        # get current player
        currentPlayer = players[i % 2]
        selectedIdxs = []
        prime = -1
        for idx, num in enumerate(number_list):
            # if already picked prime num then
            # find if num is multiple of the prime num
            if prime != -1:
                if num % prime == 0:
                    selectedIdxs.append(idx)
            # else check if num is prime then pick it
            else:
                if isPrime(num):
                    selectedIdxs.append(idx)
                    prime = num
        # if failed to pick then current player lost
        if prime == -1:
            if currentPlayer == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            number_list = [num for idx, num in enumerate(number_list) if idx not in selectedIdxs]
    return None

def isPrime(n):
    '''Checks if a number is prime'''
    # 0, 1, even numbers greater than 2 are NOT PRIME
    if n <= 1 or (n > 2 and n % 2 == 0):
        return False
    else:
        # Not prime if divisible by another number less
        # or equal to the square root of itself.
        # n**(1/2) returns square root of n
        for i in range(3, int(n**(1/2)) + 1, 2):
            if n % i == 0:
                return False
        return True

