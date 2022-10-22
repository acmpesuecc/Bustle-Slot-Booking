"""
TicTacToe Player Module
Has a Player parent class, HumanPlayer, and AIPlayer
"""

import math
import pygame #python module used to build games
import time

class Player:
    """Player parent class"""
    def __init__(self) -> None: # -> is return annotation. Here, -> None indicates that the function returns nothing,i.e, None (but doesn't force it to return nothing)
        pass

    def set_symbol(self, symbol:str) -> None:
        """sets the object's sumbol to parameter.
        Param: String "X" or "O" """
        self.symbol = symbol

    def play(self, board) -> bool:
        pass

class HumanPlayer(Player): #HumanPlayer taking Player as an argument is an example of inheritance.
    #Here, HumanPlayer will inherit all the properties and methods of Player which is its parent class
    def __init__(self) -> None:
        super().__init__() #super() gives access to the __init__ defined in parent class

    def set_symbol(self, symbol) -> None:
        return super().set_symbol(symbol)

    def select(self,board) -> None:
        """Given a TicTacToe board, gives the current mouse position
        to select a slot."""
        pos = pygame.mouse.get_pos() #Allows us to find the coordinates of the mouse cursor everytime the cursor is moved
        board.select(pos)

    def play(self, board) -> bool:
        """Given a board, handles if the player selects or confirms a play.
        Returns True if player confirms play, else False.
        """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #quits the game if the pygame quit event is triggered
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN: #if a click is detected, the square that the mouse curosr was on is selected
                    self.select(board)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if board.add_at_selected(self.symbol): #adds the selected symbol at the selected square
                            return True
        return False

class AIPlayer(Player): #creates an AI Player that shares the same methods and properties as the Player class
    def __init__(self) -> None:
        super().__init__()

    def set_symbol(self, symbol) -> None:
        return super().set_symbol(symbol)

    def play(self, board) -> bool:
        """Given a board, AI uses Minimax algorithm to play optimal move.
        Returns True if player confirms play, else False."""
        copy = board.copy()
        time.sleep(.5)  # 0.5s pause so that the game is not updated instantly
        i = self.minimax(copy, -math.inf, math.inf, True, 0)
        board.add_at_i(self.symbol,i)
        return True


    def minimax(self, board, alpha: int, beta:int, maximizing:bool, depth: int) -> int:
        """Minimax algorithm with alpha-beta pruning to play best move for TicTacToe.
        No depth limit because Tictactoe is a simple game. Returns 
        best move index on first call, the other calls returns the evaluated value of branch.
        Params: TicTacToe object, max alpha, min beta, boolean representing turn, current depth.
        """
        winner = board.has_winner()
        if winner:
            if winner == self.symbol:
                return board.cur_capacity() + 1 # Uses capacity to favor wins with fewer turns
            elif winner != "D":
                return -1 * (board.cur_capacity() + 1)
            else:
                return 0

        if maximizing:
            max_eval = -math.inf
            best_idx = 0
            for i in range(9):
                if not board.add_at_i(self.symbol, i): continue
                eval = self.minimax(board, alpha, beta, False, depth +1)
                if (eval > max_eval):
                    best_idx = i
                    max_eval = eval
                board.delete_symbol(i)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            if depth == 0:
                return best_idx
            return max_eval
        else:
            min_eval = math.inf
            symbol = "O" if self.symbol == "X" else "X"
            for i in range(9):
                if not board.add_at_i(symbol, i): continue
                eval = self.minimax(board, alpha, beta, True, depth +1)
                min_eval = min(min_eval, eval)
                board.delete_symbol(i)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval