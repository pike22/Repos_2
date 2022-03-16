import review
from .image_node import Image_Node

class Collision_Logic_v2():
	def __init__(self, width=None, height=None):


		#--Grid Parameters--#
		self.__Grid		= {}
		self._heightSC	= height
		self._widthSC	= width
		self._boxSize	= 32
		self._xPos		= 0
		self._yPos		= 0


	#--Collision's Engine--#
	def Create_Grid(self, ):
		boxCountX = int(self._widthSC/self._boxSize)
		boxCountY = int(self._heightSC/self._boxSize)

		boxNumb = 0
		for x in range(boxCountX+1):
			if x == 0:
				self._xPos = 0
			else:
				self._xPos += self._boxSize
			for y in range(boxCountY+1):
				self._yPos += self._boxSize
				if y == (boxCountY):
					self._yPos = 0
				boxNumb+=1
				self.__Grid[boxNumb] = (self._xPos, self._yPos)
				print((self._xPos, self._yPos), 'box coords\t', y)
			print('<----------------------------------------->')

	def Add_Collision(self, ):
		pass
	
