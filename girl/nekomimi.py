import re


def count_cat_occurrences(S):
    count = len(re.findall("cat", S))
    return count


S = input().rstrip()

print(count_cat_occurrences(S))
