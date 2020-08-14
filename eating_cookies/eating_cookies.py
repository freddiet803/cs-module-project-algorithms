'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, cache={}):
    denominations = [1, 2, 3]
    # Your code here
    '''cache = [0 for i in range(n+1)]
    cache[0] = 1

    for denom in denominations:
        for n in range(denom, n + 1):
            cache[n] = cache[n] + cache[n - denom]

    return cache[n]'''
    if n < 0:
        return 0
    if n <= 1:
        return 1
    if n not in cache:
        cache[n] = eating_cookies(
            n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
