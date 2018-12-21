def hangman(word):
    # 変数宣言
    wrong_count = 0                     # プレイヤーが間違えた回数
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rest_letters = list(word)           # まだ当てられていない文字のリスト
    score_board = ["_"] * len(word)     # プレイヤーに表示する一部が隠された単語
    win = False                         # プレイヤーが勝ったかどうか保持するフラグ

    # ゲーム開始
    print("ハングマンへようこそ！")
    while wrong_count < len(stages) - 1:
        # 1文字入力
        print("\n")
        message = "１文字予想してね"
        guess_char = input(message)

        # 変数の更新
        if guess_char in rest_letters:  # 正解
            guess_index = rest_letters.index(guess_char)
            score_board[guess_index] = guess_char
            rest_letters[guess_index] = '$'
        else:                           # 不正解
            wrong_count += 1

        # 途中結果の表示
        print(" ".join(score_board))
        print("\n".join(stages[0:wrong_count+1]))

        if "_" not in score_board:
            win = True
            break

    # 最終結果の表示
    if win:
        print("あなたの勝ち！")
        print(" ".join(score_board))
    else:
        print("\n".join(stages[0:wrong_count+1]))
        print("あなたの負け！正解は {}.".format(word))

hangman("cat")
