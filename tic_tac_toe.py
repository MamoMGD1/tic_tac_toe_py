import random, math, time, csv
class Globals:
    game_board = []
    records = []
    temp_records = []
    training_times = 0
    training = False
    player1, player2, winner = '','AI',''
    p1_turn = True
class Record:
    def __init__(self, board, move='',score=0):
        self.board = board
        self.move = move
        self.score = score
def initialize():
    Globals.game_board=[i for i in range(9)]
    Globals.player1 = 'AI_Trainer' if Globals.training else 'Human'
    Globals.winner = ''
    Globals.p1_turn = True
def print_board():
    print("\n")
    for i in range(3):
        row = " | ".join(str(Globals.game_board[i * 3 + j]) for j in range(3))
        print(" " + row)
        if i < 2:
            print("---|---|---")  # Horizontal separator
    print("\n")
def check_winner(arr=None):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    if arr is None:
        arr=Globals.game_board
    # Check for a winner
    for combo in winning_combinations:
        if arr[combo[0]] == arr[combo[1]] == arr[combo[2]] != '':
            if arr[combo[0]] == 'O':
                return Globals.player1
            elif arr[combo[0]] == 'X':
                return Globals.player2
    
    if all(isinstance(x, str) for x in arr):
        return 'Draw'
    return ''
def possible_moves(arr=None):
    if arr is None:
        arr = Globals.game_board
    return [i for i in range(9) if isinstance(arr[i], int)]

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == Globals.player2:  # AI wins
        return 10 - depth
    elif winner == Globals.player1:  # Human wins
        return depth - 10
    elif winner == "Draw":  # Draw
        return 0
    moves = possible_moves(board).copy()
    random.shuffle(moves)
    if is_maximizing:  # AI's turn
        max_eval = -math.inf
        for new_move in moves:
            board[new_move] = 'X'
            eval = minimax(board[:], depth + 1, False)
            board[new_move] = new_move  # Undo move
            max_eval = max(max_eval, eval)
        return max_eval
    else:  # Human's turn
        min_eval = math.inf
        for new_move in moves:
            board[new_move] = 'O'
            eval = minimax(board[:], depth + 1, True)
            board[new_move] = new_move  # Undo move
            min_eval = min(min_eval, eval)
        return min_eval

def ai_move():
    if len(Globals.records) > 0 and not Globals.training:
        max_score = -math.inf
        best_move = ''
        for record in Globals.records:
            if record.board == ''.join(map(str, Globals.game_board)) and record.score > max_score:
                max_score = record.score
                best_move = record.move
        if best_move:
            print("Found A Smart Move!🧠")
            return best_move

    # Minimax decision-making
    best_score = -math.inf
    best_move = None
    temp_board = Globals.game_board[:]
    moves = possible_moves(temp_board).copy()
    random.shuffle(moves)
    for move in moves:  
        temp_board[move] = 'X'  # Simulate AI move
        move_score = minimax(temp_board, 0, False)  # Evaluate the move
        temp_board[move] = move  # Undo move

        if move_score > best_score:
            best_score = move_score
            best_move = move

    if best_move is not None:
        return best_move
    
    return random.choice(moves)

def human_move():
    move = ''
    while True:
        move = int(input("Enter Your Move: "))
        if move in possible_moves():
            break
        print("Invalid Move!❌")
    return move

def proceed_game():
    if Globals.p1_turn:
        Globals.game_board[ai_move() if Globals.training else human_move()]='O'
    else:
        move = ai_move()
        Globals.game_board[move]='X'
        if not Globals.training:
            print(f"AI's Move: {move}")
        else:
            Globals.temp_records[len(Globals.temp_records)-1].move = move
    Globals.p1_turn = not Globals.p1_turn

#Phase 1: Training
Globals.training_times = int(input("How Many Times Should I Train? "))
if Globals.training_times>0 and input("Can I Use External Data To Train?(Y/N) ").capitalize=="Y":
    with open("tic_tac_toe.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            Globals.records.append(Record(row["Board"],int(row["move"]),int(row["Score"])))
if Globals.training_times!=0: Globals.training = True
progress_bar=['_' for _ in range(30)]
for _ in range(Globals.training_times):
    initialize()
    Globals.temp_records = []
    while not Globals.winner:
        if not Globals.p1_turn: Globals.temp_records.append(Record(''.join(map(str,Globals.game_board))))
        proceed_game()
        Globals.winner = check_winner()
        if Globals.winner==Globals.player1:
            for i in range(len(Globals.temp_records)):
                Globals.temp_records[i].score-=10
        elif Globals.winner==Globals.player2:
            for i in range(len(Globals.temp_records)):
                Globals.temp_records[i].score+=10
        elif Globals.winner=='Draw':
            for i in range(len(Globals.temp_records)):
                Globals.temp_records[i].score-=3
    for temp_record in Globals.temp_records:
        for record in Globals.records:
            if record.board == temp_record.board and record.move == temp_record.move:
                record.score+=temp_record.score
                break
        else:
            Globals.records.append(temp_record)
    progress_bar[math.floor(_/Globals.training_times*30)] = "■"
    print(f"[{''.join(progress_bar)}] Training ({_+1:04})/({Globals.training_times})", end="\r")
    time.sleep(0.01)
if Globals.training:
    Globals.training = False
    print("\033[K",end="\r")
    print("Training Done!✅")
    #Exporting Data To A .csv File
    with open("tic_tac_toe.csv","w",newline="") as file:
        writer = csv.DictWriter(file,fieldnames=["Board","Move","Score"])
        writer.writeheader()
        writer.writerows([{"Board":r.board, "Move":r.move, "Score":r.score} for r in Globals.records])
print(f"{len(Globals.records)} Data Have Been Imported!")
for _ in range(len(Globals.records)):
    if Globals.records[_].score>=50:
        print(f"{Globals.records[_].board} Move: {Globals.records[_].move} Score: {Globals.records[_].score}")

#Phase 2: Playing The Game
for _ in range(int(input("How Many Games Shall We Play? "))):
    initialize()
    print_board()
    while not Globals.winner:
        proceed_game()
        print_board()
        Globals.winner = check_winner()
        if Globals.winner==Globals.player1:
            print(f"'{Globals.winner}' Is The Winner👦\n-------------------------")
        elif Globals.winner==Globals.player2:
            print(f"'{Globals.winner}' Is The Winner🤖\n-------------------------")
        elif Globals.winner=='Draw':
            print("Round Draw!🤝\n-------------------------")