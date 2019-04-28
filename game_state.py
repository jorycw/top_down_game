

class Game_State():

	def __init__(self, id, players, projectiles):
		self.id = id
		self.players = players
		self.projectiles = projectiles

	def get_p(self):
		return self.players[self.id]
