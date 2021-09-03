
# Written by Nicholas Johansan
# On 15th May 4:25PM

"""
references
+---------------------------------------------+
| Info Sheet                                  |
+------------+--------------------------------+
| Sides      | Pieces                         |
| B -> Black | P: Pawn  B: Bishop  Q: Queen   |
| W -> White | R: Rook  K: Knight  k: King    |
+------------+--------------------------------+

+-----+---------------------------------------+
|     |                                       |
|  8  | a8   b8   c8   d8   e8   f8   g8   h8 |
|     |                                       |
|  7  | a7   b7   c7   d7   e7   f7   g7   h7 |
|     |                                       |
|  6  | a6   b6   c6   d6   e6   f6   g6   h6 |
|     |                                       |
|  5  | a5   b5   c5   d5   e5   f5   g5   h5 |
|     |                                       |
|  4  | a4   b4   c4   d4   e4   f4   g4   h4 |
|     |                                       |
|  3  | a3   b3   c3   d3   e3   f3   g3   h3 |
|     |                                       |
|  2  | a2   b2   c2   d2   e2   f2   g2   h2 |
|     |                                       |
|  1  | a1   b1   c1   d1   e1   f1   g1   h1 |
|     |                                       |
|     +---------------------------------------+
|  r/                                         |
|  /f   a    b    c    d    e    f    g    h  |
|                                             |
+---------------------------------------------+

grid = [
	["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
	["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
	["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
	["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
	["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
	["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
	["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
	["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]
]
"""

from enum import Enum

class Side(Enum):
	B = "B"
	W = "W"

class Tile:
	def __init__(self, row_col):
		self.row_col = row_col
		self.row, self.col = row_col
		rank = 8-self.row
		file = chr(97+self.col)
		self.name = f"{file}{rank}"
		self.contain = None

class ChessPiece:
	def __init__(self, side, piece_name):
		self.side = side # B/W
		self.chess_piece = side.value + piece_name

class Pawn(ChessPiece):
	piece_name = "P"
	def __init__(self, side):
		ChessPiece.__init__(self, side, self.__class__.piece_name)
		self.has_moved = False
		self.dirn_value = 1 if side == Side.B else -1

	def get_all_possible_tiles(self, current_tile):
		row, col = current_tile
		possible_moves = []
		possible_moves.append((row + (1 * self.dirn_value), col))
		if not self.has_moved: possible_moves.append((row + (2 * self.dirn_value), col))
		return possible_moves


class Rook(ChessPiece):
	piece_name = "R"
	def __init__(self, side):
		ChessPiece.__init__(self, side, self.__class__.piece_name)
		self.has_moved = False

	def get_all_possible_tiles(self, current_tile):
		row, col = current_tile
		possible_moves = []
		for i in range(8):
			if i != row: possible_moves.append((i, col))
			if i != col: possible_moves.append((row, i))
		return possible_moves

class Knight(ChessPiece):
	piece_name = "K"
	def __init__(self, side):
		ChessPiece.__init__(self, side, self.__class__.piece_name)
		self.has_moved = False

	def get_all_possible_tiles(self, current_tile):
		row, col = current_tile
		possible_moves = []

		possible_moves.append((row-2, col-1))
		possible_moves.append((row-2, col+1))
		possible_moves.append((row+2, col-1))
		possible_moves.append((row+2, col+1))

		possible_moves.append((row-1, col+2))
		possible_moves.append((row-1, col-2))
		possible_moves.append((row+1, col+2))
		possible_moves.append((row+1, col-2))

		return possible_moves

class Bishop(ChessPiece):
	piece_name = "B"
	def __init__(self, side):
		ChessPiece.__init__(self, side, self.__class__.piece_name)
		self.has_moved = False

	def get_all_possible_tiles(self, current_tile):
		return []

class Queen(ChessPiece):
	piece_name = "Q"
	def __init__(self, side):
		ChessPiece.__init__(self, side, self.__class__.piece_name)
		self.has_moved = False

	def get_all_possible_tiles(self, current_tile):
		return []

class King(ChessPiece):
	piece_name = "k"
	def __init__(self, side):
		ChessPiece.__init__(self, side, self.__class__.piece_name)
		self.has_moved = False

	def get_all_possible_tiles(self, current_tile):
		row, col = current_tile
		possible_moves = []

		possible_moves.append((row-1, col+1))
		possible_moves.append((row-1, col))
		possible_moves.append((row-1, col-1))

		possible_moves.append((row, col+1))
		possible_moves.append((row, col-1))

		possible_moves.append((row+1, col+1))
		possible_moves.append((row+1, col))
		possible_moves.append((row+1, col-1))

		return possible_moves

class Game:

	board = """
+-----+---------------------------------------+
|     |                                       |
|  8  | a8   b8   c8   d8   e8   f8   g8   h8 |
|     |                                       |
|  7  | a7   b7   c7   d7   e7   f7   g7   h7 |
|     |                                       |
|  6  | a6   b6   c6   d6   e6   f6   g6   h6 |
|     |                                       |
|  5  | a5   b5   c5   d5   e5   f5   g5   h5 |
|     |                                       |
|  4  | a4   b4   c4   d4   e4   f4   g4   h4 |
|     |                                       |
|  3  | a3   b3   c3   d3   e3   f3   g3   h3 |
|     |                                       |
|  2  | a2   b2   c2   d2   e2   f2   g2   h2 |
|     |                                       |
|  1  | a1   b1   c1   d1   e1   f1   g1   h1 |
|     |                                       |
|     +---------------------------------------+
|  r/                                         |
|  /f   a    b    c    d    e    f    g    h  |
|                                             |
+---------------------------------------------+
"""
	info_sheet = """
+---------------------------------------------+
| Info Sheet                                  |
+------------+--------------------------------+
| Sides      | Pieces                         |
| B -> Black | P: Pawn  B: Bishop  Q: Queen   |
| W -> White | R: Rook  K: Knight  k: King    |
+------------+--------------------------------+"""

	def __init__(self):

		self.grid = self.__class__.get_default_grid()
		self.print_board()
		#print(self.get_movable_tiles())

	@staticmethod
	def get_default_grid():
		grid = []
		for row in range(8):
			grid.append([])
			for col in range(8):
				grid[row].append(Tile(row_col=(row, col)))

		for tile in grid[1]: tile.contain = Pawn(Side.B) # Position Black Pawns
		for tile in grid[6]: tile.contain = Pawn(Side.W) # Position White Pawns

		grid[0][0].contain = Rook(Side.B)
		grid[0][7].contain = Rook(Side.B)
		grid[7][0].contain = Rook(Side.W)
		grid[7][7].contain = Rook(Side.W)

		grid[0][1].contain = Knight(Side.B)
		grid[0][6].contain = Knight(Side.B)
		grid[7][1].contain = Knight(Side.W)
		grid[7][6].contain = Knight(Side.W)

		grid[0][2].contain = Bishop(Side.B)
		grid[0][5].contain = Bishop(Side.B)
		grid[7][2].contain = Bishop(Side.W)
		grid[7][5].contain = Bishop(Side.W)

		grid[0][3].contain = Queen(Side.B)
		grid[0][4].contain = King(Side.B)
		grid[7][3].contain = Queen(Side.W)
		grid[7][4].contain = King(Side.W)

		return grid

	def print_board(self):
		print(self.__class__.info_sheet) #print info sheet
		print(self.get_ascii_board(self.grid)) #print board

	@classmethod
	def get_ascii_board(cls, grid):
		ascii_board = cls.board
		for row in grid:
			for tile in row:
				ascii_board = ascii_board.replace(tile.name, "  " if tile.contain == None else tile.contain.chess_piece)
		return ascii_board

	def get_possible_movements(self, tile):
		if tile.contain == None: return []
		chess_piece = tile.contain
		possible_tiles = []
		for tile in chess_piece.get_all_possible_tiles(tile.row_col):
			row, col = tile
			if (row > 7 or row < 0) or (col > 7 or col < 0):
				continue
			elif (self.grid[row][col].contain != None):
				continue
			possible_tiles.append((row, col))
		return possible_tiles

	def get_movable_tiles(self):
		return list(filter(
			lambda movements: movements[0] != [],
			map(
				lambda tile: (self.get_possible_movements(tile), tile.name),
				[tile for row in self.grid for tile in row]
			)
		))


Game()