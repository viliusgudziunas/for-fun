# https://www.youtube.com/watch?v=HWW-jA6YjHk&list=WL&index=5&t=0s


def num_coins(cents, coins):
    if cents < 1:
        return 0
    num_of_coins = 0
    for coin in coins:
        num_of_coins += cents // coin
        cents = cents % coin
        if cents == 0:
            break
    return num_of_coins


def min_coins(cents):
    if cents < 1:
        return 0
    coins = [25, 10, 1]
    min_number_of_coins = 999999999
    while len(coins) > 0:
        new_min = num_coins(cents, coins)
        if new_min < min_number_of_coins:
            min_number_of_coins = new_min
        coins = coins[1:]

    return min_number_of_coins


print(min_coins(70))
