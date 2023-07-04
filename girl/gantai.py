def find_buy_volumes(N, my_volumes, available_volumes):
    my_volumes = set(my_volumes)
    available_volumes = set(available_volumes)
    return sorted(available_volumes - my_volumes) or None


N = int(input())
M1 = int(input())
my_volumes = list(map(int, input().split()))
M2 = int(input())
available_volumes = list(map(int, input().split()))

print(
    " ".join(map(str, find_buy_volumes(N, my_volumes, available_volumes)))
    if find_buy_volumes(N, my_volumes, available_volumes)
    else "None"
)
