def concatenate_words():
    n = int(input())  # 単語の総数を入力
    words = [input() for _ in range(n)]  # n個の単語を入力
    return "_".join(words)  # 単語を'_'で繋ぎ合わせて結果を返す


result = concatenate_words()
print(result)
