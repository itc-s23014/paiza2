def check_candy_pack(n, m):
    return "ok" if m % n == 0 else "ng"


n, m = map(int, input().split())
result = check_candy_pack(n, m)
print(result)
