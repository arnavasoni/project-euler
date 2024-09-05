def count_ways_to_make_200p():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]  # Available coins in pence
    target = 200  # £2 is 200 pence
    dp = [0] * (target + 1)  # Create a DP array initialized to 0
    dp[0] = 1  # There's one way to make 0p, by using no coins

    # For each coin, update the DP table
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    return dp[target]

# Output the result
print("Number of ways to make £2:", count_ways_to_make_200p())
