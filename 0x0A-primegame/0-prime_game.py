#!/usr/bin/python3

def isWinner(x, nums):
    def sieve_of_eratosthenes(limit):
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= limit:
            if primes[p]:
                for i in range(p * p, limit + 1, p):
                    primes[i] = False
            p += 1
        return [i for i in range(limit + 1) if primes[i]]

    def game_winner(n):
        primes = sieve_of_eratosthenes(n)
        return "Ben" if len(primes) % 2 == 0 else "Maria"

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = game_winner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Test the function
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))

