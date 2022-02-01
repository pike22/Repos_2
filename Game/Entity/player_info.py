from Engine.info_node import Info_Node

class Player_Info(Info_Node):
	def __init__(self):
		Info_Node.__init__(self, ID='P#001', groupID='#player')


	def Player_Data(self, coords, speed, health, defense, attack): #add more here as needed.
		self._baseDefense	= defense
		self._baseHealth	= health
		self._baseAttack	= attack
		self._myCoords		= coords
		self._speed			= speed
