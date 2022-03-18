from .collision_logic_v2 import Collision_Logic_v2

#use this for the games loop collision
class Collision_Node_v2():
	def __init__(self, cLogic):
		self.__logic = cLogic

		#<--Rosters-->#
		self._staticRoster	= None #Objects that can't move, Exclude Walls
		self._playerRoster	= None #Player Objects
		self._enemyRoster	= None #Enemy Objects
		self._weapRoster	= None #Any Weapons Objects
		self._projRoster	= None #Any Flying Objects
		self._wallRoster	= None #Wall Objects

		#<--Collision Results-->#
		self.__cResult = None #Collision
		self.__sResult = None #Side
		self.__wallHit = None


	def Use_Collision(self, tag):
		self.__cResult = self.__logic.Is_Collision(tag)

		for object in self.__cResult:
			print(object)


			#<--Player_Collision-->#
			if object.get_ID() in self._playerRoster:
				print("Player")

			#<--Enemy_Collision-->#
			if object.get_ID() in self._enemyRoster:
				print("Enemy")

			#<--Weapon_Collision-->#
			if object.get_ID() in self._weapRoster:
				print("Weapon")

			#<--Static_Collision-->#
			if object.get_ID() in self._staticRoster:
				print("Statics")
			
