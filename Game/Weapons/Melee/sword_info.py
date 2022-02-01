from Engine.info_node import Info_Node

class Sword_Info(Info_Node):
	def __init__(self, ID):
		Info_Node.__init__(self, ID=ID, groupID='#sword')

	def Sword_Data(self, attack ,durability=None, rarity=None): #add more here as needed.
		self._durability = durability
		self._baseAttack = attack
		self._rarity 	 = rarity
