#here will be the Stalfos's controller
from .enemy_main import Enemy_Main
from .stalfos_info import Stalfos_Info
from Engine import *

class Stalfos_Main(Enemy_Main):
	def __init__(self, ID, cLogic, iNode):
		Enemy_Main.__init__(self, info=Stalfos_Info(ID), cLogic=cLogic, iNode=iNode)

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
		self.__x, self.__y = self.Random_Place(self._info.get_size(), screenWidth, screenHeight)
		self._iNode.Image_Place(x=self.__x, y=self.__y, image=self._info.get_tkImage(), tag=[ID, self._info.get_groupID()])

		#final set of information save to stalfos numb.
		self._info.Stalfos_Data(coords=(self.__x, self.__y), speed=5, health=10, defense=5, attack=2)
		self._info.set_myCorners(self._info.get_ID())

		#Active Parameters
		self._myHealth = self._info.get_health()

	def Movement_Controll(self):
		self.CPU_MoveControll() #BPL=0
		collision = self._cLogic.Check_forCollision(objCorners=self._info.get_myCorners())
		if collision == []:
			self.My_Collision()

	def Stal_Attack(self):
		pass


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	# def get_

	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	# def set_
