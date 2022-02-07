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
		self.__x, self.__y = self.Random_Place(self._info.get_size(), screenWidth, screenHeight)
		self._iNode.Image_Place(x=self.__x, y=self.__y, image=self._info.get_tkImage(), tag=[ID, self._info.get_groupID()])

		#final set of information save to Slime
		self._info.Slime_Data(coords=(self.__x, self.__y), speed=5, health=10, defense=5, attack=2) #check Slime_info for well info.
		Image_Node.Render.addtag_withtag(group_ID, self._info.get_ID())
		self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))

		#Acitve Parameters
		self._myHealth = self._info.get_health()

	def Movement_Controll(self, playerLoc):
		self.CPU_MoveControll(BPL='BPL=1', L1Pack=playerLoc)

	def Stal_Attack(self):
		pass


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	# def get_


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	# def set_
