arrange = {
    "1": ".",
    "2": ".",
    "3": ".",
    "4": ".",
    "5": ".",
    "6": ".",
    "7": ".",
    "8": ".",
    "9": ".",
}


def board(arrange):
    print(f"{arrange['1']} | {arrange['2']} | {arrange['3']}")
    print("--+" * 3)
    print(f"{arrange['4']} | {arrange['5']} | {arrange['6']}")
    print("--+" * 3)
    print(f"{arrange['7']} | {arrange['8']} | {arrange['9']}")


def play():
    players = ["o", "x"]
    current_player = players[0]

    def check_win(arrange, current_player):
        win_patterns = [
            ("1", "2", "3"),
            ("4", "5", "6"),
            ("7", "8", "9"),  # Rows
            ("1", "4", "7"),
            ("2", "5", "8"),
            ("3", "6", "9"),  # Columns
            ("1", "5", "9"),
            ("3", "5", "7"),
        ]  # Diagonals
        for pattern in win_patterns:
            if all(arrange[pos] == current_player for pos in pattern):
                return True
        return False

    board(arrange)

    for j in range(9):
        while True:
            message = input(f"Player {current_player}, enter a position (1-9): ")
            if message in arrange and arrange[message] == ".":
                break
            elif message in arrange and arrange[message] != ".":
                print("Position already taken. Try again.")
                board(arrange)
            else:
                print("Invalid input. Try again.")

        arrange[message] = current_player
        board(arrange)

        if check_win(arrange, current_player):
            board(arrange)
            print(f"Player {current_player} wins!")
            break

        if "." not in arrange.values():
            board(arrange)
            print("It's a draw!")
            break

        current_player = players[1] if current_player == players[0] else players[0]


play()
