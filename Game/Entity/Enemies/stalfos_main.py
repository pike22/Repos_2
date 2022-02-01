#here will be the Stalfos's controller
from .enemy_main import Enemy_Main
from .stalfos_info import Stalfos_Info
from Engine import *

import random

class Stalfos_Main(Enemy_Main):
	def __init__(self, ID, cLogic, iNode):
		Enemy_Main.__init__(self, info=Stalfos_Info(ID), cLogic=cLogic, iNode=iNode)
		self.__rand   = random

		#----Temp Var----#
		self.__x	= 0
		self.__y	= 0
		self.__var	= 1
		self.__randNum = None


	#seting up player bellow
	def Stalfos_SetUP(self, screenWidth, screenHeight):
		#img setup
		ID = self._info.get_ID()
		imageInfo = self._iNode.Image_Add('z_Pictures/bloodboy.png')
		self._info.Image_Data(size=imageInfo[1], pilImage=imageInfo[0], tkImage=imageInfo[2], fileLoc='z_Pictures/bloodboy.png')

		#placing the img
		self.__x = 0
		self.__y = 0
		x, y = self._info.get_size()
		occupied = False
		while occupied == False:
			self.__x = int(self.__rand.randint((32+x), screenWidth-(32+x)))
			self.__y = int(self.__rand.randint((32+x), screenHeight-(32+y)))
			objects = self._cLogic.Check_forCollision(objCorners=(self.__x, self.__y, self.__x+x, self.__y+y))
			# print(objects)
			if objects != None and len(objects) >= 0:
				print('someones here.')
			else:
				occupied = True
		self._iNode.Image_Place(x=self.__x, y=self.__y, image=self._info.get_tkImage(), tag=[ID, self._info.get_groupID()])

		#final set of information save to stalfos numb.
		self._info.Stalfos_Data(coords=(self.__x, self.__y), speed=5, health=10, defense=5, attack=2) #check stalfos_info for, well info.
		self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))

		#Active Parameters
		self._myHealth = self._info.get_health()

	def Movement_Controll(self):
		if Timer_Node.GameTime == self.__var:
			self.__randNum = int(self.__rand.randint(0, 3))
			# print(self.__var, S#82)
			self.__var += 11

		if self.__randNum == 0:
			direction = "up"
			new_Coords = self._kNode.Controlled_Move(myCoords=self._info.get_myCoords(), ID=self._info.get_ID(), direction=direction, speed=self._info.get_speed())
			self._info.set_myCoords(new_Coords)
			self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))
			self._isMoving = True
		elif self.__randNum == 1:
			direction = "right"
			new_Coords = self._kNode.Controlled_Move(myCoords=self._info.get_myCoords(), ID=self._info.get_ID(), direction=direction, speed=self._info.get_speed())
			self._info.set_myCoords(new_Coords)
			self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))
			self._isMoving = True
		elif self.__randNum == 2:
			direction = "down"
			new_Coords = self._kNode.Controlled_Move(myCoords=self._info.get_myCoords(), ID=self._info.get_ID(), direction=direction, speed=self._info.get_speed())
			self._info.set_myCoords(new_Coords)
			self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))
			self._isMoving = True
		elif self.__randNum == 3:
			direction = "left"
			new_Coords = self._kNode.Controlled_Move(myCoords=self._info.get_myCoords(), ID=self._info.get_ID(), direction=direction, speed=self._info.get_speed())
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
