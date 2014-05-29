from ChessPiece import ChessPiece
import sys


class Bing(ChessPiece):

    def get_image_file_name(self):
        if self.selected:
            if self.is_red:
                return "images/RPS.gif"
            else:
                return "images/BPS.gif"
        else:
            if self.is_red:
                return "images/RP.gif"
            else:
                return "images/BP.gif"

    def get_move_locs(self):
        return []
        return [(self.x, self.y+1)]

    def move(self, board, dx, dy):
        if abs(dx) + abs(dy) != 1:
            print 'Too far'
            return False
        if (self.is_red and dy == -1) or (self.is_red == False and dy==1):
            print 'cannot go back'
            return False
        if dy == 0:
            if (self.is_red and self.y <5) or (self.is_red == False and self.y >=5):
                'behind river'
                return False
        nx, ny = self.x + dx, self.y + dy
        if (nx, ny) in board.pieces:
            if board.pieces[nx, ny].is_red == self.is_red:
                print 'blocked by yourself'
                return False
            else:
                print 'kill a chessman'
                board.remove(nx, ny)
        return ChessPiece.move(self, board, dx, dy)

    def __init__(self, x, y, is_red):
        ChessPiece.__init__(self, x, y, is_red)

    def display(self):
        sys.stdout.write('B')