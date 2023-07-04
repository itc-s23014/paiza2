def f(n, m, songs):
    total_time = 0
    for i in range(m):
        total_time += songs[i]
        if total_time > n * 60:
            return i
    return "OK"


n = int(input())
m = int(input())
songs = [int(input()) for _ in range(m)]
result = f(n, m, songs)
print(result)
