from Engine import *
from .projectile_main import Projectile_Main
from .arrow_info import Arrow_Info

class Arrow_Main(Projectile_Main):
	def __init__(self, itemCount, cLogic, iNode, tNode):
		Projectile_Main.__init__(self, info=Arrow_Info("P#A00"+str(itemCount)), cLogic=cLogic, iNode=iNode, tNode=tNode)
		self.__direction = None

	def Arrow_SetUP(self):
		#img setup
		imageInfo = self._iNode.Image_Add('z_Pictures/arrow_.png')
		self._info.Image_Data(size=imageInfo[1], pilImage=imageInfo[0], tkImage=imageInfo[2], fileLoc='z_Pictures/arrow_.png')


	def Use_Projectile(self, x, y, direction, dmgMod):
		self.Arrow_SetUP()
		self.__direction = direction
		if self.__direction == 'up':
			# print('up')s
			newImage = self._iNode.Image_Rotate(self._info.get_pilImage(), 90)
			self._info.set_tkImage(newImage)
			self._iNode.Image_Place(x, y, self._info.get_tkImage(), tag=[self._info.get_ID(), self._info.get_groupID()])
			# self.When_Active((x, y), direction)
		elif self.__direction == 'down':
			# print('down')s
			newImage = self._iNode.Image_Rotate(self._info.get_pilImage(), 270)
			self._info.set_tkImage(newImage)
			self._iNode.Image_Place(x, y, self._info.get_tkImage(), tag=[self._info.get_ID(), self._info.get_groupID()])
			# self.When_Active((x, y), direction)
		elif self.__direction == 'left':
			# print('left')s
			newImage = self._iNode.Image_Rotate(self._info.get_pilImage(), 180)
			self._info.set_tkImage(newImage)
			self._iNode.Image_Place(x, y, self._info.get_tkImage(), tag=[self._info.get_ID(), self._info.get_groupID()])
			# self.When_Active((x, y), direction)
		elif self.__direction == 'right':
			# print('right') #this is snormal direction
			newImage = self._iNode.Image_Rotate(self._info.get_pilImage(), 0)
			self._info.set_tkImage(newImage)
			self._iNode.Image_Place(x, y, self._info.get_tkImage(), tag=[self._info.get_ID(), self._info.get_groupID()])
			# self.When_Active((x, y), direction)

		self._isActive = True
		#final half of Arrow_setUP
		self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))
		self._info.Arrow_Data(attack=2+dmgMod, coords=(x, y), speed=15)


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_direction(self):
		return self.__direction


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	#def set_
