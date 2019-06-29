class TicTacToeBoard:
	def __init__(self,start='O'):
		self._board=[[' ']*3 for i in range(3)]
		self._Mark=[None,'O','X']
		dic={'O':1,'X':-1}
		self._i=dic[start]
	def mark(self,x,y):
		self._board[x][y]=self._Mark[self._i]
		self._i*=-1
		print(self.__str__())
		print()
	def _iswin(self,mark):
		board=self._board
		return (mark == board[0][0] == board[0][1] == board[0][2] or 
		mark == board[1][0] == board[1][1] == board[1][2] or # row 1
		mark == board[2][0] == board[2][1] == board[2][2] or # row 2
		mark == board[0][0] == board[1][0] == board[2][0] or # column 0
		mark == board[0][1] == board[1][1] == board[2][1] or # column 1
		mark == board[0][2] == board[1][2] == board[2][2] or # column 2
		mark == board[0][0] == board[1][1] == board[2][2] or # diagonal
		mark == board[0][2] == board[1][1] == board[2][0]) 
	def winner(self):
		for mark in 'XO':
			if self._iswin(mark):
				string='The winner is :'+ mark
				return string
		return None
	def __str__(self):
		rows=['|'.join(self._board[r]) for r in range(3)]
		return '\n------\n'.join(rows)
game=TicTacToeBoard()
game.mark(1,1)
game.mark(0,2)
game.mark(0,0)
game.mark(0,1)
game.mark(2,2)
print(game.winner())
print(game)