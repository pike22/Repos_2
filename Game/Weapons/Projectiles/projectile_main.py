from Engine.image_node import Image_Node
from ..weapons_main import Weapons_Main

#Parent: Weapons_Node
#Children:
	#Arrow_Main

class Projectile_Main(Weapons_Main):
	def __init__(self, info, cLogic=None, cNode=None, iNode=None, tNode=None):
		Weapons_Main.__init__(self, info=info, cLogic=cLogic, cNode=cNode, iNode=iNode, tNode=tNode)



	def When_Active(self, direction):
		if direction == 'up':
			new_Coords = self._kNode.Controlled_Move(myCoords=self._info.get_myCoords(), ID=self._info.get_ID(), direction='up', speed=self._info.get_speed())
			self._info.set_myCoords(new_Coords)
			self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))
		elif direction == 'down':
			new_Coords = self._kNode.Controlled_Move(myCoords=self._info.get_myCoords(), ID=self._info.get_ID(), direction='down', speed=self._info.get_speed())
			self._info.set_myCoords(new_Coords)
			self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))
		elif direction == 'left':
			new_Coords = self._kNode.Controlled_Move(myCoords=self._info.get_myCoords(), ID=self._info.get_ID(), direction='left', speed=self._info.get_speed())
			self._info.set_myCoords(new_Coords)
			self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))
		elif direction == 'right':
			new_Coords = self._kNode.Controlled_Move(myCoords=self._info.get_myCoords(), ID=self._info.get_ID(), direction='right', speed=self._info.get_speed())
			self._info.set_myCoords(new_Coords)
			self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	# def get_


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	# def set_
