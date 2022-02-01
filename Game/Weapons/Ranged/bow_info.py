from Engine.info_node import Info_Node

class Bow_Info(Info_Node):
	def __init__(self, ID):
		Info_Node.__init__(self, ID=ID, groupID='#bow')

	def Bow_Data(self, attack, durability=None, rarity=None): #add more here as needed.
		self._baseAttack = attack
		self._durability = durability
		self._rarity	 = rarity
