import numpy as np
board = np.full((3, 3),99, dtype=object)
def print_board(board):
    for row in board:
        print(" ".join(str(cell) if cell not in ['X', 'O'] else cell for cell in row))

def check_winner(board):
    for row in board:
        if np.all(row == 'X') or np.all(row == '0'):
            return row[0]
    
    for col in board.T:  # board.T là ma trận chuyển vị
        if np.all(col == 'X') or np.all(col == '0'):
            return col[0]
    
    if np.all(np.diag(board) == 'X') or np.all(np.diag(board) == '0'):
        return board[0, 0]
    
    if np.all(np.diag(np.fliplr(board)) == 'X') or np.all(np.diag(np.fliplr(board)) == '0'):
        return board[0, -1]
    
    return None

def play_game():
    board = np.full((3, 3), 99, dtype=object)
    players = ['X', '0']
    turn = 0  # X đi trước
    
    while True:
        print_board(board)
        print(f"Lượt của {players[turn]}:")
        
        try:
            row, col = map(int, input("Nhập vị trí (row, col): ").split())
            
            if board[row, col] in ['X', '0']:  # Kiểm tra ô trống
                print("Vị trí đã có, hãy nhập lại!")
                continue
            
            board[row, col] = players[turn]
            
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Người chơi {winner} thắng!")
                break
            
            turn = 1 - turn  # Chuyển lượt cho người chơi còn lại
        except Exception:
            print("Lỗi nhập liệu, hãy nhập lại!")
            continue

if __name__ == "__main__":
    play_game()
      