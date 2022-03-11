def fastFib(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n - 1, memo) + fastFib(n-2, memo)
        memo[n] = result;
        return result

print(fastFib(990))
print('\n')
def fastFib2(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    elif n in memo.keys():
        return memo[n]
    else:
        result = fastFib2(n - 1, memo) + fastFib2(n-2, memo)
        memo[n] = result;
        return result

print(fastFib2(990))
