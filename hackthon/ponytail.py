def is_pass_test(d, e):
    return d == e


def eyesight_test():
    test_results = [input().split() for _ in range(5)]
    pass_count = sum(is_pass_test(d, e) for d, e in test_results)
    return "OK" if pass_count >= 3 else "NG"


if __name__ == "__main__":
    result = eyesight_test()
    print(result)
