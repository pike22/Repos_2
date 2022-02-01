from Engine import *
import random

#Parent: Main_Node
#Children:
	#Enemy_Main
	#Player_Main

class Entity_Main(Main_Node):
	def __init__(self, info, cLogic=None, cNode=None, iNode=None, tNode=None):
		Main_Node.__init__(self, info=info, cLogic=cLogic, cNode=cNode, iNode=iNode, tNode=tNode)
		self._rand = random

		#---Controlls---#
		self._keyUP		= 'w'
		self._keyDOWN	= 's'
		self._keyLEFT	= 'a'
		self._keyRIGHT	= 'd'
		self._ranged	= 'l'
		self._melee		= 'k'

		#---Active Parameters---#
		self._lastDir	= None #last Directions looked
		self._myHealth	= 0

		self._isStatic	= False
		self._isMoving	= False
		self._isAttack	= False
		self._isAlive	= True
		self._isHit		= False


	def Reset_Hit(self, Name=None):
		if Timer_Node.GameTime == self._saveTime+5:
			self._isHit = False
			print(str(Name)+' Can Get Hit')
			print(self._myHealth, ':'+str(Name)+' Health')

	def Check_Health(self):
		if self._isHit == True:
			if self._myHealth > 0:
				# print('Alive')
				return True
			elif self._myHealth <= 0:
				Image_Node.Render.delete(self._info.get_ID())
				self._cLogic.Del_CollisionDict(self._info.get_ID())
				return False
		elif self._isHit == False:
			print("Error: 'self._isHit == False' \n\t Game\Entity\entity_main.py Check_Health #41")

	def Self_Move(self, ):
		pass

	#OSC == Other Side of Collision, it represents the other object that collided with player
	#OSA == Other Side's Attack, represents the other objects needed parameters.
	def My_Collision(self, OSC=None, OSA=None, side=None, staticsList=None):
		# print('My_Collision:\n\t', OSC)
		if self._isHit == False:
			if OSC == None:
				return
			#__Other Side Collision: Static__#
			elif OSC == 'Static':
				for newSide in side:
					if newSide == 'top':
						side = 'up'
					elif newSide == 'bottom':
						side = 'down'
					else:
						side = newSide
					new_Coords = self._kNode.Static_Hit(self._info.get_myCoords(), self._info.get_ID(), side, speed=self._info.get_speed())
					self._info.set_myCoords(new_Coords)
					self._info.set_myCorners(self._info.get_ID())
				#__Other Side Collision: Enemy/Weapon/Friend__#
			elif OSC == 'Enemy' or OSC == 'Weapon' or OSC == 'Friend':
				#---------------Math---------------#
				if OSC != 'Friend':
					self._myHealth -= OSA
				for newSide in side:
					if newSide == 'top':
						side = 'up'
					elif newSide == 'bottom':
						side = 'down'
					else:
						side = newSide
					for time in range(50):
						newCoords = self._kNode.Knock_Back(self._info.get_myCoords(), self._info.get_ID(), side)
						self._info.set_myCoords(newCoords)
						self._info.set_myCorners(self._info.get_ID())
						possibleCollide = self._cLogic.Check_forCollision(self._info.get_ID())
						if possibleCollide != None:
							#print(possibleCollide, 'MyCollision')
							for obj in possibleCollide:
								if obj != None:
									if obj.get_groupID() in staticsList:
										direction = self._cLogic.Side_Calc(self._cLogic.Tag_toObject(self._info.get_ID()))
										self.My_Collision(OSC='Static', side=direction)
										return
				#---------------Logic---------------#
				if OSC != 'Friend':
					self._isHit		= True
					self._isAlive	= self.Check_Health()
					self._saveTime	= Timer_Node.GameTime


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_isAlive(self):
		return self._isAlive

	def get_isHit(self):
		return self._isHit

	def get_isMoving(self):
		return self.__isMoving

	def get_isAttack(self):
		return self.__isAttack



	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	# def set_isAlive(self, isAlive):
	# 	self._isAlive = isAlive
