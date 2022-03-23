from ..weapons_main import Weapons_Main
from .sword_info import Sword_Info
from Engine import *

class Sword_Main(Weapons_Main):
	def __init__(self, ID=None, cLogic=None, cNode=None, iNode=None, tNode=None):
		Weapons_Main.__init__(self, info=Sword_Info(ID='W#S001'), cLogic=cLogic, cNode=cNode, iNode=iNode, tNode=tNode)

	def Sword_Setup(self):
		#img setup
		imageInfo = self._iNode.Image_Add('z_Pictures/notasword.png')
		self._info.Image_Data(size=imageInfo[1], pilImage=imageInfo[0], tkImage=imageInfo[2], fileLoc='z_Pictures/notasword.png')
		self._info.Sword_Data(2) #check melee_info for well info.



	def Use_Sword(self, x, y, direction):
		ID = self._info.get_ID()
		groupID = self._info.get_groupID()
		if self._isActive == False:
			self._info.set_myCoords(coords=(x, y))

			if direction == 'up':
				newImage = self._iNode.Image_Rotate(self._info.get_pilImage(), 90)
				self._info.set_tkImage(newImage)
				self._iNode.Image_Place(x, y, self._info.get_tkImage(), tag=[ID, groupID])
			if direction == 'down':
				newImage = self._iNode.Image_Rotate(self._info.get_pilImage(), 270)
				self._info.set_tkImage(newImage)
				self._iNode.Image_Place(x, y, self._info.get_tkImage(), tag=[ID, groupID])
			if direction == 'left':
				newImage = self._iNode.Image_Rotate(self._info.get_pilImage(), 180)
				self._info.set_tkImage(newImage)
				self._iNode.Image_Place(x, y, self._info.get_tkImage(), tag=[ID, groupID])
			if direction == 'right':
				newImage = self._iNode.Image_Rotate(self._info.get_pilImage(), 0)
				self._info.set_tkImage(newImage)
				self._iNode.Image_Place(x, y, self._info.get_tkImage(), tag=[ID, groupID])

			Image_Node.Render.addtag_withtag(groupID, ID)
			self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))
			self._saveTime = Timer_Node.GameTime

			self._isActive = True

		#this may not be needed, depends for now.
	def My_Collision(self):
		pass



	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_pilImage(self):
		return self._info.get_pilImage()

	def get_tkImage(self):
		return self._info.get_tkImage()


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_isActive(self, Fort):
		self._isActive = Fort
