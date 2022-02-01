from .enemy_main import Enemy_Main
from .slime_info import Slime_Info
from Engine import *

class Slime_Main(Enemy_Main):
	def __init__(self, ID, cLogic, iNode):
		Enemy_Main.__init__(self, info=Slime_Info(ID), cLogic=cLogic, iNode=iNode)

		#----Temp Var----#
		self.__x	= 0
		self.__y	= 0
		self.__var	= 1
		self._randNum = None

	def Slime_SetUP(self, screenWidth, screenHeight):
		#img setup
		ID = self._info.get_ID()
		group_ID = self._info.get_groupID()
		imageInfo = self._iNode.Image_Add('z_Pictures/slime.png')
		self._info.Image_Data(size=imageInfo[1], pilImage=imageInfo[0], tkImage=imageInfo[2], fileLoc='z_Pictures/slime.png')

		#placing the img
		self.__x = 0
		self.__y = 0
		x, y = self._info.get_size()
		occupied = True
		while occupied == True:
			self.__x = int(self._rand.randint((32+x), screenWidth-(32+x)))
			self.__y = int(self._rand.randint((x+32), screenHeight-(32+y)))
			objects = self._cLogic.Check_forCollision(objCorners=(self.__x, self.__y, self.__x+x, self.__y+y))
			# print(objects)
			if objects != None and len(objects) >= 0:
				print('someones here.')
			else:
				occupied = False
		self._iNode.Image_Place(x=self.__x, y=self.__y, image=self._info.get_tkImage(), tag=[ID, self._info.get_groupID()])

		#final set of information save to Slime
		self._info.Slime_Data(coords=(self.__x, self.__y), speed=5, health=10, defense=5, attack=2) #check Slime_info for well info.
		Image_Node.Render.addtag_withtag(group_ID, self._info.get_ID())
		self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))

		#Acitve Parameters
		self._myHealth = self._info.get_health()

	def Movement_Controll(self, playerLoc):
		my_x, my_y = self._info.get_myCoords()
		pl_x, pl_y = playerLoc
		if my_x > pl_x:
			direction = 'left'
			new_Coords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), direction, speed=self._info.get_speed())
			self._info.set_myCoords(new_Coords)
			self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))
			self._isMoving = True
		if my_x < pl_x:
			direction = 'right'
			new_Coords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), direction, speed=self._info.get_speed())
			self._info.set_myCoords(new_Coords)
			self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))
			self._isMoving = True
		if my_y > pl_y:
			direction = 'up'
			new_Coords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), direction, speed=self._info.get_speed())
			self._info.set_myCoords(new_Coords)
			self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))
			self._isMoving = True
		if my_y < pl_y:
			direction = 'down'
			new_Coords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), direction, speed=self._info.get_speed())
			self._info.set_myCoords(new_Coords)
			self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))
			self._isMoving = True

	def Stal_Attack(self):
		pass


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	# def get_


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	# def set_
