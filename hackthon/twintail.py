def f(s, t):
    return "-" * (t - 1) + "+" + "-" * (s - t)


s = int(input())
t = int(input())
result = f(s, t)
print(result)
