from collections import Counter


def count_votes(votes):
    yes_count = votes.count("yes")
    no_count = votes.count("no")

    if yes_count > no_count:
        return "yes"
    else:
        return "no"


def main():
    votes = [input() for _ in range(5)]
    result = count_votes(votes)
    print(result)


if __name__ == "__main__":
    main()
