from Engine.timer_node import Timer_Node
from Engine.image_node import Image_Node
from Engine.main_node import Main_Node

#Parent: Main_Node
#Children:
	#Projectile_Main
	#Sword_Main
	#Bow_Main

class Weapons_Main(Main_Node):
	def __init__(self, info, cLogic=None, cNode=None, iNode=None, tNode=None):
		Main_Node.__init__(self, info=info, cLogic=cLogic, cNode=cNode, iNode=iNode, tNode=tNode)
		self._isActive = False


	def Weapon_Active(self):
		if Timer_Node.GameTime == (self._saveTime+9):
			Image_Node.Render.delete(self._info.get_ID())
			self._isActive = False

	def Del_Item(self):
		self._isActive = False
		Image_Node.Render.delete(self._info.get_ID())
		self._cLogic.Del_CollisionDict(tagOrId=self._info.get_ID())


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...

	def get_isActive(self):
		return self._isActive
