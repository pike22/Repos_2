from Engine.info_node import Info_Node

class Arrow_Info(Info_Node):
	def __init__(self, ID):
		Info_Node.__init__(self, ID=ID, groupID='#arrow')

	def Arrow_Data(self, attack, coords, speed ,durability=None, rarity=None):
		self._durability  = durability
		self._baseAttack  = attack
		self._myCoords	  = coords
		self._rarity	  = rarity
		self._speed	  	  = speed
