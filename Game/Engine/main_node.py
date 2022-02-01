from .node import Node
from .kinetics_node import Kinetics_Node

#Parent: Node
#Children:
	#Weapons_Main
	#Entity_Main
	#Button_Main
	#Placed_ImageMain

class Main_Node(Node):
	def __init__(self, info, cLogic=None, cNode=None, iNode=None, tNode=None):
		Node.__init__(self, cLogic=cLogic, cNode=cNode, iNode=iNode, tNode=tNode)
		self._info = info
		self._saveTime	= 0



	def Info_Print(self, Name):
		#list of prints for start of program(CPU_Stalfoss)
		print('-----------------------------------')
		print(str(Name)+'Data:')
		print(self._info.get_ID(), '\t:Entity ID')
		print(self._info.get_speed(), 	'\t:Speed')
		print(self._info.get_health(),	'\t:Health')
		print(self._info.get_defense(),'\t:Defense')
		print(self._info.get_attack(),	'\t:Attack')
		print('\nParameters:')
		print(self._info.get_size(), 	'\t\t:Size')
		print(self._info.get_myCoords(), 	'\t\t:Coords')
		print(self._info.get_myCorners(), 	'\t:Corners')
		print(self._info.get_rarity(), '\t:Rarity')
		print(self._info.get_)
		print('-----------------------------------\n')


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_size(self):
		return self._info.get_size()

	def get_myCorners(self):
		return self._info.get_myCorners()

	def get_myCoords(self):
		return self._info.get_myCoords()

	def get_canCollide(self):
		return self._info.get_canCollide()

	#--ID's, fileLocations, Rotation--#
	def get_ID(self):
		return self._info.get_ID()

	def get_groupID(self):
		return self._info.get_groupID()

	def get_buttonID(self):
		return self._info.get_buttonID()

	def get_fileLoc(self):
		return self._info.get_fileLoc()

	def get_rotation(self):
		return self._info.get_rotation()


		#_attack, health, defense_#
	def get_attack(self):
		return self._info.get_attack()

	def get_health(self):
		return self._info.get_health()

	def get_defense(self):
		return self._info.get_defense()
