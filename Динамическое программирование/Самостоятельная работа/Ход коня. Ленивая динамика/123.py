import pprint
def knapsack(values, weights, W):
    n = len(values)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    item = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                if dp[i - 1][w - weights[i - 1]] + + values[i - 1] > dp[i-1][w]:
                # dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
                dp[i][w] = dp[i - 1][w - weights[i - 1]] + values[i - 1]
                if item[i][w]:
                    item[i][w].append(i)
                else:
                    item[i][w] = [i]
            else:
                dp[i][w] = dp[i - 1][w]

    return dp, item


if __name__ == '__main__':
    #values = [120, 100, 150]
    values = [100, 150, 120] *3
    weights = [2, 3, 1]*3
    W = 10
    pprint.pprint(knapsack(values, weights, W))




import pprint
def knapsack(values, weights, W):
    n = len(values)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp


if __name__ == '__main__':
    #values = [120, 100, 150]
    values = [100, 150, 120] *3
    weights = [2, 3, 1]*3
    W = 10
    pprint.pprint(knapsack(values, weights, W))