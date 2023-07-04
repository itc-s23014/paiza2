def calculate_steps(M, N):
    result = M - N
    if result <= 0:
        result = 0
    return result


input_values = input().split()
M = int(input_values[0])
N = int(input_values[1])

output = calculate_steps(M, N)
print(output)
