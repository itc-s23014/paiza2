def countdown(n):
    if n == 0:
        return ["0!!"]
    else:
        return [str(n)] + countdown(n - 1)


n = int(input())
output = countdown(n)
print("\n".join(output))
