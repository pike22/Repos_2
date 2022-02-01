from .collision_logic import Collision_Logic

#use this for the games loop collision
class Collision_Node():
	def __init__(self, clNode):
		self.__logic = clNode

		#different obj needed for collision node
		self.__stalfosRoster = None
		self.__playerRoster  = None
		self.__staticRoster	 = None
		self.__weaponRoster	 = None
		self.__slimeRoster	 = None
		self.__enemyRoster	 = None
		self.__wallRoster	 = None
		self.__projRoster	 = None

		#COllision Result save
		self.__result  = None
		self.__tempVar = None
		self.__wallHIT = None


	def Use_Collision(self, cornerList, totItemCount):
		self.__logic.Add_Collision(listofCorners=cornerList)

		self.__result = None
		for loopCount in range(totItemCount):
			self.__result = self.__logic.Is_Collision(loopCount)
			# print('-----------', loopCount, '---------:TIME THROUGH LOOP')
			# print(cornerList[loopCount], loopCount,"'s item corner")

			# if self.__result != []:
			# 	print('--------------------------------------')
			# 	print("-------------'result'-----------------")
			# 	print(self.__result)
			# 	print('--------------------------------------')


			"""Col_Dict = self.__logic.get_Col_Dict() #this may not be needed"""
			if self.__result != []:
				for item in range(len(self.__result)):
					# print('\titem:', item)
					# print('\ttag: ', self.__result[item].get_ID())
					# print('----------------------')

					"""#__# PLAYER COL_LOGIC #__#"""
					if self.__result[item].get_ID() in self.__playerRoster:
						side = self.__logic.Side_Calc(self.__result[item])
						if len(self.__result) >= 2:
							if item == 0:
								if self.__result[item+1].get_groupID() in self.__weaponRoster:
									self.__result[item+1].Del_Item()
								elif self.__result[item+1].get_groupID() in self.__staticRoster:
									self.__result[item].My_Collision(OSC='Static', side=side)
							else:
								if self.__result[item-1].get_groupID() in self.__enemyRoster:
									self.__result[item].My_Collision(OSC='Enemy', OSA=self.__result[item-1].get_attack(), side=side, staticsList=self.__staticRoster)

					"""#__# STALFOS COL_LOGIC #__#"""
					if self.__result[item].get_ID() in self.__stalfosRoster:
						side = self.__logic.Side_Calc(self.__result[item])
						# print('stalfos direction:', side)
						# print(len(self.__result))
						if len(self.__result) >= 2:
							if item == 0:
								if self.__result[item+1].get_groupID() in self.__staticRoster:
									self.__result[item].My_Collision(OSC='Static', side=side)
									self.__wallHIT = True
									# print(self.__wallHIT)
							elif item == 1:
								if self.__result[item-1].get_groupID() in self.__weaponRoster:
									self.__result[item].My_Collision(OSC="Weapon", OSA=self.__result[item-1].get_attack(), side=side, staticsList=self.__staticRoster)
								elif self.__result[item-1].get_groupID() in self.__projRoster:
									self.__result[item].My_Collision(OSC="Weapon", OSA=self.__result[item-1].get_attack(), side=side, staticsList=self.__staticRoster)
									self.__result[item-1].Del_Item()
								elif self.__result[item-1].get_groupID() in self.__enemyRoster:
									self.__result[item].My_Collision(OSC='Friend', side=side, staticsList=self.__staticRoster)

					if self.__result[item].get_ID() in self.__slimeRoster:
						side = self.__logic.Side_Calc(self.__result[item])
						# print('stalfos direction:', side)
						# print(len(self.__result))
						if len(self.__result) >= 2:
							if item == 0:
								if self.__result[item+1].get_groupID() in self.__staticRoster:
									self.__result[item].My_Collision(OSC='Static', side=side)
									self.__wallHIT = True
									# print(self.__wallHIT)
							elif item == 1:
								if self.__result[item-1].get_groupID() in self.__weaponRoster:
									self.__result[item].My_Collision(OSC="Weapon", OSA=self.__result[item-1].get_attack(), side=side, staticsList=self.__staticRoster)
								elif self.__result[item-1].get_groupID() in self.__projRoster:
									self.__result[item].My_Collision(OSC="Weapon", OSA=self.__result[item-1].get_attack(), side=side, staticsList=self.__staticRoster)
									self.__result[item-1].Del_Item()
								elif self.__result[item-1].get_groupID() in self.__enemyRoster:
									self.__result[item].My_Collision(OSC='Friend', side=side, staticsList=self.__staticRoster)

					"""#__# WEAPON COL_LOGIC #__#"""
					if self.__result[item] == self.__logic.Tag_toObject('W#S001'): #weapon will always be last
						#print('Sword')
						pass
					if self.__result[item] == self.__logic.Tag_toObject('W#B001'):
						#print('Bow')
						pass

					"""#__# STATIC COL_LOGIC #__#"""
					if self.__result[item].get_ID() in self.__wallRoster:
						if len(self.__result) >= 2:
							if item == 0:
								# print('hell0')
								pass
							elif item == 1:
								# print('goodbye')
								# print(self.__result[item].get_groupID(), 'item:',item)
								if self.__result[item-1].get_groupID() in self.__weaponRoster:
									print('CLANG!!!!!')
								if self.__result[item-1].get_groupID() in self.__projRoster:
									self.__result[item-1].Del_Item()
							else:
								# print('wut the CN#101')
								pass
		# print('--------------------------------------')



	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_wallHIT(self):
		return self.__wallHIT


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_playerRoster(self, Roster):
		self.__playerRoster = Roster
		self.__logic.set_playerRoster(Roster)

	def set_enemyRoster(self, Roster):
		self.__enemyRoster = Roster
		self.__logic.set_enemyRoster(Roster)

	def set_stalfosRoster(self, Roster):
		self.__stalfosRoster = Roster
		self.__logic.set_stalfosRoster(Roster)

	def set_slimeRoster(self, Roster):
		self.__slimeRoster = Roster
		self.__logic.set_slimeRoster(Roster)

	def set_weaponRoster(self, Roster):
		self.__weaponRoster = Roster
		self.__logic.set_weaponRoster(Roster)

	def set_projRoster(self, Roster):
		self.__projRoster = Roster
		self.__logic.set_projRoster(Roster)

	def set_staticRoster(self, Roster):
		self.__staticRoster = Roster
		self.__logic.set_staticRoster(Roster)

	def set_wallRoster(self, Roster):
		self.__wallRoster = Roster
		self.__logic.set_wallRoster(Roster)
