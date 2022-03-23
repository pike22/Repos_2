from ..weapons_main import Weapons_Main
from .bow_info import Bow_Info
from ..Projectiles import *
from Engine import *

class Bow_Main(Weapons_Main):
	def __init__(self, cLogic, cNode, iNode, tNode):
		Weapons_Main.__init__(self, info=Bow_Info(ID='W#B001'), cLogic=cLogic, cNode=cNode, iNode=iNode, tNode=tNode)
		self.__ammo		 = None
		self.__direction = None

		'''Projectile Parameters'''
		self.__projActive = False
		self.__projCount  = 0
		self.__projID	  = []


	def Bow_Setup(self):
		#img setup
		imageInfo = self._iNode.Image_Add('z_Pictures/bow_.png')
		self._info.Image_Data(size=imageInfo[1], pilImage=imageInfo[0], tkImage=imageInfo[2], fileLoc='z_Pictures/bow_.png')
		self._info.Bow_Data(3)

		#self.output = self.Image.

	def Use_Bow(self, x, y, direction):
		self._info.set_myCoords((x, y))
		height, width = self._info.get_size()
		if self._isActive == False:
			#intial bow render and variable updates
			self.__direction = direction
			self.__projCount += 1
			self._isActive   = True

			#this creates arrow and saves the current state to collision
			self.__ammo = Arrow_Main(iNode=self._iNode, cLogic=self._cLogic, itemCount=self.__projCount, tNode=self._tNode)
			self.__projID.append(self.__ammo.get_ID())
			self._cLogic.Add_CollisionDict(tagOrId=self.__ammo.get_ID(), obj=self.__ammo)

			#this is for what direction the arrow flies
			if direction == 'up':
				# print((x, y), 'bow Coords')
				newImage = self._iNode.Image_Rotate(self._info.get_pilImage(), 90)
				self._info.set_tkImage(newImage)
				self._iNode.Image_Place(x, y, self._info.get_tkImage(), tag=[self._info.get_ID(), self._info.get_groupID()])
				self.__ammo.Use_Projectile(x, (y-width), 'up', dmgMod=self._info.get_attack())
			elif direction == 'down':
				# print((x, y), 'bow Coords')
				newImage = self._iNode.Image_Rotate(self._info.get_pilImage(), 270)
				self._info.set_tkImage(newImage)
				self._iNode.Image_Place(x, y, self._info.get_tkImage(), tag=[self._info.get_ID(), self._info.get_groupID()])
				self.__ammo.Use_Projectile(x, (y+width), 'down', dmgMod=self._info.get_attack())
			elif direction == 'left':
				# print((x, y), 'bow Coords')
				newImage = self._iNode.Image_Rotate(self._info.get_pilImage(), 180)
				self._info.set_tkImage(newImage)
				self._iNode.Image_Place(x, y, self._info.get_tkImage(), tag=[self._info.get_ID(), self._info.get_groupID()])
				self.__ammo.Use_Projectile((x-height), y, 'left', dmgMod=self._info.get_attack())
			elif direction == 'right':
				# print((x, y), 'bow Coords')
				newImage = self._iNode.Image_Rotate(self._info.get_pilImage(), 0)
				self._info.set_tkImage(newImage)
				self._iNode.Image_Place(x, y, self._info.get_tkImage(), tag=[self._info.get_ID(), self._info.get_groupID()])
				self.__ammo.Use_Projectile((x+height), y, 'right', dmgMod=self._info.get_attack())

			#finishing the render of the bow
			Image_Node.Render.addtag_withtag(self._info.get_groupID(), self._info.get_ID())
			self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))
			self._saveTime = Timer_Node.GameTime

	def Proj_Active(self, numb=None):
		if numb != None:
			if self._cLogic.Tag_toObject(self.__projID[numb]).get_isActive() == True:
				self._cLogic.Tag_toObject(self.__projID[numb]).When_Active(direction=self._cLogic.Tag_toObject(self.__projID[numb]).get_direction())

		#this may not be needed, depends for now.
	def My_Collision(self):
		pass



	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	# def get_


	"""#|---------Projectile-Getters--------|#"""
	def get_projCount(self):
		return self.__projCount

	def get_projID(self, numb=None):
		if numb == None:
			return self.__projID
		else:
			return self.__projID[numb]

	def get_projActive(self, numb=None):
		if numb == None:
			if self.__projID == []:
				return False
		else:
			if self.__projID[numb] in self._cLogic.CollisionDict_Keys():
				return self._cLogic.Tag_toObject(self.__projID[numb]).get_isActive()

	def get_projCorners(self, numb=None):
		if numb == None:
			pass
		else:
			return self._cLogic.Tag_toObject(self.__projID[numb]).get_myCorners()

	def get_projCoords(self, numb=None):
		if numb == None:
			pass
		else:
			return self._cLogic.Tag_toObject(self.__projID[numb]).get_myCoords()

	def get_projClass(self, numb=None):
		if numb == None:
			pass
		else:
			return self._cLogic.Tag_toObject(self.__projID[numb])


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_isActive(self, Fort):
		self._isActive = Fort

	def set_ammo(self, ammo):
		self.__ammo = ammo
