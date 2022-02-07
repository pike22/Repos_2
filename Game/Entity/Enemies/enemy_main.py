from ..entity_main import Entity_Main
from Engine import *

#Parenet: Entity_Main
#Children:
	#Stalfos_Main
	#CPU_Stalfos_Main

class Enemy_Main(Entity_Main):
	def __init__(self, info, cLogic=None, cNode=None, iNode=None, tNode=None):
		Entity_Main.__init__(self, info=info, cLogic=cLogic, cNode=cNode, iNode=iNode, tNode=tNode)
		self.Var = 1

	#Brain Power Level [BPL]
	def CPU_MoveControll(self, BPL='BPL=0', L1Pack=None):
		#level packs is a tuple of the required info of the BPL
		#BPL options
			# 'BPL=0' Random movement
			# 'BPL=1' Simple follow player
			# 'BPL=2' Advanced follow player.

		#General Info
		my_w, my_h = self._info.get_size()
		my_x, my_y = self._info.get_myCoords()

		#Level 0: sets movement in random directions, and is the defult.
		if BPL == 'BPL=0':
			if Timer_Node.GameTime == self.Var:
				self.randNumb = int(self._rand.randint(0, 3))
				self.Var += 11

			if self.randNumb == 0:
				newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), 'left', self._info.get_speed())
				self.Move_Sets(newCoords)
			elif self.randNumb == 1:
				newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), 'right', self._info.get_speed())
				self.Move_Sets(newCoords)
			elif self.randNumb == 2:
				newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), 'up', self._info.get_speed())
				self.Move_Sets(newCoords)
			elif self.randNumb == 3:
				newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), 'down', self._info.get_speed())
				self.Move_Sets(newCoords)
		#level 1: Simply follows the player, regardless of obsticles.
		elif BPL == 'BPL=1':
			pl_x, pl_y = L1Pack
			if my_x > pl_x or my_x > pl_x+my_w:
				newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), 'left', speed=self._info.get_speed())
				self.Move_Sets(newCoords)
			if my_x < pl_x or my_x < pl_x+my_w:
				newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), 'right', speed=self._info.get_speed())
				self.Move_Sets(newCoords)
			if my_y > pl_y or my_y > pl_y+my_h:
				newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), 'up', speed=self._info.get_speed())
				self.Move_Sets(newCoords)
			if my_y < pl_y or my_y < pl_y+my_h:
				newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), 'down', speed=self._info.get_speed())
				self.Move_Sets(newCoords)
		#level 2: Advanced follow/ moves around obsticles to follow player.
		elif BPL == 'BPL=2':
			playerLoc, var = L2Pack
			pl_x, pl_y = playerLoc
			if my_x > pl_x or my_x > pl_x+my_w:
				newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), 'left', speed=self._info.get_speed())
				self.Move_Sets(newCoords)
			if my_x < pl_x or my_x < pl_x+my_w:
				newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), 'right', speed=self._info.get_speed())
				self.Move_Sets(newCoords)
			if my_y > pl_y or my_y > pl_y+my_h:
				newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), 'up', speed=self._info.get_speed())
				self.Move_Sets(newCoords)
			if my_y < pl_y or my_y < pl_y+my_h:
				newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), 'down', speed=self._info.get_speed())
				self.Move_Sets(newCoords)
